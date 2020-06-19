from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["argon2"])


def hash_password(password: str) -> str:
    return pwd_context.hash(password)
