from typing import Iterator

from users_generator.utils import User, generate_user


def generator_of_users(amount_of_users: int) -> Iterator[User]:
    for _ in range(amount_of_users):
        yield generate_user()
