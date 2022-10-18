from django.contrib import admin
from .models import *
# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ["id","name","price","discount","content","slug"]
    list_display_links = ('id',"name")
    prepopulated_fields = {'slug':('name',),}
admin.site.register(Product,ProductAdmin)
admin.site.register(ProductSize)
admin.site.register(ProductColor)
admin.site.register(ProductState)
admin.site.register(PaymentType)
admin.site.register(SocialLink)
class OrsersAdmin(admin.ModelAdmin):
    list_display = ["id","product","full_name","phone_number","address","payment_type"]
    list_display_links = ("id","product","full_name")
admin.site.register(Orders,OrsersAdmin)




