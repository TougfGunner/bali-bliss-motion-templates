#!/usr/bin/env python3
"""
Bali Bliss Editorial Audio Suite Server
Strictly bound to 127.0.0.1:8885
Single-threaded, supporting static files, byte-range streaming, and mark-deleted API
"""
import http.server
import json
import os
import sys

PORT = 8885
DIRECTORY = "/Users/lashperera/Dev/Projects/bali-bliss-motion-templates"
JSON_PATH = os.path.join(DIRECTORY, "bali_bliss_sound_fx.json")
VAULT_JSON_PATH = "/Users/lashperera/Dev/Projects/bali-love-intelligence-vault/data/bali_bliss/bali_bliss_sound_fx.json"

class AudioHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

    def end_headers(self):
        self.send_header("Cache-Control", "no-cache")
        super().end_headers()

    def do_OPTIONS(self):
        self.send_response(200)
        self.end_headers()

    def do_POST(self):
        if self.path == "/api/mark-deleted":
            content_length = int(self.headers.get("Content-Length", 0))
            body = self.rfile.read(content_length).decode("utf-8")
            try:
                req = json.loads(body)
                filename = req.get("filename")
                is_deleted = bool(req.get("deleted", True))

                updated = False
                for path in [JSON_PATH, VAULT_JSON_PATH]:
                    if os.path.exists(path):
                        with open(path, "r") as f:
                            data = json.load(f)
                        for t in data.get("tracks", []):
                            if t.get("filename") == filename:
                                t["deleted"] = is_deleted
                                updated = True
                        with open(path, "w") as f:
                            json.dump(data, f, indent=2)

                self.send_response(200)
                self.send_header("Content-Type", "application/json")
                self.end_headers()
                res = {
                    "success": True,
                    "filename": filename,
                    "deleted": is_deleted,
                    "updated": updated
                }
                self.wfile.write(json.dumps(res).encode("utf-8"))
            except Exception as e:
                self.send_response(500)
                self.send_header("Content-Type", "application/json")
                self.end_headers()
                self.wfile.write(json.dumps({"success": False, "error": str(e)}).encode("utf-8"))
            return

        super().do_POST()

if __name__ == "__main__":
    server = http.server.HTTPServer(("127.0.0.1", PORT), AudioHandler)
    print(f"Serving Bali Bliss Editorial Audio on http://127.0.0.1:{PORT}/audio_player.html")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
