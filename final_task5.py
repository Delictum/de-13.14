purchases = [
    {"item": "apple", "category": "fruit", "price": 1.2, "quantity": 10},
    {"item": "banana", "category": "fruit", "price": 0.5, "quantity": 5},
    {"item": "milk", "category": "dairy", "price": 1.5, "quantity": 2},
    {"item": "bread", "category": "bakery", "price": 2.0, "quantity": 3},
]


def total_revenue(purchases):
    return sum(i['price'] * i['quantity'] for i in purchases)


def items_by_category(purchases):
    items_by_c = {}
    for i in purchases:
        category = i['category']
        if category not in items_by_c:
            items_by_c[category] = []
        items_by_c[category].append(i['item'])
    return items_by_c


def expensive_purchases(purchases, min_price):
    return [i for i in purchases if i['price'] >= min_price]


def average_price_by_category(purchases):
    category_price = {}
    category_count = {}
    
    for purchase in purchases:
        category = purchase['category']
        price = purchase['price']
        if category not in category_price:
            category_price[category] = 0
            category_count[category] = 0
        category_price[category] += price
        category_count[category] += 1
    
    return {category: category_price[category] / category_count[category] for category in category_price}


def most_frequent_category(purchases):
    category_quantity = {}    
    for i in purchases:
        category = i['category']
        if category not in category_quantity:
            category_quantity[category] = 0
        category_quantity[category] += i['quantity']
    return max(category_quantity, key=category_quantity.get)
    

min_price = 1.0
print(f"Общая выручка: {total_revenue(purchases)}")
print(f"Товары по категориям: {items_by_category(purchases)}")
print(f"Покупки дороже {min_price}: {expensive_purchases(purchases, min_price)}")
print(f"Средняя цена по категориям: {average_price_by_category(purchases)}")
print(f"Категория с наибольшим количеством проданных товаров: {most_frequent_category(purchases)}")
