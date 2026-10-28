"""Render a one-page service-business preview from a JSON data file onto kit-template.html.

Usage: python3 build_preview.py data.json out.html
The data file holds the facts pulled from public listings and the current site (a review may carry its own "source" when it is not from review_source); the copy fields
(headline, subhead, services_lead, why_lead, why items, area_lead) are written by Claude per business.
"""
import json, sys, html, re, os

HERE = os.path.dirname(os.path.abspath(__file__))

def esc(s):
    return html.escape(str(s), quote=True)

def render(d):
    t = open(os.path.join(HERE, 'kit-template.html')).read()
    first, _, second = d['name'].partition(' ')
    if not d.get('phone'):
        d['phone'] = 'your phone number here'
    digits = re.sub(r'\D', '', d['phone'])
    cards = ''.join(f'<div class="card"><h3>{esc(s["name"])}</h3><p>{esc(s["blurb"])}</p></div>' for s in d['services'])
    options = ''.join(f'<option>{esc(s["name"])}</option>' for s in d['services']) + '<option>Something else</option>'
    why = ''.join(f'<div><b>{esc(w["title"])}</b>{esc(w["text"])}</div>' for w in d['why'])
    reviews = ''.join(f'<div class="review"><div class="stars">&#9733;&#9733;&#9733;&#9733;&#9733;</div><p>&ldquo;{esc(r["text"])}&rdquo;</p><small>{esc(r["author"])}, {esc(r.get("source") or d.get("review_source", "Google"))} review, {esc(r["when"])}</small></div>' for r in d['reviews'])
    chips = ''.join(f'<span>{esc(a)}</span>' for a in d['areas'])
    hours = ''.join(f'<tr><td>{esc(day)}</td><td>{esc(hrs)}</td></tr>' for day, hrs in d['hours'])
    trust = []
    if d.get('rating'):
        trust.append(f'<div><b>{esc(d["rating"])} stars</b>{esc(d["review_count"])} {esc(d.get("review_source", "Google"))} reviews</div>')
    if d.get('years'):
        trust.append(f'<div><b>{esc(d["years"])}</b>years in {esc(d["area_short"])}</div>')
    if d.get('trust3_big'):
        trust.append(f'<div><b>{esc(d["trust3_big"])}</b>{esc(d.get("trust3_small", ""))}</div>')
    n = len(d['reviews'])
    reviews_lead = d.get('reviews_lead') or f'{d["rating"]} stars across {d["review_count"]} {d.get("review_source", "Google")} reviews. ' + ({1: 'One recent one:', 2: 'Two recent ones:', 3: 'Three recent ones:'}.get(n, 'Recent ones:'))
    fields = {
        'name': d['name'], 'short_name': d.get('short_name', first), 'tagline': d['tagline'],
        'meta_description': d['meta_description'], 'brand_color': d.get('brand_color', '#1f4e79'),
        'accent_color': d.get('accent_color', '#f5b921'), 'logo_first': first, 'logo_second': second,
        'phone': d['phone'], 'phone_digits': digits, 'headline': d['headline'], 'subhead': d['subhead'],
        'rating': d['rating'], 'review_count': d['review_count'], 'area_short': d['area_short'],
        'reviews_lead': reviews_lead, 'services_lead': d['services_lead'],
        'why_lead': d['why_lead'], 'area_lead': d['area_lead'], 'address': d['address'], 'email': d['email'],
        'year': d.get('year', '2026'), 'license_line': d.get('license_line', ''),
        'checkout_url': d.get('checkout_url', '#'), 'call_url': d.get('call_url', '#'),
        'form_endpoint': d.get('form_endpoint', '#'), 'brand': d.get('brand', 'Fixedfront'),
    }
    out = t
    for k, v in fields.items():
        out = out.replace('{{' + k + '}}', esc(v))
    for k, v in {'services_cards': cards, 'service_options': options, 'why_items': why,
                 'review_cards': reviews, 'area_chips': chips, 'hours_rows': hours, 'trust_items': ''.join(trust),
                 'email_line': (f'<p>Email: <a href="mailto:{esc(d["email"])}">{esc(d["email"])}</a></p>' if d.get('email') else '')}.items():
        out = out.replace('{{' + k + '}}', v)
    if not d['reviews']:
        out = re.sub(r'<section id="reviews">.*?</section>', '', out, flags=re.S)
        out = out.replace('<a href="#reviews">Reviews</a>', '')
    if not d['why']:
        out = re.sub(r'<section class="alt" id="why">.*?</section>', '', out, flags=re.S)
        out = out.replace('<a href="#why">Why us</a>', '')
    left = re.findall(r'{{\w+}}', out)
    assert not left, f'unfilled placeholders: {left}'
    return out

if __name__ == '__main__':
    data = json.load(open(sys.argv[1]))
    open(sys.argv[2], 'w').write(render(data))
    print('wrote', sys.argv[2])
