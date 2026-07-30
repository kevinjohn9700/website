"""
Tiny local server for the Girlfriend's Day website.

Usage:
    python server.py
    (then open the link it prints, e.g. http://localhost:8000)

This is only for previewing the site on your own computer before
pushing it to GitHub Pages. GitHub Pages will host index.html directly,
you won't need this script once it's live.
"""

import http.server
import socketserver
import webbrowser
import os

PORT = 8000

# make sure we serve from the folder this script lives in
os.chdir(os.path.dirname(os.path.abspath(__file__)))

Handler = http.server.SimpleHTTPRequestHandler

def main():
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        url = f"http://localhost:{PORT}"
        print(f"Serving your site at {url}")
        print("Press Ctrl+C to stop.")
        try:
            webbrowser.open(url)
        except Exception:
            pass
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nStopped.")

if __name__ == "__main__":
    main()
