str = input('Enter str to check for palindrome: ')

def reverse(str):
    return str[::-1]

if(reverse(str) == str):
    print(f'{str} is a palindrome')
else:
    print(f'{str} is not a palindrome')
