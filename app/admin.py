from django.contrib import admin
from .models import User,UserPayment

@admin.register(User)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('fullname', 'birthday','profession',"agecategory","city","district","village","date_created")
    search_fields = ("fullname",)

@admin.register(UserPayment)
class PaymentMethodInline(admin.ModelAdmin):
    list_display = ("user","status","date_created",)