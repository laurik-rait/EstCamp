from django.shortcuts import render
from precise_bbcode.bbcode import get_parser

from pages.models import Homepage
from reservations.models import Reservation
from tickets.models import TicketType, Ticket


def home_view(request, *args, **kwargs):
    context = {
        'post': Homepage.objects.get(pk=1).text,
    }
    return render(request, 'index.html', context=context)


def tickets_view(request, *args, **kwargs):
    ticket_types = TicketType.objects.all()
    available_tickets = dict()
    for ticket_type in ticket_types:
        ticket_count = Ticket.objects.filter(type=ticket_type).count()
        reservation_count = Reservation.objects.filter(type=ticket_type).count()
        available_tickets[ticket_type] = ticket_type.limit - ticket_count - reservation_count

    context = {
        'available_tickets': available_tickets,
    }
    return render(request, 'tickets.html', context=context)
