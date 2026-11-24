# 2100 Net community website

A standalone, dependency-free website reconstructed from inspected Wayback Machine captures. The complete working site is in `dist/`; it can be opened directly in a browser or served by any static web server. No package installation is required.

## Run and edit

From this directory:

```sh
python3 build.py
python3 -m http.server 4173 --bind 127.0.0.1 --directory dist
```

Open http://127.0.0.1:4173/. Edit page content and shared navigation in `build.py`, presentation in `dist/styles.css`, and the small progressive enhancements in `dist/site.js`. Re-run the build after content/configuration changes. Styles, scripts and recovered assets are intentionally authored in `dist/` and are not deleted by the build.

The nine pages cover Home, About, Schedule/Join, Operators, Community/Contact, History, Photo Gallery, Resources and Recovery Notes. Navigation and content remain usable without JavaScript. JavaScript adds a collapsible mobile menu and an Arizona clock; the clock is not a live-net indicator.

## Current information still needed

The owner confirmed that new contact information must be obtained. Current operator assignments, tonight’s actual net operation, online chat/audio services, and the public logging-app URL have not been verified. The site does not invent them. Current repeater guidance links to ARA; the 2018 frequencies are a labeled historical disclosure.

In `site-config.json`, replace `null` with a verified `contactEmail` and/or HTTPS `logBaseUrl`, then rebuild. The optional logging URL creates links to `/public/nets`, `/public/nets?scope=all` and `/nets`. Leave these values null until confirmed. No emails are sent by the website; a configured email becomes a mail link. There is no simulated chat, contact submission, member registration or database.

## 2100NetLog integration decision

Inspected `/Users/lucas/websites/2100netlog`: Laravel 13, PHP 8.3, Livewire 4, Fortify authentication. Its existing public controller supplies server-rendered net listings and detail pages. Public listings exclude drafts and archived sessions and show checked-in participants; protected routes handle net control, station editing, roll call, second round, trivia and printing.

A separate static community front end is appropriate now: it can have its own public lifecycle while the logging app retains its authentication and existing workflows. Its working tree already had modifications, which were left untouched. No database, `.env`, credentials, private station records or user accounts were copied.

Use links to the app’s public pages first. Do not scrape protected pages or expose the station database. If live cards or shared accounts are later needed, add a deliberately scoped, read-only API and review public fields within the Laravel project. The current project does not have that API or cross-site sign-in integration.

## Recovery and attribution

Read `RECOVERY.md` for snapshot selection, source URLs, changes and known gaps. `recovery/assets.json` records every recovered image’s source URL and local path. Original image filenames and binary content are preserved. Photo labels reflect the archive, not present membership. Rights remain with their original owners; no new image license is asserted.

## Validation

```sh
python3 validate.py
node --check dist/site.js
```

The structural check validates local links and anchors, asset references, unique page titles, one main heading per page, and nonempty image alternative text. Browser checks covered the narrow layout, menu toggle and Escape behavior, the frequency disclosure, and image loading. This is not a full accessibility audit.

## Hosting

A private Sites project is registered in `.openai/hosting.json`. These files also work independently of Sites: serve `dist/` from any static host. Reuse the recorded project identity for future Sites publishing. The community site does not deploy the separate Laravel application or change 2100net.org DNS.

Private preview publication was not completed: automatic approval review rejected the external repository upload pending explicit approval. The project remains local.
