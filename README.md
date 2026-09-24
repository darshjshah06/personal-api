# Personal API

A weekly-updating personal API built with FastAPI — endpoints for my current
location, what I'm working on, and what's new.

## Endpoints

- `GET /` — the full current status
- `GET /location` — current location
- `GET /working-on` — what I'm currently working on
- `GET /whats-new` — latest update
- `GET /history` — every weekly update on record, most recent first

## Running locally

```bash
pip install -r requirements.txt
uvicorn main:app --reload
```

## Updating

`data.json` is a list of weekly entries, most recent first. Each week, add a
new object to the front with an `updated`, `location`, `working_on`, and
`whats_new` value.

## Example Weekly Updates

Here's what `data.json` has looked like week to week:

| Updated | Location | Working On | What's New |
|---|---|---|---|
| 2026-09-21 | Memphis, TN | Building a personal API project for the channel | Just started a new ML healthcare project — more details soon |
| 2026-09-14 | Memphis, TN | Prepping course material for my ML study group | Hit 10k followers on Instagram this week |
| 2026-09-07 | Nashville, TN (visiting family) | Refactoring the personal API and adding new endpoints | Landed my first PR collab with a tech brand |
| 2026-08-31 | Memphis, TN | Wrapping up a computer vision project for my AI coursework | Published a new video breaking down transformers for beginners |
| 2026-08-24 | Memphis, TN | Starting the semester and outlining my ML study group curriculum | Crossed 5k followers on TikTok after a viral CS meme post |

<details>
<summary>Raw JSON for each week</summary>

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

```json
{
  "updated": "2026-08-31",
  "location": "Memphis, TN",
  "working_on": "Wrapping up a computer vision project for my AI coursework",
  "whats_new": "Published a new video breaking down transformers for beginners"
}
```

```json
{
  "updated": "2026-08-24",
  "location": "Memphis, TN",
  "working_on": "Starting the semester and outlining my ML study group curriculum",
  "whats_new": "Crossed 5k followers on TikTok after a viral CS meme post"
}
```

</details>

## Deploying to Vercel

This repo includes a `vercel.json` that runs `main.py` as a Python serverless
function via `@vercel/python`. Import the repo on
[vercel.com/new](https://vercel.com/new) and deploy — no extra config needed.
