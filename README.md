# Legacy HTTP Server

Small local HTTP server to open legacy files in the browser.

This project started as a straightforward solution for cases where an old
page, manual or HTML package does not work well when opened directly from
the filesystem via `file://`.

Some legacy architectures rely on relative paths, `.htm` files,
`windows-1252` encoding, SVG/SVGZ files or behaviors that modern browsers
handle better when content is served over local HTTP.

## What it is for

- Serve a local directory on `http://127.0.0.1:8000`.
- Automatically open a starting page, `index.htm` by default.
- Make legacy content accessible without configuring Apache, Nginx or
  another full web server.
- Preserve basic compatibility with `.htm`, `.html`, `.svg` and `.svgz`.

## What this project is not

- It is not a production server.
- It is not a security solution.
- It does not replace a real migration of legacy systems.
- It must not be exposed to the internet.

The idea is to be a small, direct tool for local use.

## Files

```text
legacy_http_server.py    Local HTTP server
README.md                Project documentation