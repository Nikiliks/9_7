def is_prime(func):
    def wrapper(*nums):
        new = func(*nums)
        for i in range(2, round(new ** 0.5)):
            if new % i == 0:
                print('Cоставное', new)
                break

        else:
            print('Простое', new)
    return wrapper

@is_prime
def sum_three(a, b, c):
    res = (a + b + c)
    return res

sum_three(2, 3, 6)