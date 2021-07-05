import hashlib
import uuid
from module import sec
Texthash = (sec)
print(sec) #used to identitfy whether the given data from module is being fetched or not
secure = hashlib.sha256(Texthash.encode()).hexdigest()
print("the encoded code for the text is :", secure)
salt = uuid.uuid4().hex
print("the salt is : ", salt)
hashed = hashlib.sha256(Texthash.encode()).hexdigest() + salt
print("the salted code is : ", hashed)
