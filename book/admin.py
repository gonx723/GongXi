from django.contrib import admin
from .models import Book,Book_Review
# Register your models here.

class BookAdmin(admin.ModelAdmin):
    list_display = ('title','description')
    search_fields = ['title','description']
    list_editable = ('description',)

admin.site.register(Book,BookAdmin)
admin.site.register(Book_Review)