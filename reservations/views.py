from django import forms
from django.forms import ModelForm, ModelChoiceField
from django.shortcuts import render, redirect

from reservations.models import Reservation
from tickets.models import TicketType


class ReservationForm(ModelForm):
    type = ModelChoiceField(queryset=TicketType.objects, empty_label=None)

    class Meta:
        model = Reservation
        fields = ["name", "email", "type"]


# Create your views here.
def reservation_view(request, *args, **kwargs):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save()
            return render(request, 'reserve.html', {'reservation': reservation})
    else:
        form = ReservationForm()

    context = {
        'form': form,
    }

    if "reservation" in kwargs:
        context['reservation'] = kwargs.get("reservation")

    return render(request, 'reserve.html', context=context)
