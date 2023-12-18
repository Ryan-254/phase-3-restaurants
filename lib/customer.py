from review import Review
class Customer:
    all_customers = []

    def __init__(self, given_name, family_name):
        self.given_name = given_name
        self.family_name = family_name
        Customer.all_customers.append(self)

    def change_given_name(self, given_name):
        self.given_name = given_name

    def change_family_name(self, family_name):
        self.family_name = family_name

    def full_name(self):
        return f"{self.given_name} {self.family_name}"

    @classmethod
    def all(cls):
        return cls.all_customers
    
    def restaurants(self):
        return list(set([review.restaurant for review in Review.all() if review.customer == self]))

    def add_review(self, restaurant, rating):
        review = Review(self, restaurant, rating)
        restaurant.add_review(review)

    def num_reviews(self):
        return len([review for review in Review.all() if review.customer == self])

    @classmethod
    def find_by_name(cls, name):
        for customer in cls.all_customers:
            if customer.full_name() == name:
                return customer
        return None

    @classmethod
    def find_all_by_given_name(cls, name):
        return [customer for customer in cls.all_customers if customer.given_name == name]