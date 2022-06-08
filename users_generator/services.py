from collections import namedtuple

from faker import Faker

fake = Faker('ru_RU')


def generator(quantity: int = 100):
    user = namedtuple('user', 'name email')
    return (user(fake.first_name(), fake.unique.ascii_email()) for _ in range(quantity))
