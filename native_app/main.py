from .ws import app, uvicorn

import typer


fast_api = typer.Typer("TabManagerWebServer")


def run(
    port: int = 8001,
    host: str = "0.0.0.0",
):
    uvicorn.run(app, port=port, host=host)
