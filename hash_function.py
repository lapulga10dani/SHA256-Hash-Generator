import hashlib
text1 = input("Enter your text: ")
print("Original text1:", text1)
text2 = input("Enter your text: ")
print("Original text2:", text2)
hash_object1 = hashlib.sha256(text1.encode())
hash_object2 = hashlib.sha256(text2.encode())
hash_value1 = hash_object1.hexdigest()
print("Text 1 SHA-256 Hash:" , hash_value1)
print("Hash Length:" , len(hash_value1))
hash_value2 = hash_object2.hexdigest()
print("Text 2 SHA-256 Hash:" , hash_value2)
print("Hash Length:" , len(hash_value2))

if hash_value1 == hash_value2:
    print("Hashes Match")
else:
    print("Hashes Not Match")