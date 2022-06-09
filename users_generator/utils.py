from typing import NamedTuple

from faker import Faker

fake = Faker('ru_RU')


class User(NamedTuple):
    name: str
    email: str


def generate_user() -> User:
    return User(fake.first_name(), fake.unique.ascii_email())
