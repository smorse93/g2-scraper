# G2 Scraper

![G2 Scraper CSV Result](https://raw.githubusercontent.com/omkarcloud/g2-scraper/master/img/example_result.png)

This is a Python script that allows you to scrape product information from G2. The script first gets the product links and then scrape the products.

## Installation

1. Clone Starter Template
```
git clone https://github.com/omkarcloud/g2-scraper
cd g2-scraper
```
2. Install dependencies
```
python -m pip install -r requirements.txt
```

## Usage

### Step 1: Extract Product Links

- Run Project
```
python main.py
```

### Step 2: Extract Product

- Open config.py and paste 
```python
from .extract_product_links import ExtractProductLinks
from .extract_products import ExtractProducts

tasks_to_be_run = [
        # ExtractProductLinks,
        ExtractProducts
]
```

- Run Project
```
python main.py
```
**The products will be extracted and stored in the output/finished.csv and output/finished.json file after scraping.**

![G2 Scraper CSV Result](https://raw.githubusercontent.com/omkarcloud/g2-scraper/master/img/example_result.png)

## Thanks

The G2 Scraper project uses the Bose Framework, a web scraping framework that is Swiss Army Knife for web scraping. I encourage you to learn about Bose Framework at [https://www.omkar.cloud/bose/](https://www.omkar.cloud/bose/)