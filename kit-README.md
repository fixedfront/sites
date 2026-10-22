# Fixedfront preview kit (flat layout)

- kit-build_preview.py + kit-template.html: the generator. Usage: python3 kit-build_preview.py data-<slug>.json p-<slug>.html
- data-<slug>.json: one file per business (facts from public listings only; nothing invented).
- p-<slug>.html: the built preview pages, served at https://fixedfront.github.io/sites/p-<slug>.html
- robots.txt disallows all crawling; .nojekyll keeps GitHub Pages from processing the files.
- kit-log.md: one line per deploy run.
To add a business: add data-<slug>.json, run the generator, commit p-<slug>.html.
