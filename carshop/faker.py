from faker import Faker
from faker.providers import BaseProvider


class CarProvider(BaseProvider):
    def car_number(self):
        return f"{self.random_element('ABCDEFGHIJKLMNOPQRSTUVWXYZ')}{self.random_element('ABCDEFGHIJKLMNOPQRSTUVWXYZ')} {self.random_number(4)} {self.random_element('ABCDEFGHIJKLMNOPQRSTUVWXYZ')}{self.random_element('ABCDEFGHIJKLMNOPQRSTUVWXYZ')}"


fake = Faker()
fake.add_provider(CarProvider)

car_number = fake.car_number()
print(car_number)
