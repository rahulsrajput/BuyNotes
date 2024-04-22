from django.db import models
import uuid
from products.models import Products
from app.models import Customer

# Create your models here.
class BaseModel(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, null=False, blank=False, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Orders(BaseModel):
    product = models.ForeignKey(Products, on_delete=models.SET_NULL, null=True)
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    complete = models.BooleanField(default=False)


class Payment(BaseModel):
    order = models.OneToOneField(Orders, on_delete=models.SET_NULL, null=True)
    is_paid = models.BooleanField(default=False)
    instamojo_id = models.CharField(max_length=100, null=True, blank=True, unique=True)
    payment_id = models.CharField(max_length=100, null=True, blank=True, unique=True)
    status = models.CharField(max_length=100, null=True, blank=True)
    amount = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)