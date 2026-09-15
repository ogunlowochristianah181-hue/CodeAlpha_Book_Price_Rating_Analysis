import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os


df = pd.read_csv("Web_Scraping_EDA_Project/data/books_dataset.csv")

print("Dataset loaded successfully!")
print(df.head())

print("\nDataset shape:")
print(df.shape)


print("\nColumn names:")
print(df.columns)

print("\nData types:")
print(df.dtypes)

print("\nMissing values:")
print(df.isnull().sum())

print("\nSummary statistics:")
print(df.describe())

print("\nEDA Questions:")
print("1. What is the distribution of book prices?")
print("2. What is the distribution of book ratings?")
print("3. Is there a relationship between book price and rating?")
print("4. How many books fall into each rating category?")


print("\nPrice range:")
print(df["Price"].min(), "to", df["Price"].max())

print("\nAverage price:")
print(df["Price"].mean())

os.makedirs("Web_Scraping_EDA_Project/images", exist_ok=True)

# price Distribution
plt.figure(figsize=(10, 6))
sns.histplot(df["Price"], bins=20)
plt.title("Distribution of Book Prices")
plt.xlabel("Price (£)")
plt.ylabel("Number of Books")
plt.tight_layout()
plt.savefig("Web_Scraping_EDA_Project/images/price_distribution.png",
            dpi=300, bbox_inches="tight")
plt.show()


# Rating distribution
plt.figure(figsize=(8, 5))
sns.countplot(x="Rating", data=df)
plt.title("Distribution of Book Ratings")
plt.xlabel("Rating")
plt.ylabel("Number of Books")
plt.tight_layout()
plt.savefig("Web_Scraping_EDA_Project/images/rating_distribution.png",
            dpi=300, bbox_inches="tight")
plt.show()


# Relationship between Price and Rating
plt.figure(figsize=(8, 5))
sns.scatterplot(x="Price", y="Rating", data=df)
plt.title("Relationship Between Book Price and Rating")
plt.xlabel("Price (£)")
plt.ylabel("Rating")
plt.tight_layout()
plt.savefig("Web_Scraping_EDA_Project/images/price_vs_rating.png",
            dpi=300, bbox_inches="tight")
plt.show()


print("\nNumber of Books by Rating:")
print(df["Rating"].value_counts().sort_index)

print("\nCorrelation between Price and Rating:")
print(df["Price"].corr(df["Rating"]))


# most expensive and most cheapest
print("\nMost Expensive Books:")
print(df.nlargest(5, "Price")[["Title", "Price", "Rating"]])

print("\nCheapest Books:")
print(df.nsmallest(5, "Price")[["Title", "Price", "Rating"]])


# Availability data
print("\nAvailability Counts:")
print(df["Availability"].value_counts())


# percentage of books
print("\nRating Percentages:")
print((df["Rating"].value_counts(normalize=True).sort_index() * 100).round(1))
