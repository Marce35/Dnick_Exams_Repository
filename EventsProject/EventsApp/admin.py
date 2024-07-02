from django.contrib import admin

from EventsApp.models import Event, Band, BandEvent


# Register your models here.

class BandEventAdminInline(admin.StackedInline):
    model = BandEvent
    extra = 0


class EventsAdmin(admin.ModelAdmin):
    exclude = ["user", "bands", ]
    list_display = ('name', 'date_time')
    inlines = [BandEventAdminInline, ]

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.user = request.user

        return super(EventsAdmin, self).save_model(request, obj, form, change)

    def has_add_permission(self, request):
        return request.user.is_superuser

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(user=request.user)

    def has_change_permission(self, request, obj=None):
        return obj and obj.user == request.user

    def has_delete_permission(self, request, obj=None):
        return obj and obj.user == request.user


class BandsAdmin(admin.ModelAdmin):
    list_display = ('name', 'country', 'number_of_events')

    def has_add_permission(self, request):
        return request.user.is_superuser


admin.site.register(Event, EventsAdmin)
admin.site.register(Band, BandsAdmin)
admin.site.register(BandEvent)
