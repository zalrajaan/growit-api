from django.contrib import admin
from .models import Plant, Accessory, Product, Category, Order,ProductItem, Profile, TrackingHistory

admin.site.register(Profile)
admin.site.register(Plant)
admin.site.register(Accessory) 
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Order)
admin.site.register(ProductItem)
admin.site.register(TrackingHistory)

