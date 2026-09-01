"""Local static server WITH HTTP Range support (python -m http.server lacks it).

PMTiles reads need byte ranges; without them protomaps/pmtiles error out
("Server returned no content-length header..."). Usage:

    python scratch/serve_range.py [port] [directory]

Defaults: port 8000, directory = repo root (parent of this file's folder).
"""
import os
import re
import sys
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer

RANGE_RE = re.compile(r"bytes=(\d*)-(\d*)$")


class RangeHandler(SimpleHTTPRequestHandler):
    def send_head(self):
        path = self.translate_path(self.path)
        rng = self.headers.get("Range")
        if rng and os.path.isfile(path):
            m = RANGE_RE.match(rng.strip())
            if m and (m.group(1) or m.group(2)):
                size = os.path.getsize(path)
                if m.group(1):
                    start = int(m.group(1))
                    end = int(m.group(2)) if m.group(2) else size - 1
                else:  # suffix form bytes=-N (last N bytes)
                    start = max(0, size - int(m.group(2)))
                    end = size - 1
                end = min(end, size - 1)
                if start >= size or start > end:
                    self.send_response(416)
                    self.send_header("Content-Range", "bytes */%d" % size)
                    self.end_headers()
                    return None
                f = open(path, "rb")
                f.seek(start)
                self.send_response(206)
                self.send_header("Content-Type", self.guess_type(path))
                self.send_header("Accept-Ranges", "bytes")
                self.send_header("Content-Range", "bytes %d-%d/%d" % (start, end, size))
                self.send_header("Content-Length", str(end - start + 1))
                self.end_headers()
                self._range_span = (start, end)
                return f
        return super().send_head()

    def copyfile(self, source, outputfile):
        span = getattr(self, "_range_span", None)
        if span is None:
            return super().copyfile(source, outputfile)
        self._range_span = None
        start, end = span
        remaining = end - start + 1
        while remaining > 0:
            chunk = source.read(min(65536, remaining))
            if not chunk:
                break
            outputfile.write(chunk)
            remaining -= len(chunk)


def main():
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 8000
    default_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    directory = sys.argv[2] if len(sys.argv) > 2 else default_dir
    handler = partial(RangeHandler, directory=directory)
    with ThreadingHTTPServer(("127.0.0.1", port), handler) as httpd:
        print("serving %s on http://127.0.0.1:%d (with Range support)" % (directory, port))
        httpd.serve_forever()


if __name__ == "__main__":
    main()
