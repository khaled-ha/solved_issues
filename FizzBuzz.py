
def check_constraint(n):
    return (n > 0) and (n < 1*(10**5))

def fizzBuzz(n):
    if check_constraint(n):
        for i in range(1,n):
            if (i % 5 == 0) and (i % 3 == 0):
                print('FizzBuzz')
            if (i % 5 == 0) and not (i % 3 == 0):
                print('Buzz')
            if not (i % 5 == 0) and (i % 3 == 0):
                print('Fizz')
            if not (i % 5 == 0) and not (i % 3 == 0):
                print(i)
