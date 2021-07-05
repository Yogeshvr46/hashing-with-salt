import hashlib

sec = input("Enter the text to be  Hashed  : ")
MD5 = hashlib.md5()
print("The Hexadecimal of md5 code is : ", MD5.hexdigest())
MD5 = hashlib.sha256()
print("The Hexadecimal of  sha256 code  is : ", MD5.hexdigest())
MD5 = hashlib.shake_256()
print("The Hexadecimal of shake_256 code is : ", MD5.hexdigest(20))
#used for converting a normal string to hashed one with multiple algorithms for different codes