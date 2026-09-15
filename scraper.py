import requests
from bs4 import BeautifulSoup
import pandas as pd
import os
import time

# Store scraped book information
book_data = []

# Scrape all 50 pages
for page in range(1, 51):

    if page == 1:
        page_url = "https://books.toscrape.com/"
    else:
        page_url = f"https://books.toscrape.com/catalogue/page-{page}.html"

    print(f"Scraping page {page}...")

    response = requests.get(
        page_url,
        headers={"User-Agent": "Mozilla/5.0"},
        timeout=60
    )

    soup = BeautifulSoup(response.text, "html.parser")

    books = soup.find_all("article", class_="product_pod")

    for book in books:
        title = book.h3.a["title"]
        price = book.find("p", class_="price_color").text
        availability = book.find(
            "p", class_="instock"
        ).get_text(" ", strip=True)
        rating = book.find(
            "p", class_="star-rating"
        )["class"][1]

        book_data.append({
            "Title": title,
            "Price": price,
            "Availability": availability,
            "Rating": rating
        })

    time.sleep(1)

print(f"Total books scraped: {len(book_data)}")

# Create DataFrame
df = pd.DataFrame(book_data)

# Clean price
df["Price"] = df["Price"].str.replace(
    r"[^\d.]", "", regex=True
).astype(float)

# Convert ratings from words to numbers
rating_map = {
    "One": 1,
    "Two": 2,
    "Three": 3,
    "Four": 4,
    "Five": 5
}

df["Rating"] = df["Rating"].map(rating_map)

# Create data folder inside the project
project_folder = os.path.dirname(os.path.abspath(__file__))
data_folder = os.path.join(project_folder, "data")

os.makedirs(data_folder, exist_ok=True)

# Save dataset
df.to_csv(
    os.path.join(data_folder, "books_dataset.csv"),
    index=False
)

print("Dataset saved successfully!")
