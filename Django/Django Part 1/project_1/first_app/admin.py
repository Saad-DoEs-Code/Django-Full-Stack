from django.contrib import admin
from first_app.models import Topic, AccessDate, WebPage

# Register your models here.
admin.site.register(Topic)
admin.site.register(AccessDate)
admin.site.register(WebPage)
