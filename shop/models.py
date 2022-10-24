from tokenize import blank_re
from django.db import models

# Create your models here.
class ProductSize(models.Model):
    name = models.CharField(max_length=250,verbose_name="O'lcham")
    def __str__(self):
        return  self.name
    class Meta():
        verbose_name = "Mahsulot o'lchami"
        verbose_name_plural = "Mahsulot o'lchamlari"


class ProductState(models.Model):
    name = models.CharField(max_length=250,verbose_name="Davlat nomi")
    def __str__(self):
        return  self.name
    class Meta():
        verbose_name = "Mahsulot ishlab chiqarilgan davlat"
        verbose_name_plural = "Mahsulot ishlab chiqarilgan davlatlar"
class ProductColor(models.Model):
    name = models.CharField(max_length=250,verbose_name="Rang nomi")
    color = models.CharField(max_length=100,null=True,blank=True)
    def __str__(self):
        return  self.name
    class Meta():
        verbose_name = "Mahsulot rangi"
        verbose_name_plural = "Mahsulot ranglari"


class Product(models.Model):
    image1 = models.ImageField(upload_to="products/images/%Y/%m/%d",blank=True,null=True,verbose_name="Rasm 1",editable=True)
    image2 = models.ImageField(upload_to="products/images/%Y/%m/%d",blank=True,null=True,verbose_name="Rasm 2",editable=True)
    image3 = models.ImageField(upload_to="products/images/%Y/%m/%d",blank=True,null=True,verbose_name="Rasm 3",editable=True)
    video = models.FileField(upload_to="products/video/%Y/%m/%d",blank=True,null=True,verbose_name="Video fayl",editable=True)
    name = models.CharField(max_length=250,verbose_name="Nomi")
    price = models.IntegerField(verbose_name="Narxi")
    discount = models.PositiveSmallIntegerField(verbose_name="Chegirma",null=True,blank=True)
    content = models.TextField(blank=True,null=True,verbose_name="Qisqacha tovar haqida")
    state = models.ForeignKey(ProductState,on_delete=models.CASCADE,verbose_name="Davlat")
    sizes = models.ManyToManyField(ProductSize,verbose_name="O'lchamlar")
    colors = models.ManyToManyField(ProductColor,verbose_name="Ranglar")
    slug = models.SlugField(unique=True)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    class Meta():
        verbose_name = "Mahsulot"
        verbose_name_plural = "Mahsulotlar"
    def new_price(self):
        if self.discount:
            return int(self.price*(100-self.discount)/100)
    def __str__(self):
        return  self.name

class PaymentType(models.Model):
    name = models.CharField(max_length=250,verbose_name="To'lov turi nomi")

    def __str__(self):
        return self.name

    class Meta():
        verbose_name = "To'lov turi"
        verbose_name_plural = "To'lov turlari"

class Orders(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE,verbose_name="Mahsulot")
    color = models.ForeignKey(ProductColor,on_delete=models.CASCADE,verbose_name="Mahsulot rangi")
    size = models.ForeignKey(ProductSize,on_delete=models.CASCADE,verbose_name="Mahsulot O'lchami")
    full_name = models.CharField(max_length=250,verbose_name="Buyurtmachi ismi")
    phone_number = models.CharField(max_length=100,verbose_name="Buyurtmachi telefon raqami")
    address = models.CharField(max_length=200,verbose_name="Buyurtmachi manzili")
    payment_type = models.ForeignKey(PaymentType,on_delete=models.CASCADE,verbose_name="Buyurtma to'lov turi")
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    is_done = models.BooleanField(default=False,verbose_name="Buyurtma yetkazildi")
    is_canceled = models.BooleanField(default=False,verbose_name="Buyurtma bekor qilindi")
    def __str__(self):
        return self.full_name + str(self.product.name)
    class Meta():
        verbose_name = "Buyurtma"
        verbose_name_plural = "Buyurtmalar"


class SocialLink(models.Model):
    name = models.CharField(max_length=250,verbose_name="Ijtimoiy tarmoq nomi")
    url = models.URLField(verbose_name="Ijtimoiy tarmoq manzili(url)")
    icon = models.CharField(max_length=250,null=True)
    def __str__(self):
        return self.name
    class Meta():
        verbose_name = "Ijtimoiy tarmoq"
        verbose_name_plural = "Ijtimoiy tarmoqlar"

