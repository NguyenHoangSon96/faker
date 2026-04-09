import random
from uuid import UUID

from faker import Faker
from faker.providers import person

from models.user import User


class FakerGenerator:
    def __init__(self, seed=None, locale=None, providers=None):
        self.locale = locale
        self.seed = seed
        self.faker = Faker(seed=seed, locale=locale, providers=providers)
        self.faker.add_provider(person)
        pass

    def gen_unique_users(self, iterator_count: int) -> set[User] | None:
        try:
            results = {self.gen_user() for i in range(iterator_count)}
            return results
        except Exception as e:
            raise e

    def gen_user(self) -> User | None:
        try:
            return User(
                code=UUID(int=random.getrandbits(128)).__str__(),
                email=self.faker.email(),
                phone_number=self.faker.phone_number(),
                first_name=self.faker.first_name(),
                last_name=self.faker.last_name(),
                age=random.randint(1, 100),
                address=self.faker.address(),
                locale=self.locale,
            )
        except Exception as e:
            raise e
