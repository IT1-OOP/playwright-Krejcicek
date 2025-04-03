import os
from playwright.sync_api import sync_playwright,expect
import urllib.parse

def test_pabe_title():
    cesta = os.path.abspath("index.html")  # Získání absolutní cesty k souboru
    cesta = urllib.parse.unquote(cesta) 

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto(f"file:///{cesta}")
        nadpis_1 = page.locator("h1").first
        expect(nadpis_1).to_be_visible()
        browser.close()



