# deductback.com: go-live steps (about 25 minutes, in this order)

Everything in this folder is ready to serve as-is. Do the steps in order; nothing needs editing unless you want to change copy.

## 1. Create the repo (3 min)
1. Sign in to github.com as **fixedfront** (the account that already hosts fixedfront.com; 2FA is on).
2. New repository → name `deductback-site` → **Public** → no README → Create.
3. Add file → **Upload files** → click "choose your files" (don't drag) → select ALL files in this folder, including `.nojekyll` and `CNAME` → Commit changes.
   - Check the file list after the commit shows: 404.html, CNAME, contact.html, favicon.svg, index.html, privacy.html, robots.txt, scan.html, sitemap.xml, terms.html, thanks.html, .nojekyll (and this README, harmless).

## 2. Turn on Pages (2 min)
1. Repo → Settings → Pages → Source: **Deploy from a branch** → Branch **main**, folder **/(root)** → Save.
2. Wait ~1 minute; the page shows "Your site is live at https://fixedfront.github.io/deductback-site/". Open it: the home page should render (links will work fully once the domain is on).
3. Custom domain: type `deductback.com` → Save. (The CNAME file already matches, so GitHub won't rewrite it.)

## 3. Point the domain (5 min, then wait)
At the registrar where deductback.com's DNS lives (the same place the Google Workspace MX records were set in September):
1. Add four **A** records, host `@`:
   `185.199.108.153`, `185.199.109.153`, `185.199.110.153`, `185.199.111.153`
2. Add a **CNAME** record, host `www`, value `fixedfront.github.io`
3. Delete any existing A or AAAA record on `@` and any CNAME on `www` that pointed at a parking page. **Do not touch** MX, TXT (SPF, DKIM, DMARC, google-site-verification) or the `_dmarc` record; email keeps working untouched.
4. Back in GitHub Settings → Pages, click "Check again" under the custom domain. It can take 15 minutes to a few hours for the check to go green (fixedfront.com took overnight). When it's green, tick **Enforce HTTPS**.

Reply "deductback dns done" in chat and I verify https://deductback.com/, /scan.html, /contact.html and the www redirect.

## 4. Activate the contact form (2 min, after the site is live)
The form on contact.html relays through formsubmit.co to zeluis@deductback.com. The FIRST submission triggers a one-time email from FormSubmit to zeluis@deductback.com with an "Activate" button. Submit the form once yourself from https://deductback.com/contact.html, click Activate in that email, then submit once more to confirm it arrives. Until that click, submissions are held, not lost.

## 5. Update the places that point at Deductback (5 min)
- Stripe (Deductback account acct_1UIqfmFtDVRcxeWZ) → Settings → Business details → Website: `https://deductback.com` (replaces the Calendly link used on 30 Oct).
- Gmail signature for zeluis@deductback.com: add `deductback.com` under the name line (plain text).
- Calendly event "Scan": set the event's description link to https://deductback.com/scan.html (optional).
- Future outreach emails: the Sales-kit signature can carry `deductback.com`; the morning brief's drafts will add it once you say "site live".

## What's in the site
- `index.html` home: offer, the problem, how it works, what we recover, sample scan (Northline Foods, illustrative), pricing (25%), who it's for, FAQ, CTA.
- `scan.html` the free scan: what to send (Target Partners Online, Walmart APDP), what comes back, how lines are rated, next steps.
- `contact.html` form + email + Calendly + mailing address + partner line; `thanks.html` after a submission (noindex).
- `terms.html` website terms (free scan is no-obligation; paid work governed by the Services Agreement); `privacy.html` (no cookies, no tracking; FormSubmit, Google, Calendly, Stripe, GitHub listed as processors). **Both are drafts for McInerny to read alongside the agreement**; they publish now with "Last updated 6 November 2026".
- `404.html`, `favicon.svg`, `robots.txt` (allow all, hide thanks.html), `sitemap.xml`, `CNAME`, `.nojekyll`.
- No analytics script. If you want Cloudflare Web Analytics like Fixedfront, add deductback.com in that dashboard and paste the token in chat; I add the one-line beacon to every page.

## Privacy checks already applied
First name only ("Zeluis, founder" appears once, in the FAQ). No employer, no surname, no phone number on the site. Mailing address is the Columbia iPostal1 box. The entity is described as "a Maryland business, currently operated as a sole proprietorship; an LLC is being formed" (same wording as fixedfront.com) — update both sites when the LLC is filed.

## Editing later
Source: `build.py` (kept in the project as claude/deductback-site-build.py). Change the copy there, run `python3 build.py`, upload the changed .html files. Or just tell me what to change in chat and I regenerate the files.
