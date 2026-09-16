# Book Price & Rating Analysis Using Web Scraping and Python

## Project Overview

This project was completed as part of my CodeAlpha Data Analytics Internship.

The project focuses on collecting book information from a public website using web scraping and then analyzing and visualizing the collected data using Python.

I scraped data from Books to Scrape and collected information on 1,000 books, including their titles, prices, availability, and ratings.

The project covers three areas:

- Web Scraping
- Exploratory Data Analysis (EDA)
- Data Visualization

## Objectives

The main objectives of this project were to:

- Collect a custom dataset from a public website using Python.
- Clean and prepare the scraped data for analysis.
- Explore the structure and characteristics of the dataset.
- Identify patterns in book prices and ratings.
- Examine the relationship between book price and rating.
- Create visualizations to communicate the findings.

## Data Source

**Books to Scrape:**  
https://books.toscrape.com/

Books to Scrape is a demo website designed for practicing web scraping.

The website states that its prices and ratings are randomly assigned and have no real-world meaning. Therefore, the findings in this project should be interpreted as observations from a demonstration dataset.

## Tools and Technologies

- Python
- Requests
- BeautifulSoup
- Pandas
- Matplotlib
- Seaborn
- VS Code

## Dataset

The final dataset contains **1,000 books** and four variables:

| Column       | Description                                            |
| ------------ | ------------------------------------------------------ |
| Title        | Name of the book                                       |
| Price        | Book price in pounds (£)                               |
| Availability | Stock availability                                     |
| Rating       | Book rating converted to a numerical scale from 1 to 5 |

## Web Scraping

The website contains 50 pages with 20 books per page.

Python's `Requests` library was used to retrieve the web pages, while `BeautifulSoup` was used to extract the required information from the HTML structure.

The scraper collected:

- Book title
- Price
- Availability
- Rating

The collected data was stored in a Pandas DataFrame and exported as a CSV file.

## Exploratory Data Analysis

The analysis examined:

- Dataset dimensions
- Column names
- Data types
- Missing values
- Summary statistics
- Price range
- Average price
- Rating distribution
- Availability
- Relationship between price and rating

### Questions Explored

1. What is the distribution of book prices?
2. What is the distribution of book ratings?
3. Is there a relationship between book price and rating?
4. How many books fall into each rating category?

## Key Findings

### Price

- Number of books: **1,000**
- Average price: **£35.07**
- Median price: **£35.98**
- Minimum price: **£10.00**
- Maximum price: **£59.99**

### Ratings

The average rating was approximately **2.92 out of 5**.

| Rating | Number of Books | Percentage |
| ------ | --------------: | ---------: |
| 1      |             226 |      22.6% |
| 2      |             196 |      19.6% |
| 3      |             203 |      20.3% |
| 4      |             179 |      17.9% |
| 5      |             196 |      19.6% |

### Price and Rating Relationship

The correlation between price and rating was approximately **0.028**, indicating a very weak linear relationship between the two variables in this dataset.

Because the website's prices and ratings are randomly assigned, this result should not be interpreted as evidence about real-world book pricing or reader preferences.

### Availability

All 1,000 books in the dataset were listed as **in stock**.

## Data Visualizations

### 1. Book Price Distribution

[Book Price Distribution](images/price_distribution.png)

### 2. Book Rating Distribution

[Book Rating Distribution](images/rating_distribution.png)

### 3. Price vs Rating

[Price vs Rating](images/price_vs_rating.png)

## Project Structure

```text
CodeAlpha_Book_Price_Rating_Analysis/
│
├── data/
│   └── books_dataset.csv
│
├── images/
│   ├── price_distribution.png
│   ├── rating_distribution.png
│   └── price_vs_rating.png
│
├── notebooks/
│   └── analysis.ipynb
│
├── scraper.py
├── analysis.py
├── README.md
└── requirements.txt
```

### How to Run the Project

### Install the required libraries

pip install -r requirements.txt

### Run the web scraper

python scraper.py

### Run the analysis

python analysis.py

### Conclusion

## Conclusion

This project demonstrates how Python can be used to collect, clean, analyze, and visualize data from a website.

Through this project, I gained practical experience in web scraping, data preparation, exploratory data analysis, correlation analysis, and data visualization. The project also strengthened my ability to turn raw web data into meaningful insights and communicate findings through visualizations.

Because the Books to Scrape website uses randomly assigned prices and ratings, the findings are intended for demonstration and learning purposes rather than real-world market conclusions.

### Internship

CodeAlpha Data Analytics Internship

### Tasks Completed

Task 1 — Web Scraping
Task 2 — Exploratory Data Analysis
Task 3 — Data Visualization
