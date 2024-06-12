import random
from django.contrib.auth.hashers import make_password
from faker import Faker
from api.models import Contact, Spam, User
# from django.contrib.auth.models import User

fake = Faker()

# Populate users
for _ in range(10):
    name = fake.name()
    phone_number = fake.phone_number()
    email = fake.email()
    password = make_password('password123')  # Default password for testing
    User.objects.create(name=name,phone_number=phone_number, email=email, password=password)

# Populate contacts
users = User.objects.all()
for user in users:
    for _ in range(random.randint(0, 5)):
        name = fake.name()
        phone_number = fake.phone_number()
        likelihood = random.uniform(0, 1)
        Contact.objects.create(user=user, name=name, phone_number=phone_number, likelihood=likelihood)

# Populate spam numbers
for _ in range(5):
    phone_number = fake.phone_number()
    likelihood = random.uniform(0, 1)
    Spam.objects.create(phone_number=phone_number, likelihood=likelihood)

print("Data populated successfully!")
