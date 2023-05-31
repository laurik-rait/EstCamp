from django.contrib import admin
from .models import Ticket, TicketType


@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ("name", "type", "email", "issue_date")


@admin.register(TicketType)
class TicketTypeAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "limit")
