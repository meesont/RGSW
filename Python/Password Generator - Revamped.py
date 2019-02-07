import string, secrets

chars = (string.ascii_lowercase, string.ascii_uppercase, string.digits, string.punctuation)

passLengthMin = int(input('Enter minimum password length: '))
passLengthMax = int(input('Enter maximum password length: '))

size = lambda: secrets.choice(range(passLengthMin, passLengthMax))
char = lambda: secrets.choice(secrets.choice(chars))
pw = lambda: ''.join([char() for _ in range(size())])

for i in range(10):
    pw = pw()
    print(f'{i}) {len(pw)} chars :: {pw}')
