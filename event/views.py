from django.shortcuts import render
from django.views.generic import CreateView,ListView,DetailView,UpdateView,DeleteView
from .models import Event
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin


def get_index(request):
    return render(request, "home/index.html")




class EventCreateView(CreateView):
    fields = ("__all__")
    model = Event
    template_name = 'home/event_form.html'
    success_url="/list/"

class EventListView(LoginRequiredMixin, ListView):
    template_name = 'home/event_list.html'
    context_object_name = 'event'
    model=Event


class EventDetailView(LoginRequiredMixin,DetailView):
    context_object_name = 'event_detail'
    model = Event
    template_name = 'home/event_detail.html'


class EventUpdateView(LoginRequiredMixin,UpdateView):
    fields = ("__all__")
    model = Event
    template_name = 'home/event_form.html'
    success_url="/list/"


class EventDeleteView(LoginRequiredMixin,DeleteView):
    model=Event
    template_name = 'home/confirm_delete.html'
    success_url="/list/"