<p align="center">
  <img src="https://www.omkar.cloud/images/favicon/prod/favicon-256x256.png" alt="omkar" />
</p>
  <div align="center" style="margin-top: 0;">
  <h1>✨ G2 Scraper 🤖</h1>
  <p>💦 Enjoy the Rain of G2 Products from G2 Categories 💦</p>
</div>
<em>
  <h5 align="center">(Programming Language - Python 3)</h5>
</em>
<p align="center">
  <a href="#">
    <img alt="g2-scraper forks" src="https://img.shields.io/github/forks/omkarcloud/g2-scraper?style=for-the-badge" />
  </a>
  <a href="#">
    <img alt="Repo stars" src="https://img.shields.io/github/stars/omkarcloud/g2-scraper?style=for-the-badge&color=yellow" />
  </a>
  <a href="#">
    <img alt="g2-scraper License" src="https://img.shields.io/github/license/omkarcloud/g2-scraper?color=orange&style=for-the-badge" />
  </a>
  <a href="https://github.com/omkarcloud/g2-scraper/issues">
    <img alt="issues" src="https://img.shields.io/github/issues/omkarcloud/g2-scraper?color=purple&style=for-the-badge" />
  </a>
</p>
<p align="center">
  <img src="https://views.whatilearened.today/views/github/omkarcloud/g2-scraper.svg" width="80px" height="28px" alt="View" />
</p>

---

<!-- # G2 Scraper -->

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
<!--
**The products will be extracted and stored in the output/finished.csv and output/finished.json file after scraping.**
-->

*PS: I have the entire G2 dataset available for purchase, priced at $400. For those seeking a more affordable option, a partial dataset is also available at a discounted price. Feel free to reach out to chetan@omkar.cloud to request a sample.*



<!-- *PS: You may also contact us at chetan@omkar.cloud to request a G2 Product Reviews Scraper to enhance your Lead generation Efforts.*

I have full Dataset of g2 available for sale for $400. Partial Dataset is also available at a lower cost. Contact chetan@omkar.cloud to request sample. -->

![G2 Scraper CSV Result](https://raw.githubusercontent.com/omkarcloud/g2-scraper/master/img/example_result.png)

## Thanks

The G2 Scraper project uses the Bose Framework, a web scraping framework that is Swiss Army Knife for web scraping. I encourage you to learn about Bose Framework at [https://www.omkar.cloud/bose/](https://www.omkar.cloud/bose/)
