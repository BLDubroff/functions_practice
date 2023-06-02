def hello():
    print("Hello!")

def pack(item1, item2, item3):
    return [item1, item2, item3]

def eat_lunch(foods):
    if len(foods) == 0:
        print('My lunchbox is empty!')
        return

    print(f'First I eat {foods[0]}')

    for food in foods[1:]:
        print(f'Next I eat {food}')

# calling hello function
hello()

# testing pack function
print(pack("One", True, 3))

# testing foods function
foods = ['fruit', 'sandwiches', 'chocolate']
eat_lunch(foods)