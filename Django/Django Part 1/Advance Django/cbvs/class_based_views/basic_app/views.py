from django.shortcuts import render
from django.views.generic import (View, TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView)
from django.urls import reverse_lazy
from basic_app.models import School, Student

class SchoolListView(ListView):
    # ListView returns context in list form => model_list
    context_object_name = "schools"
    model = School
    template_name = "basic_app/school_list.html"
    # The list view that is being passed to the template, is by default being returned as context in form of "school_list" => Syntax: (model_list)

class SchoolDetailView(DetailView):
    # DetailView returns context in lowercase => lowercase(model)
    context_object_name = "school_details"
    model= School
    template_name = 'basic_app/school_detail.html'


class SchoolCreateView(CreateView):

    fields = ('name', 'principal', 'address')
    model = School
    template_name = "basic_app/school_create.html"

class SchoolUpdateView(UpdateView):

    fields = ('principal', 'address')
    model = School
    template_name = "basic_app/school_create.html"

class SchoolDeleteView(DeleteView):
    model = School
    success_url = reverse_lazy('basic_app:list')



# Create your views here.
# class IndexView(TemplateView):

#     template_name = "basic_app/index.html"

#     def get_context_data(self, **kwargs: Any):
        
#         context = super().get_context_data(**kwargs)
#         context['title'] = "INDEX PAGE"
#         context['para'] = "The colored text is being injected from views."
#         return context
