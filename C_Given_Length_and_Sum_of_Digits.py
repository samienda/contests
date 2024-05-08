# m, s = list(map(int, input().split()))
# total = s

# maxi = []

# for i in range(m):
#     curr = 9 if s >= 9 else s
#     s -= curr

#     maxi.append(curr)

# print(maxi)

# s = total
# mini = []
# for i in range(m):
#     curr = 1 if s < 9 * (m - i - 1) else s - ((m - i - 1) * 9)
#     s -= curr
#     mini.append(curr)

# print(mini)
# left = sum(mini)
# right = sum(maxi)
# print(left, right, total)

# print(*["".join(map(str, mini)), "".join(map(str, maxi))] if left == right == total else [-1, -1])

import time
from datetime import datetime, timezone

creation_time = time.strptime("2018-04-15 15:00:00", "%Y-%m-%d %H:%M:%S")
linux_time = int(time.mktime(creation_time))

date_string = "2018-04-15 15:00:00"
datetime_object = datetime.strptime(
    date_string, "%Y-%m-%d %H:%M:%S").replace(tzinfo=timezone.utc)
windows_time = int(datetime_object.timestamp()) + 14400

print("Linux Time:", linux_time)
print("Windows Time:", windows_time)

import time
from datetime import datetime

# Example seconds since the epoch
seconds_since_epoch = 1523818800  # Example value

# Convert seconds since the epoch to a datetime object
datetime_object = datetime.utcfromtimestamp(seconds_since_epoch)

# Convert the datetime object to a date string
date_string = datetime_object.strftime("%Y-%m-%d %H:%M:%S")

# Print the date string
print("Date string:", date_string)
print(seconds_since_epoch - windows_time)


from Crypto.Cipher import AES
#for time manuplation
from ctypes import *
import time
from datetime import datetime , timezone

# Given data
plaintext_hex = '255044462d312e350a25d0d4c5d80a34'
ciphertext_hex = 'd06bf9d0dab8e8ef880660d2af65aa82'
IV_hex = '09080706050403020100A2B2C2D2E2F2'


# Changing given data into bytes
known_plaintext = bytes.fromhex(plaintext_hex)
ciphertext = bytes.fromhex(ciphertext_hex)
IV = bytes.fromhex(IV_hex)



# Key generator function
libc = cdll.msvcrt
def generator(timestamp):
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
start_time = int(datetime_object.timestamp()) - 200000
end_time = int(datetime_object.timestamp()) + 200000


## actual loop that checks every key generated within that time period
for timestamp in range(int(start_time), int(end_time) + 1):
    key = generator(timestamp)
    # print(key)

    decrypted = decrypt_AES_CBC(ciphertext, key, IV)

    if decrypted == known_plaintext:
        print("Key found:", key)
        print("Timestamp:", timestamp)
        print("Decrypted plaintext:", decrypted)
        break
else:
    print("Key not found within the time window.")

# new_key = '95fa2030e73ed3f8da761b4eb805dfd7'
# new_key = bytes.fromhex(new_key)
# print("nk: ", new_key)

# decypt = decrypt_AES_CBC(ciphertext , new_key , IV)

# if decypt == known_plaintext:
#     print("Yayy!!")

