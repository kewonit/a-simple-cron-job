# a-simple-cron-job

This repository contains a simple cron job implemented using GitHub Actions that periodically pings a specified URL and stores the results in JSON and HTML formats. The HTML output is designed to be served via a simple HTMX-based site.

## Features

- Scheduled ping via GitHub Actions (cron schedule)
- Stores ping history as JSON in `data/site_data.json`
- Generates an HTML table in `data/site_data.html`
- HTMX front-end to display results dynamically

## Setup

1. Add your URL as a repository secret named `PING_URL`.
2. Adjust the schedule in `.github/workflows/ping_site.yml` as needed.

## Usage

- The action will automatically run on the defined schedule and commit updated data back to the main branch.
- To view results, serve the repository root via any static site server (e.g., `python -m http.server`) and open `index.html`.

## HTMX Frontend

The `index.html` in the repo root loads `data/site_data.html` via HTMX and auto-refreshes every minute. It includes a styled table for displaying timestamps, status codes, and response times.
