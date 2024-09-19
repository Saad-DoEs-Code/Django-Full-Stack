import os
import random
from faker import Faker
fake_gen = Faker()
os.environ.setdefault("DJANGO_SETTINGS_MODULE","project_1.settings")

import django
django.setup()

from first_app.models import Topic, WebPage, AccessDate

topic_list = ["Social","Streaming","Searching","Services"]

def save_topic():
    t = Topic.objects.get_or_create(topic_name=random.choice(topic_list))[0]
    t.save()
    return t

def populate_data(N=5):
    
    for entry in range(N):

        # Create new topic
        t = save_topic()
    
        # Create Fake Data for Website
        fake_url = fake_gen.url()
        fake_date = fake_gen.date()
        fake_name = fake_gen.company()

        # Create new webpage entry
        web_page = WebPage.objects.get_or_create(topic=t, name=fake_name, url=fake_url)[0]
        web_page.save()

        # Create new access date entry
        access_date = AccessDate.objects.get_or_create(name=web_page, date=fake_date)[0]
        access_date.save()


if __name__ == "__main__":
    print("Populating script!")
    populate_data(20)
    print("Populating complete!")



