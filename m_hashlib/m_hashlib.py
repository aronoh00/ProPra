import hashlib

print(hashlib.algorithms_available)

hash_obj1 = hashlib.sha256()

hash_obj1.update(b"ProPra")
hash_hex = hash_obj1.hexdigest()
print("1. ProPra SHA-256:\t", hash_hex)

hash_obj2 = hashlib.sha256()
hash_obj2.update(b"ProPra ")
hash_hex2 = hash_obj2.hexdigest()
print("2. added a space:\t", hash_hex2)

countH = 0
countS = 0
for i in range(len(hash_hex)):
    if hash_hex[i] == hash_hex2[i]:
        countH += 1

for i in range(len(hash_hex)):
    countS = countS + 1/16
print("3. identical digits: expected:", countS, "found:", countH)

def check (a, b):
    count = 0
    for i in range(len(a)):
        if a[i] == b[i]:
            count += 1
    if count == len(a):
        return True
    else:    
        return False

hash_obj3 = hashlib.sha256()
hash_obj3.update(b"ProPra FU Berlin")
hash_hex3 = hash_obj3.hexdigest()
hash_obj1.update(b" FU Berlin")
hash_hex = hash_obj1.hexdigest()

if check(hash_hex, hash_hex3):
    print("4. ProPra;  FU Berlin = ProPra FU Berlin")
else:
    print("Fehler")

hash_hex4 = hashlib.file_digest(open("text.txt", "rb"), "sha256").hexdigest()

print("5. file checksum:\t", hash_hex4)