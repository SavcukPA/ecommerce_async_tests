from faker import Faker

fake = Faker()


class Payloads:

    random_user = {
        "email": fake.email(),
        "password": fake.password(),
        "first_name": fake.first_name(),
        "last_name": fake.last_name(),
    }
