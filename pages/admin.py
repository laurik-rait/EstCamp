from django.contrib import admin

from pages.models import Homepage


@admin.register(Homepage)
class HomepageAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return False if self.model.objects.count() > 0 else super().has_add_permission(request)

    def has_delete_permission(self, request, obj=None):
        return False
