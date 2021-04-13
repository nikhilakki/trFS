# Copyright (C) 2021 Nikhil Akki
# 
# This file is part of trFS (Tiny RESTful File Server).
# 
# trFS (Tiny RESTful File Server) is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# trFS (Tiny RESTful File Server) is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with trFS (Tiny RESTful File Server).  If not, see <http://www.gnu.org/licenses/>.

from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
import uvicorn
from pathlib import os
from dotenv import load_dotenv

load_dotenv()

folder_path = os.getenv("SHAREPATH", "/home/pi/share/files")
port = os.getenv("PORT", 8080)

app = FastAPI()
app.mount("/share/", StaticFiles(directory=folder_path), name="files")

@app.get("/")
def list_all():
    files = [f"<li><a href='/share/{item}'>{item}</li>" for item in os.listdir(folder_path) if item.lower().split(".")[-1] == "pdf"]
    files_html = "\n".join(files)
    html_content = f"""
    <html>
        <head>
            <title>Rpi Share File Server</title>
        </head>
        <body>
            <h1>Shared files -</h1>
            <ol>{files_html}</ol>
        </body>
    </html>
    """
    return HTMLResponse(content=html_content, status_code=200)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=port)

