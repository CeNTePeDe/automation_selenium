import random

from data.data import Person, Color, Date
from faker import Faker

faker_ru = Faker('ru_RU')
faker_en = Faker('En')
Faker.seed()  # прописание работы faker на русском


def generated_person():
    yield Person(
        FULL_NAME=faker_ru.first_name() + " " + faker_ru.last_name() + " " + faker_ru.middle_name(),
        FIRST_NAME=faker_ru.first_name(),
        LAST_NAME=faker_ru.last_name(),
        AGE=random.randint(10, 90),
        SALARY=random.randint(100, 10000),
        DEPARTMENT=faker_ru.job(),
        EMAIL=faker_ru.email(),
        CURRENT_ADDRESS=faker_ru.address(),
        PERMANENT_ADDRESS=faker_ru.address(),
        MOBILE=faker_ru.msisdn(),

    )


def generated_file():
    path = rf'C:\Users\Anton\PycharmProjects\automation_selenium\filetest{random.randint(0, 999)}.txt'
    file = open(path, "w+")
    file.write(f'Hello world{random.randint(1, 999)}')
    file.close()
    return file.name, path


def generated_color():
    yield Color(
        color_name=['Red', 'Blue', 'Green', 'Black', 'White', 'Violet', 'Indigo', 'Magenda', 'Aqua', 'Purple', 'Yellow']
    )


def generated_date():
    yield Date(
        year = faker_en.year(),
        month = faker_en.month_name(),
        day = faker_en.day_of_month(),
        time = "12:00",
    )