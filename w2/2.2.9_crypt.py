from simplecrypt import encrypt, decrypt

with open("encrypted.bin", "rb") as inp:
    ciphertext = inp.read()

# plain_text = decrypt('RVrF2qdMpoq6Lib', ciphertext)
with open('password.txt') as f:
    for password in f:
        password = password.strip()
        try:
            print(password)
            plain_text = decrypt(password, ciphertext)
        except:
            pass

print(plain_text)
# from simplecrypt import encrypt, decrypt
#
# def decrypt_file(file_name, key):
#     with open(file_name, 'rb') as inp:
#         encrypted = inp.read()
#     dec = decrypt(key, encrypted)
#     print("decrypted text: %s" % dec)
#
# passwords = [line.rstrip('\n') for line in open('password.txt')]
# for i in passwords:
#  try:
#      print(i)
#      decrypt_file("encrypted.bin", i)
#  except:
#      pass