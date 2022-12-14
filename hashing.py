from passlib.context import CryptContext

# Initialize Password Hashing
pwd_cxt = CryptContext(schemes=['bcrypt'], deprecated="auto")

class Hash():
    def bcrypt(password: str):
        return pwd_cxt.hash(password)
    
    def verify(plain_password, hashed_paswword):
        return pwd_cxt.verify(plain_password, hashed_paswword)
