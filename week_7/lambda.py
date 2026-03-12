# add_and_square = lambda a, b: (a + b) ** 2


# check_even = lambda n: "Even" if n % 2 == 0 else "Odd"

# print(check_even(5))

calculate_price = lambda price, is_number: price -  (price *(0.20 if is_number else .05))



print(calculate_price(20,True))