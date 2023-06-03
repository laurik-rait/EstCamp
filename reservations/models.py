from django.core.exceptions import ValidationError
from django.db import models

from tickets.models import Ticket, TicketType
from django.utils.translation import gettext as _


class Reservation(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    type = models.ForeignKey(TicketType, on_delete=models.CASCADE)
    reservation_date = models.DateTimeField('reserved at', auto_now_add=True)

    def issue_ticket(self):
        ticket = Ticket(name=self.name, email=self.email, type=self.type)
        ticket.save()
        self.delete()

    def clean(self, *args, **kwargs):
        if self.pk is None:
            if not self.type.is_available():
                raise ValidationError(_("There are no more tickets available for this type."))

    def __str__(self):
        return f"{self.name} || {self.type.name}"
