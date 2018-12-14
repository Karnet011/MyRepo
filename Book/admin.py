from django.contrib import admin
from Book.models import Author,Book

class AuthorInLine(admin.StackedInline):
    model=Book
    extra= 1
class AuthorAdmin(admin.ModelAdmin):
    inlines = [AuthorInLine]
    list_filter = ['name']

admin.site.register(Author,AuthorAdmin)

# Register your models here.
