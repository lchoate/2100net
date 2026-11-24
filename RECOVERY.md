# Wayback recovery report

Inspected September 21, 2026 (Arizona time).

## Snapshot selection

The Wayback calendar reported **25 homepage captures** from May 16, 2014 to September 16, 2026. The prefix URL inventory reported **448 captured URLs**. These counts are archive entries, not counts of complete website versions. Several images have separate crawl dates, so even one replay can combine different capture times.

| Capture | Observations | Decision |
| --- | --- | --- |
| [2014-05-16 21:00:25 homepage](https://web.archive.org/web/20140516210025/http://2100net.org/) | Welcome, nightly 9 PM MST, three-person operator rotation, Rimlink frequencies, links to chat/audio/photos/resources/history and Sunday coffee. Footer says updated April 1, 2014 and credits Daddy Cool. One banner initially failed. | Early historical baseline. |
| [2014-06-29 20:27:35 gallery](https://web.archive.org/web/20140629202735/http://2100net.org/pictures.html) | Readable member captions and many retrievable thumbnails. Requests could historically add/change/remove a picture. | Recover 19 thumbnails and their captions. |
| [2014-06-29 10:24:29 history](https://web.archive.org/web/20140629102429/http://2100net.org/history.html) | W5ORV commentary about 73/73’s and an old 1AW QSL card; ARRL origins article credited to Wikipedia. | Preserve the topics and source link; do not pass personal commentary off as current authoritative guidance or reproduce the long borrowed article. |
| [2014-06-29 13:27:42 links](https://web.archive.org/web/20140629132742/http://2100net.org/links.html) | ARRL, FCC, QRZ, repeater directories, retailers, equipment makers and other ham links. | Retain useful categories; replace the long commercial directory with a concise organization directory. |
| [2018-12-26 22:38:57 homepage](https://web.archive.org/web/20181226223857/http://2100net.org/) | Later roster, volunteering guidance, operator script and social gallery links; footer says September 12, 2018. Mount Ord background available. | Best of the inspected homepages for the rebuild: richer content and useful image, with the 2014 version preserving earlier history. |
| [2018-09-03 12:48:07 script](https://web.archive.org/web/20180903124807/http://www.2100net.org:80/script.html) | Preamble, priority-traffic check, regular roll call, visitors, second round and closing. Page says updated June 5, 2016. Old checkboxes, participant list and operator qualifications are present. | Use the format to explain joining; link original for historical operator guidance. Do not turn the old station list into current accounts or assignments. |
| [2018-09-03 12:49:01 social page](https://web.archive.org/web/20180903124901/http://2100net.org/being_social.html) | 2014–2016 hamfests, Payson gathering, Tempe coffee, station/antenna projects, June 2015 Field Day at Arizona Science Center C.A.R.L. | Preserve a dated summary and recover two representative photographs. |
| [2026-09-16 17:52:41 homepage](https://web.archive.org/web/20260916175241/2100net.org) | Replay redirected to an unrelated travelideaz.com/lander capture, which was unavailable. | Exclude as a community source. |

September 2018 URLs for history, links, photos and streaming were also identified through the archive index. Not all 25 homepage captures or 448 URLs were inspected or downloaded. “Best” here means the most useful inspected combination; this is a targeted reconstruction, not an exhaustive mirror.

## Recovered content

- Social, welcoming purpose; listed nightly schedule; ARA/Rimlink relationship.
- Original navigation concepts: home, photos, chat, streaming, ham links, history, events, contact; later operator script and social gatherings.
- 2014 roster: Joe AE7JG Monday/Wednesday; Dale N7OXF Thursday/Sunday; Bill W1VBG Tuesday/Friday; rotating Saturday.
- 2018 roster: Joe AE7JG Tuesday; Jason KG7VLF Friday; other days labeled open.
- Eight repeater entries from the 2018 page, kept behind an explicitly historical disclosure. The 2014 page additionally listed Greens Peak 448.375− / 100.0 and 927.1625− / 151.4; it did not list Mingus Mountain. These differences are a reason not to treat either list as current.
- Net procedure: priority-traffic check, roll call, calls for visitors/late/missed, second round, closing acknowledgment.
- Historical photographs and community-event captions.
- Historic contact links were found, but the owner needs new contact information. They are not promoted as current or wired into mail buttons.

## Recovered images

**24 local image files:** 19 member thumbnails, two banner GIFs, Mount Ord photograph, Payson gathering thumbnail and Field Day thumbnail. All successful originals are preserved in `dist/assets/archive/`, including unused banner GIFs. `recovery/assets.json` maps local names to exact attempted replay URLs. Wayback may have served the closest available binary capture.

From the original gallery, 27 assets were attempted and 21 succeeded. Failures: `mtord1t.jpg`, `N7BBStt.jpg`, `w7adot.jpg`, `W1VBGtt.jpg`, `wx7jemt.jpg`, and `logo_icon2.ico`. Responses were missing or invalid image content. Failed files were not embedded as broken images. Mount Ord and two later social thumbnails were recovered separately.

The 19 recovered gallery captions are preserved as originally displayed, including cases where filenames use an older call sign (`kg7gtht.jpg` labeled WB4CVO; `Kg7elrt.jpg` labeled W7DGL). They have not been independently matched to present call-sign holders. Original photographer credits were not supplied on those pages. Images are archival material, not newly licensed stock art.

## Rebuild changes

- Nine coherent pages, shared navigation, mobile menu with expanded state, keyboard Escape handling and skip link.
- Responsive layout, semantic headings/tables, readable contrast, focus indicators, image descriptions, reduced interface clutter, no marquee or antique plugin embeds.
- Recovered Mount Ord photograph anchors the design; deep blue-green and bright lime distinguish the new interface from the original table markup.
- Direct, plain-language joining steps; historical schedules/frequencies/rosters clearly separated from current references.
- Current resources checked: [ARA](https://www.w7ara.org/), [ARA repeaters](https://www.w7ara.org/z/Repeaters.aspx), [ARRL](https://www.arrl.org/), [QRZ](https://www.qrz.com/), [ARCA](https://arca-az.org/). [Kachina ARC](https://kachinaarc.org/nets/) also lists the nightly 9 PM MST net, but no source here verifies tonight’s actual operation.
- No old chat/audio endpoints reactivated; no invented email addresses, members, live status, or submission confirmations.
- Removed active use of historical linking/unlinking repeater codes, stale service/repair contacts and old commercial links.

## Remaining limits

Current operators, current email and public logging-app address need confirmation. No community message board or persistent online messaging was implemented without a real administrator/contact destination. On-air guidance and links to current community resources provide the usable contact path now. The static front end is ready to connect to the existing logging project via verified public URLs.

The core archive pages and representative imagery were recovered; this is not a complete offline copy of every historical page, full-resolution photo, media stream, embedded video or check-in record.
