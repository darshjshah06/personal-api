import json
from pathlib import Path

from fastapi import FastAPI
from fastapi.responses import JSONResponse

DATA_PATH = Path(__file__).parent / "data.json"


class PrettyJSONResponse(JSONResponse):
    def render(self, content) -> bytes:
        return json.dumps(content, ensure_ascii=False, indent=2).encode("utf-8")


app = FastAPI(title="Personal API", default_response_class=PrettyJSONResponse)


def load_history() -> list[dict]:
    with open(DATA_PATH) as f:
        return json.load(f)


def load_current() -> dict:
    return load_history()[0]


@app.get("/")
def root():
    return load_current()


@app.get("/location")
def location():
    return {"location": load_current()["location"]}


@app.get("/working-on")
def working_on():
    return {"working_on": load_current()["working_on"]}


@app.get("/whats-new")
def whats_new():
    return {"whats_new": load_current()["whats_new"]}


@app.get("/history")
def history():
    return load_history()
