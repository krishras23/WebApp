def hi(name):
    print('Hello, {}' + (name))


hi("Krish")

print('%d %s cost $%.2f' % (6, 'bananas', 1.74))

print('{0} {2} cost ${1} {0}'.format(6, 'bananas', 1.74))
print('{} {} cost ${}'.format(6, 'bananas', 1.74))
quantity = 6
print('{quantity} {item} cost ${price}'.format(
    quantity=7,
    item='bananas',
    price=1.74))
