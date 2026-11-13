# Fixedfront preview kit (flat layout)

- kit-build_preview.py + kit-template.html: the generator. Usage: python3 kit-build_preview.py data-<slug>.json p-<slug>.html
- data-<slug>.json: one file per business (facts from public listings only; nothing invented).
- p-<slug>.html: the built preview pages, served at https://fixedfront.github.io/sites/p-<slug>.html
- robots.txt disallows all crawling; .nojekyll keeps GitHub Pages from processing the files.
- kit-log.md: one line per deploy run.
To add a business: add data-<slug>.json, run the generator, commit p-<slug>.html.

## Buy button (28 Oct 2026)
"Make it mine" on every preview goes to the Fixedfront Stripe Payment Link ($795 setup + $49/month, PAYMENT_LINK in kit-build_preview.py) with `client_reference_id=<slug>` so the Stripe payment shows which business bought. A data file's checkout_url is used only if it is an explicit https:// URL; "#checkout", "#", a mailto: or a missing key all mean "use the Payment Link". Set checkout_url to "none" to keep a mailto button (A1 Pool Service, founding-client offer).

## Review captions
A review object may set "source" ("HomeGuide", "Company site", "Experience.com", "Google", "Yelp", "Birdeye"). That is the caption. With no "source", the page review_source is used, which is what the star rating refers to. A blank "when" is omitted, so the caption does not end with a comma. Existing data files with a date and no per-review source render the same caption as before.

## Blank address, service area, and trust stats
A blank address is omitted from the contact block and the footer. If both areas and area_lead are blank, the "Where we work" section is omitted. A blank area_short makes the why heading "Why customers call {short_name}". A place name stays "Why {area_short} calls {short_name}". A blank years value and a blank third trust fact are omitted, so an empty trust stat is not shown. trust3_big / trust3_small may be one string pair. A three-item list uses only a non-empty third item, because the rating chip already shows the rating and the review count.

## Price change (9 Nov 2026)
Price is now $795 setup + $49/month. The $990 + $149 Payment Link is retired. New Payment Link (11 Nov 2026): https://buy.stripe.com/9B69ATfnXdFz0HZ3Fg5Vu00 — wired into PAYMENT_LINK; A1 keeps its mailto (checkout_url "none").
