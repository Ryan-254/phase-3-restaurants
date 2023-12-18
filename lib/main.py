from customer import Customer
from review import Review
from restaurant import Restaurant

# Assuming the Customer, Review, and Restaurant classes are defined as provided

# Creating restaurant instances
restaurant1 = Restaurant("Restaurant A")
restaurant2 = Restaurant("Restaurant B")

# Creating customer instances
customer1 = Customer("John", "Doe")
customer2 = Customer("Jane", "Smith")

# Customers adding reviews for restaurants
customer1.add_review(restaurant1, 4)
customer2.add_review(restaurant1, 5)
customer2.add_review(restaurant2, 3)

# Accessing information about restaurants and their reviews
print(f"{restaurant1.get_name()} reviews: {restaurant1.get_reviews()}")
print(f"{restaurant2.get_name()} reviews: {restaurant2.get_reviews()}")

# Getting customers who have reviewed a specific restaurant
customers_reviewed_restaurant1 = restaurant1.get_customers()
print(f"Customers who reviewed {restaurant1.get_name()}: {[customer.full_name() for customer in customers_reviewed_restaurant1]}")

# Calculating the average star rating for a restaurant
print(f"Average star rating for {restaurant1.get_name()}: {restaurant1.average_star_rating()}")
