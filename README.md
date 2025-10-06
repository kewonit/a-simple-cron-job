# a-simple-cron-job

This repository contains a simple cron job implemented using GitHub Actions that periodically pings a specified URL and stores the results in JSON and HTML formats. The HTML output is designed to be served via a simple HTMX-based site.

## Features

- Scheduled ping via GitHub Actions (cron schedule)
- Stores ping history as JSON in `data/site_data.json`
- Generates an HTML table in `data/site_data.html`
- HTMX front-end to display results dynamically

## Setup

- The ping URL is now hardcoded in `scripts/ping_site.py`. To change the URL, edit the `URL` variable.
- The GitHub Actions workflow runs on every commit (push) to any branch, and daily via cron.
- HTMX front-end in `index.html` fetches JSON data from a raw GitHub URL by default:
  `https://raw.githubusercontent.com/kewonit/a-simple-cron-job/refs/heads/main/data/site_data.json`
  You can replace this URL in `index.html` to point at your own repository or branch.

## Usage

- The action will automatically run on the defined schedule and commit updated data back to the main branch.
- To view results, serve the repository root via any static site server (e.g., `python -m http.server`) and open `index.html`.

## HTMX Frontend

The `index.html` in the repo root now fetches the raw JSON data via HTMX from a GitHub raw URL and auto-refreshes every minute. It parses the JSON and renders it into a styled HTML table displaying timestamps, status codes, and response times.
You can customize the raw JSON URL in `index.html` to point to your own repository or branch.
