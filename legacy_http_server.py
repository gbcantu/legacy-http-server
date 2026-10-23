import argparse
from functools import partial
from http.server import HTTPServer, SimpleHTTPRequestHandler
import mimetypes
import socket
import webbrowser

mimetypes.add_type("image/svg+xml", ".svg")
mimetypes.add_type("image/svg+xml", ".svgz")


class LegacyHTTPRequestHandler(SimpleHTTPRequestHandler):
    extensions_map = SimpleHTTPRequestHandler.extensions_map.copy()
    extensions_map.update({
        ".htm": "text/html; charset=windows-1252",
        ".html": "text/html; charset=windows-1252",
        ".svg": "image/svg+xml",
        ".svgz": "image/svg+xml",
    })

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
        description="Servidor HTTP local simples para abrir arquivos legados no navegador."
    )
    parser.add_argument("--host", default="127.0.0.1", help="Endereco do servidor local.")
    parser.add_argument("--port", type=int, default=8000, help="Porta do servidor local.")
    parser.add_argument("--directory", default=".", help="Diretorio que sera servido.")
    parser.add_argument("--page", default="index.htm", help="Pagina aberta automaticamente.")
    parser.add_argument(
        "--no-browser",
        action="store_true",
        help="Inicia o servidor sem abrir o navegador automaticamente.",
    )
    return parser.parse_args()


def main():
    args = parse_args()
    handler = partial(LegacyHTTPRequestHandler, directory=args.directory)
    server = ReuseAddrHTTPServer((args.host, args.port), handler)
    url = f"http://{args.host}:{args.port}/{args.page}"

    print(f"Servidor rodando em {url}")
    print("Pressione Ctrl+C para encerrar.")

    if not args.no_browser:
        webbrowser.open(url)

    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nServidor encerrado.")
    finally:
        server.server_close()


if __name__ == "__main__":
    main()
