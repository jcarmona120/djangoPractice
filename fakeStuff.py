import django
from faker import Faker
fake = Faker()

print(django.setup())

print(fake.name())
# 'Lucy Cechtelar'
