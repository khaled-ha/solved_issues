def check_constraints(numbers):
    if (len(numbers)) >= 1 and (len(numbers) <= 10 ** 4) and all([(x >= 1 and x <= 10**4) for x in numbers]):
        return True
    return False

def arraySum(numbers):
    # Write your code here
    sum = 0 
    if check_constraints(numbers):
        for x in numbers:
            sum += x
    return sum
