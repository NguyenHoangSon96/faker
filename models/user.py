from dataclasses import dataclass


@dataclass(frozen=True)
class User:
    code: str
    email: str
    phone_number: str
    first_name: str
    last_name: str
    age: int
    address: str
    locale: str
