from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Topic, AccessDate, WebPage

# Create your views here.
def index(request):
    web_list = AccessDate.objects.order_by("date")
    date_dict = {"access_dates": web_list}
    # Context means the data being transferred
    return render(request,"first_app/index.html", context=date_dict)
