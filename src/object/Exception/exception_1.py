from object.Exception.my_exception import MyException

price = ""
try:
    price = input('price: ')
    price = int(price)
    if price > 200 or price <= 99:
        raise MyException(price)
except MyException as x:
    print('Error,price value:', x, 'not correct')
except ValueError:
    print('The value:', price, 'must be an natural number')
else:
    print('Everything is fine')
finally:
    print('Verification done')






