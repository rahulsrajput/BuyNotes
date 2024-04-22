from django.contrib import admin
from .models import Orders, Payment

# Register your models here.
@admin.register(Orders)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['uuid', 'complete', 'customer', 'product','created_at','updated_at']

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ['order','is_paid','status','amount','instamojo_id','payment_id']