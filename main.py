import sys,os

def gcd(p, q):
    while q:
        p, q = q, p % q
    return p


def lcm(p, q):
    return (p * q) // gcd(p, q)


def generate_keys(p, q):
    N = p * q
    L = lcm(p - 1, q - 1)

    for i in range(2, L):
        if gcd(i, L) == 1:
            E = i
            break

    for i in range(2, L):
        if (E * i) % L == 1:
            D = i
            break

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


def get_files(extention, directory):
    file_list = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(extention):
                file_list.append(os.path.join(root, file))
    return file_list


def print_result(file, public_key, private_key):
    with open(file) as f:
        plain_text = f.read()
        encrypted_text = encrypt(plain_text, public_key)
        decrypted_text = decrypt(encrypted_text, private_key)
        print(f'''
        秘密鍵: {public_key}
        公開鍵: {private_key}

        平文:
        「{plain_text}」

        暗号文:
        「{sanitize(encrypted_text)}」

        平文 (復号化後):
        「{decrypted_text}」
        '''[1:-1])


def main():
    public_key, private_key = generate_keys(101, 3259)
    directory = sys.argv[1]
    files = get_files('.md', directory)
    for file in files:
        print_result(file, public_key, private_key)


if __name__ == '__main__':
    main()
