def checkPrime(n):
    if n < 2:
        return False
    else:
        if n == 2:
            return True
        else:
            for i in range(2, n):
                if n % i == 0:
                    return False
            return True

if __name__ == '__main__':
    num = int(input('Enter a number to check if prime >> '))
    isPrime = checkPrime(num)
    if(isPrime):
        print(f'{num} is prime')
    else:
        print(f'{num} is not prime')
