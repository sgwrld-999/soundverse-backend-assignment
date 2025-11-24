Soundverse Backend Intern - Assignment

Here’s your assignment. Please submit it with a demo video and a GitHub repository link.


Objective
Build a backend service for a fictitious feature called "Play" - a lightweight audio library that lets users fetch and stream short audio previews. Your goal is to implement basic API functionality, integrate a database, and deploy it online with simple monitoring.


Scope of Work
You’ll build a backend with FastAPI that allows users to:

Get a list of available sound clips
Stream a specific clip
Track how many times each clip has been played

Features to Implement
1. GET /play
Returns a list of 5–6 dummy sound clips.
Each item should include:
id
title
description
genre (e.g., ambient, pop, electronic)
duration (e.g., 30s)
audio_url (public link to a hosted .mp3 file)
2. GET /play/{id}/stream
Streams the clip’s audio (simulate streaming by sending back the MP3 file using FastAPI's FileResponse or similar).
Increment a play_count in the database for each stream.
3. GET /play/{id}/stats
Returns play count and metadata for a given clip.

Database (PostgreSQL)
Use PostgreSQL to store:
Metadata of clips
Play count
Seed the DB with 5–6 clips using public domain or royalty-free MP3 URLs (you can use links from FreeSound, Pixabay, or GitHub-hosted files).

Monitoring (Grafana + Prometheus)
Track:
Number of total API requests
Number of streams (by clip ID)
Response latency (optional)
Use the starlette_exporter plugin for easy Prometheus integration with FastAPI, and display basic metrics on Grafana (demo via screenshot or in the Loom video is fine).


Deployment
Deploy your FastAPI app publicly using Render, Railway, or Vercel Serverless Functions (your choice).
API shouldn’t be accessible publicly.

Bonus (Optional)
Add a POST /play route to add a new clip entry (no file upload required — just metadata and a link).
Add a basic GitHub Actions workflow for linting, testing, and deploying (if you’re familiar).
 Tech Stack

FastAPI
PostgreSQL
Grafana + Prometheus
Deployed on Vercel / Render / Railway
(Optional: Terraform for infra setup — not required)

Evaluation Criteria
Working API with clean design and separation of concerns
Deployed service that’s publicly accessible
Play tracking and stream functionality works as expected
Use of PostgreSQL + basic schema
Code clarity and README documentation
Monitoring integration (even if locally shown)
Bonus for CI/CD and Terraform

Submission
Record a Loom video (max 5 mins) explaining:
What you built
How the code is structured
API demo (via browser or Postman)
Monitoring demo (screenshots or live)
Share your GitHub repository
Send both to sourabh@soundverse.ai with the subject:
"Backend Intern Assignment Submission - (Your Name)"

Notes
You can use public MP3 URLs or upload short clips to GitHub/CDN for the exercise.
Don’t hardcode secrets — use .env and pydantic for config.
Treat this like production-lite: clean code, modular structure, error handling.
You can use AI to accelerate your assignment. However, don’t use Lovable, Bolt, Cursor etc. Claude, Gemini and ChatGPT are permitted.

Good luck! 🚀 If you have questions, don’t hesitate to reach out.