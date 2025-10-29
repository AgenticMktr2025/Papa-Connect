import reflex as rx
from typing import Optional
from app.database import get_db
from app.models.db_models import User
from passlib.context import CryptContext
from jose import JWTError, jwt
import datetime

SECRET_KEY = "super-secret-key-that-should-be-in-env"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class AuthState(rx.State):
    error_message: str = ""
    is_authenticated: bool = False
    token: str = ""

    @rx.event
    def verify_password(self, plain_password, hashed_password):
        return pwd_context.verify(plain_password, hashed_password)

    @rx.event
    def get_password_hash(self, password):
        return pwd_context.hash(password)

    @rx.event
    async def login(self, form_data: dict) -> bool:
        with get_db() as db:
            user = db.query(User).filter(User.email == form_data["email"]).first()
        if not user or not self.verify_password(
            form_data["password"], user.password_hash
        ):
            self.error_message = "Incorrect email or password"
            return False
        access_token_expires = datetime.timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        self.token = self.create_access_token(
            data={"sub": str(user.id)}, expires_delta=access_token_expires
        )
        self.is_authenticated = True
        return True

    @rx.event
    async def register(self, form_data: dict) -> bool:
        with get_db() as db:
            if db.query(User).filter(User.email == form_data["email"]).first():
                self.error_message = "Email already registered"
                return False
            hashed_password = self.get_password_hash(form_data["password"])
            new_user = User(
                email=form_data["email"],
                name=form_data["email"].split("@")[0],
                password_hash=hashed_password,
            )
            db.add(new_user)
            db.commit()
            db.refresh(new_user)
        return await AuthState.login(form_data)

    @rx.event
    def create_access_token(
        self, data: dict, expires_delta: Optional[datetime.timedelta] = None
    ):
        to_encode = data.copy()
        if expires_delta:
            expire = datetime.datetime.utcnow() + expires_delta
        else:
            expire = datetime.datetime.utcnow() + datetime.timedelta(minutes=15)
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
        return encoded_jwt

    @rx.event
    def logout(self):
        self.is_authenticated = False
        self.token = ""