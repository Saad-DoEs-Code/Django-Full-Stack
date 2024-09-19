import os

import django
from faker import Faker

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project_2.settings')
django.setup()

fake_gen = Faker()

from app_two.models import User
def populate(n=5):

    for entry in range(n):
        fake_first_name = fake_gen.name()
        fake_last_name=fake_gen.last_name()
        fake_email = fake_gen.email()

        fake_user = User.objects.get_or_create(first_name= fake_first_name,last_name=fake_last_name, email_address = fake_email)[0]

        fake_user.save()

if __name__ == "__main__":
    print("Populating script!")
    populate(20)
    print("Populating complete!")


