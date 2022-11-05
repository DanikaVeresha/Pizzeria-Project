import random
from collections import namedtuple

Pizza = namedtuple('Pizza', ['idx', 'name', 'price', 'description'])


def pizzas_list():

    for item in Pizzas:
        print(f'\n {item.idx}. {item.name}:'
              f'\n Description: {item.description}')


def dec_1(func):
    def inner():
        print('----------------------------------------------------------------')
        func()
        d = random.randint(1, 31)
        m = random.randint(1, 12)
        n = random.randint(1, 100)
        print(f'data:_{d}/{m}/2022_, check_№:_{n}_\n'
              f'You were served by: - cashier:Veresha_Dasha')
        print('----------------------------------------------------------------')
    return inner


def dec_2(func):
    def inner():
        print('-------------Category of pizzas by pricing policy: -------------')
        func()
        print('----------------------------------------------------------------')
    return inner


@dec_1
def check():
    order = random.randint(1, 6)
    print(f'Number of checks for the current day: {order}\n'
          f'Pizza: price - amount')
    check_order = random.sample(Pizzas, order)
    sum = 0
    for item in check_order:
        amount = random.randint(1, 3)
        sum1 = item.price * amount
        sum += sum1
        print(f'{item.name}: {item.price} UAH - {amount}\n'
              f'All by check: {sum1} UAH')
    print(f'Total for the check for the current day: {sum} UAH')


@dec_2
def pizza_price_range():
    pizzas_1 = filter(lambda item: item.price < 150, Pizzas)
    print(f'The price of pizza is less than 150 UAH:')
    for item in pizzas_1:
        print(f'{item.idx}. {item.name} - {item.price} UAH')
    pizzas_2 = filter(lambda item: item.price > 150, Pizzas)
    print(f'The price of pizza is more than 150 UAH:')
    for item in pizzas_2:
        print(f'{item.idx}. {item.name} - {item.price} UAH')
    pizzas_3 = filter(lambda item: item.price == 150, Pizzas)
    print(f'The price of pizza is 150 UAH:')
    for item in pizzas_3:
        print(f'{item.idx}. {item.name}')


Pizzas = [
    Pizza(1, 'Hawaiian', 100, 'Chicken + pineapple + bakery + mozzarella + sauce'),
    Pizza(2, 'Carbonara', 110, 'Bacon + tavern + bakery + marinated + olives + mozzarella'),
    Pizza(3, 'M`yasna', 120, 'Bacon + salami + tomato + mozzarella'),
    Pizza(4, 'Margarita', 130, 'Tomato + mozzarella + sauce + salami'),
    Pizza(5, 'Mislivska', 140, 'Hunting sausages + salami + salted cucumber + garlic'),
    Pizza(6, 'Vegetable teriyaki', 150, 'Tomato + mushrooms + bell pepper + pickles'),
    Pizza(7, 'Pepperoni', 160, 'Pepperoni + italian herbs + mozzarella + signature sauce'),
    Pizza(8, 'Francesca', 170, 'Bacon + salami + mushrooms + tomato + olives + mozzarella'),
    Pizza(9, 'Four cheeses', 180, 'Dor bleu cheese + gouda cheese + cream cheese + mozzarella'),
    Pizza(10, 'Sharp', 200, 'Salami + tomatoes + bell pepper + green beans + sauce')
]

while True:
    print('Hello. 0 - Exit, 1 - all pizzas(), 2 - pizza_price_range, 3 - order')
    c = input('Your choise: ')
    match c:
        case '0':
            break
        case '1':
            pizzas_list()
        case '2':
            pizza_price_range()
        case '3':
            check()
        case _:
            print('Wrong choise! Try again')

print('Bye')
