class Restaurant:
    def __init__(self, name):
        self.name = name
        self.reviews = []

    def get_name(self):
        return self.name

    def add_review(self, review):
        self.reviews.append(review)

    def get_reviews(self):
        return self.reviews

    def get_customers(self):
        return list(set([review.customer for review in self.reviews]))

    def average_star_rating(self):
        if not self.reviews:
            return 0
        return sum([review.rating for review in self.reviews]) / len(self.reviews)