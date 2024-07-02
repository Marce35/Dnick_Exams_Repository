from django.contrib import admin

from BooksApp.models import Author, Book, AuthorBook


# Register your models here.

class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name', 'age']
    exclude = ('user',)

    def has_add_permission(self, request):
        return request.user.is_superuser

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.user = request.user

        return super(AuthorAdmin, self).save_model(request, obj, form, change)


class BookAdminInline(admin.StackedInline):
    model = AuthorBook
    extra = 0


class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'pub_date', 'authors']
    search_fields = ['description', ]
    inlines = [BookAdminInline, ]
    exclude = ['authors']

    def has_add_permission(self, request):
        return Author.objects.filter(user=request.user).exists()

    def has_change_permission(self, request, obj=None):
        return Author.objects.filter(user=request.user).exists()

    def save_model(self, request, obj, form, change):
        super(BookAdmin, self).save_model(request, obj, form, change)

        author_books = AuthorBook.objects.filter(book=obj)

        author_names = ', '.join([an.author.name for an in author_books])

        obj.authors = author_names

        obj.save()

    def get_queryset(self, request):
        qs = super(BookAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(authors__user=request.user)


admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(AuthorBook)
