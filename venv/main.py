from fastapi import FastAPI
from Routes import browser_route
from fastapi.responses import HTMLResponse
import uvicorn

app = FastAPI()
app.include_router(browser_route.router)

@app.get("/", response_class=HTMLResponse)
async def root():
    return """
    <html>
        <head>
            <title>Hello World</title>
        </head>
        <body>
            <h1>Hello World</h1>
        </body>
    </html>
    """

if __name__ == "__main__":
    uvicorn.run("main:app", port=5000, log_level="info")