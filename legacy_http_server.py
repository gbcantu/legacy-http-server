#!/usr/bin/env python3
"""
legacy_http_server.py

Small standard-library HTTP server to serve legacy HTML content over
localhost. Useful when old pages, manuals or HTML packages do not behave
well when opened directly from the filesystem via file://, due to
relative paths, windows-1252 encoding, gzip-encoded SVGZ files or other
behaviors that modern browsers handle better when content is served over
HTTP.

Not intended for production. Listens on 127.0.0.1 by default.

Usage:
    python legacy_http_server.py
    python legacy_http_server.py --port 8080 --page manual.htm
    python legacy_http_server.py --directory ./content --no-browser
"""

import argparse
import mimetypes
import socket
import sys
import webbrowser
from functools import partial
from http.server import HTTPServer, SimpleHTTPRequestHandler

mimetypes.add_type("image/svg+xml", ".svg")
mimetypes.add_type("image/svg+xml", ".svgz")


class LegacyHTTPRequestHandler(SimpleHTTPRequestHandler):
    extensions_map = SimpleHTTPRequestHandler.extensions_map.copy()
    extensions_map.update(
        {
            ".htm": "text/html; charset=windows-1252",
            ".html": "text/html; charset=windows-1252",
            ".svg": "image/svg+xml",
            ".svgz": "image/svg+xml",
        }
    )

    def end_headers(self):
        if self.path.lower().endswith(".svgz"):
            self.send_header("Content-Encoding", "gzip")
        super().end_headers()


class ReuseAddrHTTPServer(HTTPServer):
    def server_bind(self):
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        super().server_bind()


def parse_args():
    parser = argparse.ArgumentParser(
        description="Local HTTP server to open legacy files in the browser."
    )
    parser.add_argument(
        "--host", default="127.0.0.1", help="Address to bind the local server (default: 127.0.0.1)."
    )
    parser.add_argument(
        "--port", type=int, default=8000, help="Port to bind the local server (default: 8000)."
    )
    parser.add_argument(
        "--directory", default=".", help="Directory to serve (default: current directory)."
    )
    parser.add_argument(
        "--page", default="index.htm", help="Page opened automatically (default: index.htm)."
    )
    parser.add_argument(
        "--no-browser",
        action="store_true",
        help="Start the server without opening the browser automatically.",
    )
    return parser.parse_args()


def main():
    args = parse_args()
    handler = partial(LegacyHTTPRequestHandler, directory=args.directory)

    try:
        server = ReuseAddrHTTPServer((args.host, args.port), handler)
    except OSError as exc:
        print(f"Cannot start server on {args.host}:{args.port}: {exc}")
        print("Try another port with --port.")
        sys.exit(1)

    url = f"http://{args.host}:{args.port}/{args.page}"

    print(f"Server running at {url}")
    print("Press Ctrl+C to stop.")

    if not args.no_browser:
        webbrowser.open(url)

    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nServer stopped.")
    finally:
        server.server_close()


if __name__ == "__main__":
    main()