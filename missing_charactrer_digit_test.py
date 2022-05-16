def get_missing_digits(s):
    return sorted({0,1,2,3,4,5,6,7,8,9} - set([int(i) for i in s if i.isdigit()]))

def get_missing_characters(s):
    return sorted({'a', 'b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'} - set([i for i in s if i.isalpha()]))
    
def missingCharacters(s):
    # Write your code here
    missed_digits , missed_characters = '', ''
    for x in get_missing_digits(s.lower()):
        missed_digits += str(x) 
    for x in get_missing_characters(s.lower()):
        missed_characters += x 
    print(missed_digits + missed_characters)
    return missed_digits + missed_characters

