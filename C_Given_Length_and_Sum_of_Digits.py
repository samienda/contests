m, s = list(map(int, input().split()))
total = s

maxi = []

for i in range(m):
    curr = 9 if s >= 9 else s
    s -= curr

    maxi.append(curr)

# print(maxi)

s = total

curr = 1 if s < 9 * (m - 1) else s - ((m - 1) * 9)
s -= curr

mini = [curr]
for i in range(1, m):
    curr = 0 if s < 9 * (m - i - 1) else s - ((m - i - 1) * 9)
    s -= curr
    mini.append(curr)

# print(mini)
left = sum(mini)
right = sum(maxi)
# print(left, right, total)

print(*["".join(map(str, mini)), "".join(map(str, maxi))] if left == right == total else [-1, -1])



from Crypto.Cipher import AES
from ctypes import *
import time
from datetime import datetime

plaintext_hex = '255044462d312e350a25d0d4c5d80a34'
ciphertext_hex = 'd06bf9d0dab8e8ef880660d2af65aa82'
IV_hex = '09080706050403020100A2B2C2D2E2F2'


# Changing given data into bytes
known_plaintext = bytes.fromhex(plaintext_hex)
ciphertext = bytes.fromhex(ciphertext_hex)
IV = bytes.fromhex(IV_hex)



# Key generator function
def generator(timestamp):
    libc = CDLL('libc.so.6')
    KEYSIZE = 16


    libc.srand(timestamp)
    key = [libc.rand() % 256 for _ in range(KEYSIZE)]
    formatted_key = (''.join(format(byte, '02x') for byte in key))
    formatted_key = bytes.fromhex(formatted_key)
    return formatted_key


## Decrypter Function
def decrypt_AES_CBC(ciphertext, key, IV):
    cipher = AES.new(key, AES.MODE_CBC, IV)
    plaintext = cipher.decrypt(ciphertext)
    return plaintext

## Change date format
date_string = "2018-04-17 23:08:49"
datetime_object = datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S")
start_time = int(datetime_object.timestamp()) - 7200
end_time = int(datetime_object.timestamp()) 


## actual loop that checks every key generated within that time period
for timestamp in range(int(start_time), int(end_time) + 1):
    key = generator(timestamp)

    decrypted = decrypt_AES_CBC(ciphertext, key, IV)

    if decrypted == known_plaintext:
        print("Key found:", key.hex())
        print("Timestamp:", timestamp.hex())
        print("Decrypted plaintext:", decrypted.hex())
        break
else:
    print("Key not found within the time window.")
