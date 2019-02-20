from django.shortcuts import render
from django.views.generic import CreateView,ListView,DetailView,UpdateView,DeleteView
from .models import Event
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin


def get_index(request):
    return render(request, "home/index.html")




class EventCreateView(CreateView):
    fields = ['event_name', 'description','date','venue','venue_url','code']
    model = Event
    template_name = 'home/event_form.html'
    success_url="/list/"

    def form_valid(self, form):
        user = self.request.user
        form.instance.user = user
        return super(EventCreateView, self).form_valid(form)

class EventListView(LoginRequiredMixin, ListView):
    template_name = 'home/event_list.html'
    context_object_name = 'event'
    model=Event


    def get_queryset(self):
        user=self.request.user
        queryset = Event.objects.filter(user=self.request.user)
        return queryset

class EventDetailView(LoginRequiredMixin,DetailView):
    context_object_name = 'event_detail'
    model = Event
    template_name = 'home/event_detail.html'



class EventUpdateView(LoginRequiredMixin,UpdateView):
    fields = ("__all__")
    model = Event
    template_name = 'home/event_form.html'
    success_url="/list/"
    fields = ['event_name', 'description','date','venue','venue_url','code']



class EventDeleteView(LoginRequiredMixin,DeleteView):
    model=Event
    template_name = 'home/confirm_delete.html'

    success_url="/list/"

