import sys,os
from prime import gen_prime
from rsa import generate_keys

def get_files(extention, directory):
    file_list = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(extention):
                file_list.append(os.path.join(root, file))
    return file_list


def encrypt_file(file, public_key):
    with open(file, mode='r+') as f:
        plain_text = f.read()
        f.seek(0)
        f.truncate()
        encrypted_text = encrypt(plain_text, public_key)
        f.write(encrypted_text)


def decrypt_file(file, private_key):
    with open(file, mode='r+') as f:
        crypt_text = f.read()
        f.seek(0)
        f.truncate()
        decrypted_text = decrypt(crypt_text, private_key)
        f.write(decrypted_text)


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
    public_key, private_key = generate_keys(gen_prime(128), gen_prime(128))
    directory = sys.argv[1]
    files = get_files('.md', directory)
    for file in files:
        print_result(file, public_key, private_key)
        encrypt_file(file, public_key)
        decrypt_file(file, private_key)


if __name__ == '__main__':
    main()
