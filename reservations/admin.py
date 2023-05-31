from django.contrib import admin, messages
from django.utils.safestring import mark_safe

from reservations.models import Reservation


@admin.action(description="Issue tickets for selected reservations")
def issue_tickets(modeladmin, request, queryset):
    for item in queryset:
        item.issue_ticket()


@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ("name", "type", "email", "reservation_date")
    actions = [issue_tickets]
