import json

def parse_json(file_path):
    # Load JSON data from a file
    with open(file_path, 'r') as f:
        data = json.load(f)

    # Extract required fields for each review
    reviews = []
    for product in data:
        product_name = product.get('product_name')
        g2_link = product.get('g2_link')
        for review in product.get('initial_reviews', []):
            review_id = review.get('review_id')
            review_title = review.get('review_title')
            review_content = review.get('review_content')
            publish_date = review.get('publish_date')
            reviewer = review.get('reviewer', {})
            reviewer_name = reviewer.get('reviewer_name')
            reviews.append({
                'Product Name': product_name,
                'G2 Link': g2_link,
                'Review ID': review_id,
                'Review Title': review_title,
                'Review Content': review_content,
                'Publish Date': publish_date,
                'Author': reviewer_name,
            })

    return reviews

# Replace this with your actual file path
file_path = "/Users/stevenmorse33/Documents/CodingProjects/G2Scraper/output/_all/json/_all.json"
reviews = parse_json(file_path)

# Write data to JSON file
with open('reviews_cleaned_CDW_Comp.json', 'w') as f:
    json.dump(reviews, f)