from django.core.exceptions import ValidationError
from django.db import models

from django.utils.translation import gettext as _

import reservations


class TicketType(models.Model):
    name = models.CharField(max_length=100)
    name_et = models.CharField('Estonian name', default="", max_length=100)
    description = models.CharField(max_length=512, default="")
    description_et = models.CharField('Estonian description', max_length=512, default="")
    price = models.PositiveIntegerField()
    limit = models.PositiveIntegerField()

    def is_available(self):
        ticket_count = Ticket.objects.filter(type=self).count()
        reservation_count = reservations.models.Reservation.objects.filter(type=self).count()

        return (ticket_count + reservation_count) < self.limit

    def __str__(self):
        return f"{self.name}"


class Ticket(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    type = models.ForeignKey(TicketType, on_delete=models.CASCADE)
    issue_date = models.DateTimeField('issued at', auto_now_add=True)

    def clean(self, *args, **kwargs):
        if self.pk is None:
            if not self.type.is_available():
                raise ValidationError(_("There are no more tickets available for this type."))

    def __str__(self):
        return f"{self.name} || {self.type.name}"

