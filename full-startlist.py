# get full starting list from running race webpage

import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

base_url = ("https://trackmaxx.ch/entrylist/"
            "?race=brl26"
            "&c=32e13bee-2c3d-40f6-ac1c-5ce4d6898493"
            "&p={page}")

all_rows = []
maxpages = 29
for page in range(1, maxpages + 1):  # pages 1 through 29
    print(f"Fetching page {page} …")
    url = base_url.format(page=page)
    resp = requests.get(url)
    resp.raise_for_status()
    soup = BeautifulSoup(resp.text, "html.parser")

    # find the table. Here it looks like each row is within the table after the heading "## Marathon Männer"
    table = soup.find("h2", string="10km Running Männer")
    if not table:
        print("Unexpected page structure on page", page)
        continue
    table = table.find_next("table")
    if not table:
        print("No table found on page", page)
        continue

    # parse headings from the table header
    headers = [th.get_text(strip=True) for th in table.find("thead").find_all("th")]

    for tr in table.tbody.find_all("tr"):
        cols = [td.get_text(strip=True) for td in tr.find_all("td")]
        if not cols:
            continue
        row = dict(zip(headers, cols))
        all_rows.append(row)

    time.sleep(0.5)  # polite pause

df = pd.DataFrame(all_rows)
print("Total rows scraped:", len(df))

# Save to Excel
df.to_excel("bremgarten10k_entries.xlsx", index=False)
print("Saved to bremgarten10k_entries.xlsx")

# Save to CSV
df.to_csv("bremgarten10k_entries.csv", index=False)
print("Saved to bremgarten10k_entries.csv")