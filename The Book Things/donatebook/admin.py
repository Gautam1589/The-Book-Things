from django.contrib import admin
from .models import BookDonation
# Register your models here.
@admin.register(BookDonation)
class BookDonationAdmin(admin.ModelAdmin):
    list_display=('id','name','email')