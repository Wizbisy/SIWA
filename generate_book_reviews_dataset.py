import pandas as pd
import random
from faker import Faker
import os
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Initialize Faker
fake = Faker('en_US')

# Parameters
num_samples = 10000
output_file = "book_reviews_dataset.csv"
genres = ["Fantasy", "Sci-Fi", "Mystery", "Romance", "Historical Fiction"]
ratings = [1, 2, 3, 4, 5]
# Pre-generate book titles to ensure they are static
book_titles = [
    f"The {fake.word().capitalize()} Saga",
    f"{fake.word().capitalize()} of the Stars",
    f"Echoes of {fake.word().capitalize()}",
    f"{fake.name()}'s Quest",
    f"The Last {fake.word().capitalize()}"
]
review_templates = {
    5: [
        "{book_title} is a breathtaking read! The writing by {author} is pure magic.",
        "Couldn’t put {book_title} down! A {genre} gem with vivid storytelling.",
        "Five stars for {book_title}! Absolutely enchanting and unforgettable.",
        "{book_title} is a must-read, beautifully crafted by {author}."
    ],
    4: [
        "{book_title} is engaging with a solid {genre} plot, highly enjoyable.",
        "Really liked {book_title}, {author} delivers a great story.",
        "{book_title} kept me hooked, though some parts felt slow.",
        "A strong {genre} book, {book_title} is worth checking out."
    ],
    3: [
        "{book_title} was decent, but the {genre} elements felt predictable.",
        "{author}’s {book_title} is okay, nothing extraordinary.",
        "{book_title} has good ideas but lacks a wow factor.",
        "Average read, {book_title} didn’t fully grip me."
    ],
    2: [
        "{book_title} was disappointing, the {genre} plot fell flat.",
        "Struggled with {book_title}, {author}’s style didn’t click.",
        "{book_title} had potential but felt poorly executed.",
        "Not a fan of {book_title}, too many dull moments."
    ],
    1: [
        "{book_title} was a letdown, {genre} clichés throughout.",
        "Couldn’t finish {book_title}, {author}’s writing was weak.",
        "{book_title} is forgettable, a waste of time.",
        "Terrible read, {book_title} missed the mark completely."
    ]
}

def generate_dataset():
    try:
        logging.info(f"Generating dataset with {num_samples} samples...")
        data = {
            "id": [],
            "book_title": [],
            "review_text": [],
            "rating": [],
            "genre": [],
            "reviewer_name": []
        }

        for i in range(num_samples):
            rating = random.choice(ratings)
            genre = random.choice(genres)
            book_title = random.choice(book_titles)
            reviewer_name = fake.name()
            author_name = fake.name()  # Generate author name separately
            review_text = random.choice(review_templates[rating]).format(
                book_title=book_title,
                genre=genre,
                author=author_name
            )

            data["id"].append(i + 1)
            data["book_title"].append(book_title)
            data["review_text"].append(review_text)
            data["rating"].append(rating)
            data["genre"].append(genre)
            data["reviewer_name"].append(reviewer_name)

        # Save to CSV
        df = pd.DataFrame(data)
        df.to_csv(output_file, index=False)
        logging.info(f"Dataset saved to {os.path.abspath(output_file)}")
    except Exception as e:
        logging.error(f"Error generating dataset: {str(e)}")
        raise

if __name__ == "__main__":
    generate_dataset()