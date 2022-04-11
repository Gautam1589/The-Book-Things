from django.contrib import admin
from .models import Book_rating
# Register your models here.
# @admin.register(Book_rating)
# class Book_ratingAdmin(admin.ModelAdmin):
#     list_display=('id','book_id','rating')

admin.site.register(Book_rating)