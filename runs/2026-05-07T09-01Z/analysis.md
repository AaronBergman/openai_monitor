# Bootstrap run — 2026-05-07T09-01Z

Fetch time (UTC): 2026-05-07T09:01:08.630082Z
Sitemap index: https://openai.com/sitemap.xml

This is the **bootstrap** run. There is no prior baseline, so every URL in
the sitemap is recorded as "first_seen" at this run_id. Subsequent daily runs
will diff against `sitemaps/openai.com/latest.xml` (the index) and the saved
sub-sitemaps under `sitemaps/openai.com/sub/latest/`.

## Stats

- Sub-sitemaps fetched: **34**
- Total URLs in sitemap: **1279**
- Pages successfully fetched + converted: **1277**
- Fetch failures: **2**

## Anomalies

None — bootstrap has no prior state to compare against. Anomaly detection
becomes active on the next run.

## Fetch failures

- `https://openai.com/index/inworld-ai-DO-NOT-PUBLISH/` — HTTPError: HTTP Error 404: 
- `https://openai.com/brand-old/` — HTTPError: HTTP Error 404: 
