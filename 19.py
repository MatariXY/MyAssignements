# import json
#
# class Product:
#     def __init__(self, name, price, quantity):
#         self.name = name
#         self.price = price
#         self.quantity = quantity
#
#     def to_dict(self):
#         return {
#             'name': self.name,
#             'price': self.price,
#             'quantity': self.quantity
#         }
#
#     @classmethod
#     def from_dict(cls, data):
#         return cls(data['name'], data['price'], data['quantity'])
#
#     def __str__(self):
#         return f"Product(name='{self.name}', price={self.price}, quantity={self.quantity})"
#
# products = [
#     Product("Laptop", 1200, 5),
#     Product("Mouse", 20, 50),
#     Product("Keyboard", 45, 30)
# ]
#
# def serialize_products(products, filename):
#     with open(filename, 'w') as file:
#         json.dump([product.to_dict() for product in products], file)
#
# def deserialize_products(filename):
#     with open(filename, 'r') as file:
#         data = json.load(file)
#         return [Product.from_dict(item) for item in data]
#
# serialize_products(products, 'products.json')
#
# deserialized_products = deserialize_products('products.json')
# for product in deserialized_products:
#     print(product)
################################################
################################################

import json


# JSON ფაილის წაკითხვის და დამუშავების ფუნქცია
def process_movies(filename):
    # ფაილის წაკითხვა
    with open(filename, 'r') as file:
        data = json.load(file)

    # ფილმების შენახვა ახალი სიისთვის
    updated_movies = []

    # ფილმების პირველი გვერდის შედეგების დამუშავება
    for movie in data[0]['results']:
        release_year = int(movie['release_date'].split('-')[0])  # გამოშვების წლის გამოთვლა

        # ფილმების ფილტრაცია და ცვლილებების შეტანა
        if release_year > 2000 and 'Crime' in movie['genres']:
            movie['genres'] = ['New_Crime' if genre == 'Crime' else genre for genre in movie['genres']]
            updated_movies.append(movie)

        elif release_year < 2000 and 'Drama' in movie['genres']:
            movie['genres'] = ['Old_Drama' if genre == 'Drama' else genre for genre in movie['genres']]
            updated_movies.append(movie)

        elif release_year == 2000:
            movie['genres'].append('New_Century')
            updated_movies.append(movie)

    # ფილმების განახლებული სია ხელახლა ჩაწერა JSON ფაილში
    with open(filename, 'w') as file:
        json.dump([{'page': 1, 'results': updated_movies}], file, indent=4)


# ფუნქციის გამოძახება movies.json ფაილზე
process_movies('movies.json')
