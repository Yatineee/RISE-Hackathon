import pandas as pd
import random
from datetime import datetime, timedelta

# Sample product
products = [
    {"product_id": "P001", "product_name": "Wireless Earbuds"},
    {"product_id": "P002", "product_name": "Bluetooth Speaker"},
    {"product_id": "P003", "product_name": "Smartwatch"},
    {"product_id": "P004", "product_name": "Phone Case"}
]

# Sample comment text (grouped by rating)
sample_reviews = {
    1: ["Battery problems again. I want a refund.",
        "Terrible experience. Will not buy again.",
        "Stopped working after one week."],
    2: ["Not comfortable in ears, and battery doesn’t last.",
        "Not worth the money.",
        "Poor build quality."],
    3: ["The sound is great, but the battery dies too fast.",
        "Just okay, nothing special.",
        "Average quality for the price."],
    4: ["Display is too dim in sunlight. Otherwise great features.",
        "Pretty good product.",
        "Decent for everyday use."],
    5: ["Loud and clear. Love the design!",
        "Excellent product! Highly recommend.",
        "Works perfectly. Will buy again."]
}


# Generate simulation data function
def generate_reviews(num_reviews=20, start_date="2024-06-01"):
    data = []
    base_date = datetime.strptime(start_date, "%Y-%m-%d")

    for i in range(num_reviews):
        review_id = 101 + i
        product = random.choice(products)
        rating = random.choices([1, 2, 3, 4, 5], weights=[0.1, 0.15, 0.25, 0.25, 0.25])[0]  # 偏向中高分
        review_text = random.choice(sample_reviews[rating])
        review_date = base_date + timedelta(days=random.randint(0, 14))

        data.append({
            "review_id": review_id,
            "product_id": product["product_id"],
            "product_name": product["product_name"],
            "review_text": review_text,
            "rating": rating,
            "review_date": review_date.strftime("%Y-%m-%d")
        })

    return pd.DataFrame(data)


# Generate and save as CSV
reviews_df = generate_reviews(30)
reviews_df.to_csv("reviews.csv", index=False)
print(reviews_df.head())
