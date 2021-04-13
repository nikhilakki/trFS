from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
import uvicorn
from pathlib import os


app = FastAPI()

folder_path = "/home/pi/share/files"
app.mount("/share/", StaticFiles(directory=folder_path), name="files")

@app.get("/")
def list_all():
    files = [f"<li><a href='/share/{item}'>{item}</li>" for item in os.listdir(folder_path) if item.lower().split(".")[-1] == "pdf"]
    files_html = "\n".join(files)
    html_content = f"""
    <html>
        <head>
            <title>Rpi3 Share File Server</title>
        </head>
        <body>
            <h1>Shared files -</h1>
            <ol>{files_html}</ol>
        </body>
    </html>
    """
    return HTMLResponse(content=html_content, status_code=200)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)

