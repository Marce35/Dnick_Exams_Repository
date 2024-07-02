from django.contrib import admin

from ListingsApp.models import Category, Listing


# Register your models here.

class ListingsAdmin(admin.ModelAdmin):
    exclude = ['user',]
    list_display = ['title', 'category', 'price']
    list_filter = ['category']
    ordering = ['price']

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.user = request.user

        return super(ListingsAdmin, self).save_model(request, obj, form, change)

    def has_add_permission(self, request):
        return request.user.is_superuser

    def has_change_permission(self, request, obj=None):
        return obj and obj.user == request.user

    def has_delete_permission(self, request, obj=None):
        return obj and obj.user == request.user


class CategoryAdmin(admin.ModelAdmin):

    def has_add_permission(self, request):
        return request.user.is_superuser


admin.site.register(Category, CategoryAdmin)
admin.site.register(Listing, ListingsAdmin)
