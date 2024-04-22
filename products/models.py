from django.db import models
import uuid
# Create your models here.

class BaseModel(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Category(BaseModel):
    name = models.CharField(max_length=100, unique=True)
    
    def __str__(self):
        return self.name


class Products(BaseModel):
    category = models.ManyToManyField(Category)
    name = models.CharField(max_length=300, unique=True, null=False, blank=False)
    price = models.DecimalField(max_digits=7, blank=False, null=False, decimal_places=2)
    discount = models.DecimalField(max_digits=2, decimal_places=0, null=True , blank=True)
    image = models.ImageField(null=False, blank=False, upload_to='media/03_BuyNotes')
    file = models.FileField(null=True, blank=True , upload_to='files/03_BuyNotes')