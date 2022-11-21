from data.data import Person
from faker import Faker

faker_ru = Faker('ru_RU')
Faker.seed()  # прописание работы faker на русском


def generated_person():
    yield Person(
        FULL_NAME=faker_ru.first_name() + " " + faker_ru.last_name() + " " + faker_ru.middle_name(),
        EMAIL=faker_ru.email(),
        CURRENT_ADDRESS=faker_ru.address(),
        PERMANENT_ADDRESS=faker_ru.address()
    )
