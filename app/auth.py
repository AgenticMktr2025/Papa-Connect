import bcrypt
from jose import JWTError, jwt
import datetime
import os
import logging

SECRET_KEY = os.environ.get("SECRET_KEY", "a-very-secret-key-that-is-not-secure")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


def hash_password(password: str) -> str:
    """Hashes a password using bcrypt."""
    return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Verifies a plain password against a hashed password."""
    try:
        return bcrypt.checkpw(
            plain_password.encode("utf-8"), hashed_password.encode("utf-8")
        )
    except (ValueError, TypeError) as e:
        logging.exception(f"Error verifying password: {e}")
        return False


def create_access_token(
    user_id: int, expires_delta: datetime.timedelta | None = None
) -> str:
    """Creates a new JWT access token."""
    to_encode = {"sub": str(user_id)}
    if expires_delta:
        expire = datetime.datetime.now(datetime.timezone.utc) + expires_delta
    else:
        expire = datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(
            minutes=ACCESS_TOKEN_EXPIRE_MINUTES
        )
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)


def verify_token(token: str) -> int | None:
    """Verifies a JWT token and returns the user ID if valid."""
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id_str = payload.get("sub")
        if user_id_str is None:
            return None
        return int(user_id_str)
    except JWTError as e:
        logging.exception(f"Error decoding token: {e}")
        return None