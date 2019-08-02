import time

def gcd(p, q):
    while q:
        p, q = q, p % q
    return p


def lcm(p, q):
    return (p * q) // gcd(p, q)


def generate_keys(p, q):
    N = p * q
    L = lcm(p - 1, q - 1)

    start = time.time()

    for i in range(2, L):
        if gcd(i, L) == 1:
            E = i
            break

    elapsed_time = time.time() - start
    print ("elapsed_time:{0}".format(elapsed_time) + "[sec]")

    start = time.time()

    for i in range(2, L):
        if (E * i) % L == 1:
            D = i
            break

    elapsed_time = time.time() - start
    print ("elapsed_time:{0}".format(elapsed_time) + "[sec]")

    return (E, N), (D, N)


def encrypt(plain_text, public_key):
    E, N = public_key
    plain_integers = [ord(char) for char in plain_text]
    encrypted_integers = [i ** E % N for i in plain_integers]
    encrypted_text = ''.join(chr(i) for i in encrypted_integers)
    return encrypted_text


def decrypt(encrypted_text, private_key):
    D, N = private_key
    encrypted_integers = [ord(char) for char in encrypted_text]
    decrypted_intergers = [i ** D % N for i in encrypted_integers]
    decrypted_text = ''.join(chr(i) for i in decrypted_intergers)
    return decrypted_text


def sanitize(encrypted_text):
    return encrypted_text.encode('utf-8', 'replace').decode('utf-8')
