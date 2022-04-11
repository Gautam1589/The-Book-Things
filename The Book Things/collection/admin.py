from django.contrib import admin
from .models import Category
from .models import Book_details
# Register your models here.
# admin.site.register(Category)
# admin.site.register(Book_details)
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display=('id','catname')


@admin.register(Book_details)
class Book_detailsAdmin(admin.ModelAdmin):
    list_display=('id','category','name','auther')