# Personal API

A weekly-updating personal API built with FastAPI — endpoints for my current
location, what I'm working on, and what's new.

## Endpoints

- `GET /` — the full current status
- `GET /location` — current location
- `GET /working-on` — what I'm currently working on
- `GET /whats-new` — latest update

## Running locally

```bash
pip install -r requirements.txt
uvicorn main:app --reload
```

## Updating

Edit `data.json` each week with a new `updated`, `location`, `working_on`,
and `whats_new` value.

## Example Weekly Updates

Here's what `data.json` has looked like week to week:

```json
{
  "updated": "2026-09-21",
  "location": "Memphis, TN",
  "working_on": "Building a personal API project for the channel",
  "whats_new": "Just started a new ML healthcare project — more details soon"
}
```

```json
{
  "updated": "2026-09-14",
  "location": "Memphis, TN",
  "working_on": "Prepping course material for my ML study group",
  "whats_new": "Hit 10k followers on Instagram this week"
}
```

```json
{
  "updated": "2026-09-07",
  "location": "Nashville, TN (visiting family)",
  "working_on": "Refactoring the personal API and adding new endpoints",
  "whats_new": "Landed my first PR collab with a tech brand"
}
```
