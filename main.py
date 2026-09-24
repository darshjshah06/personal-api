import json
from pathlib import Path

from fastapi import FastAPI

app = FastAPI(title="Personal API")

DATA_PATH = Path(__file__).parent / "data.json"


def load_data() -> dict:
    with open(DATA_PATH) as f:
        return json.load(f)


@app.get("/")
def root():
    return load_data()


@app.get("/location")
def location():
    return {"location": load_data()["location"]}


@app.get("/working-on")
def working_on():
    return {"working_on": load_data()["working_on"]}


@app.get("/whats-new")
def whats_new():
    return {"whats_new": load_data()["whats_new"]}
