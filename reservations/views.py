from django.forms import ModelForm, ModelChoiceField
from django.shortcuts import render

from reservations.models import Reservation
from tickets.models import TicketType


class ReservationForm(ModelForm):
    type = ModelChoiceField(queryset=TicketType.objects, empty_label=None)

    class Meta:
        model = Reservation
        fields = ["name", "email", "type"]


def reservation_view(request, type_id=None, *args, **kwargs):
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

    if type_id:
        context['selected_type'] = type_id

    if "reservation" in kwargs:
        context['reservation'] = kwargs.get("reservation")
    else:
        available_types = set()
        for t in TicketType.objects.all():
            if t.is_available():
                available_types.add(t)
        context['available_types'] = available_types

    return render(request, 'reserve.html', context=context)
