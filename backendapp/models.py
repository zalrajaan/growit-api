from django.db import models
from django.contrib.auth.models import User



class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    phone_number = models.IntegerField()
    city = models.CharField(max_length=120)
    block = models.IntegerField(blank = True, null = True)
    street = models.CharField(max_length=120)
    avenue = models.IntegerField(blank = True, null = True)
    house_number = models.IntegerField()
    apt_number = models.IntegerField(blank = True, null = True)
    del_instructions = models.CharField(max_length=120)
    
    def __str__(self):
        return str(self.user)


care_level_choices = (
        ('easy', 'easy'),
        ('moderate', 'moderate'),
        ('expert', 'expert'),
    )
lighting_level = (
        ('dim', 'dim'),
        ('moderate', 'moderate'),
        ('bright', 'bright'),
    )
season_type = (

        ('summer', 'summer'),
        ('fall', 'fall'),
        ('spring', 'spring'),
        ('winter', 'winter'),

    )
sizechoices = (

        ('desktop', 'desktop'),
        ('ground', 'ground'),
        ('tall', 'tall'),

    )
#-*- coding: utf-8 -*-

care_level_choices_ar = (
        ('سهل', 'سهل'),
        ('متوسط', 'متوسط'),
        ('متقدم', 'متقدم'),
    )
lighting_level_ar = (
        ('قليل', 'قليل'),
        ('متوسط', 'متوسط'),
        ('قوي', 'قوي'),
    )
season_type_ar = (

        ('صيف', 'صيف'),
        ('خريف', 'خريف'),
        ('ربيع', 'ربيع'),
        ('شتاء', 'شتاء'),

    )
sizechoices_ar = (

        ('سطح المكتب', 'سطح المكتب'),
        ('ارضي', 'ارضي'),
        ('طويل', 'طويل'),

    )

class Category(models.Model):
    category= models.CharField(max_length=120)
    category_ar= models.CharField(max_length=120, default="a")
    img = models.ImageField()


    def __str__(self):
        return self.category

class Product(models.Model):
    name = models.CharField(max_length=120)
    name_ar = models.CharField(max_length=120, default="a")
    description = models.TextField()
    description_ar = models.TextField(default="a")
    price = models.IntegerField()
    img = models.ImageField()
    quantity = models.IntegerField()
    category= models.ForeignKey(Category, on_delete=models.CASCADE)
    #category_ar= models.ForeignKey(Category, on_delete=models.CASCADE) check with hamza

    
    def __str__(self):
        return self.name

class Plant(Product):
    scientific_name = models.CharField(max_length=120)
    location = models.TextField()
    watering_frequency = models.IntegerField()
    fertilizing_frequency = models.IntegerField()
    date_created = models.DateField(auto_now_add=True)
    color = models.CharField(max_length=120)
    care_level = models.CharField(max_length=120, choices= care_level_choices)
    lighting = models.CharField(max_length=120, choices= lighting_level)
    pet_friendly = models.BooleanField()
    size = models.CharField(max_length=120, choices= sizechoices)
    theme = models.CharField(max_length=120)
    season = models.CharField(max_length=120, choices= season_type)
    stage_1day = models.IntegerField(default=1)
    stage_2day = models.IntegerField(default=1)
    stage_3day = models.IntegerField(default=1)
    stage_1des = models.CharField(max_length=120, default="a")
    stage_2des = models.CharField(max_length=120, default="a")
    stage_3des = models.CharField(max_length=120, default="a")
    stage_1det = models.TextField(default="a")
    stage_2det = models.TextField(default="a")
    stage_3det = models.TextField(default="a")
    stage_4det = models.TextField(default="a")
    stage_1des_ar = models.CharField(max_length=120, default="a")
    stage_2des_ar = models.CharField(max_length=120, default="a")
    stage_3des_ar = models.CharField(max_length=120, default="a")
    stage_1det_ar = models.TextField(default="a")
    stage_2det_ar = models.TextField(default="a")
    stage_3det_ar = models.TextField(default="a")
    stage_4det_ar = models.TextField(default="a")
    tracking_code = models.TextField(default="a")
    lighting_frequency = models.IntegerField(default=1)
    scientific_name_ar = models.CharField(max_length=120, default="a")
    color_ar = models.CharField(max_length=120, default=[1])
    care_level_ar = models.CharField(max_length=120, choices= care_level_choices_ar, default=care_level_choices_ar[1])
    lighting_ar = models.CharField(max_length=120, choices= lighting_level_ar, default=lighting_level_ar[1])
    size_ar = models.CharField(max_length=120, choices= sizechoices_ar, default=sizechoices_ar[1])
    season_ar = models.CharField(max_length=120, choices= season_type_ar, default=season_type_ar[1])


    def __str__(self):
        return self.name

class Accessory(Product):
    
    def __str__(self):
        return self.name


# class Stage(models.Model):
#     days = models.IntegerField()
#     description = models.CharField(max_length=120)
#     details = models.TextField()

#     def __str__(self):
#         return self.days

class PlantCycle(models.Model):
    plant_height_cm = models.IntegerField()
    plant_height_days = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.plant_height_cm

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(Product, through ='ProductItem')
    date_created = models.DateField(auto_now_add=True)
    # total_price = models.DecimalField(max_digits=10, decimal_places=3)

    # def calculate_order_price(self):
    #     self.total_price = 0
    #     for item in self.items:
    #         self.total_price += item.price
    #     items.save()

    def __str__(self):
        return self.user.username + "order: " + str(self.id)

class ProductItem(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE )
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return str(self.order)

class TrackingHistory(models.Model):

    planted_on = models.DateField(auto_now_add=True)
    active = models.BooleanField()
    plant = models.ForeignKey(Plant,on_delete=models.CASCADE )
    user = models.ForeignKey(User,on_delete=models.CASCADE )

    def __str__(self):
        return str(self.plant)

class PlantHeight(models.Model):

    days = models.DateField(auto_now_add=True)
    active = models.BooleanField()
    height = models.DecimalField(max_digits=10, decimal_places=2)
    track = models.ForeignKey(TrackingHistory,on_delete=models.CASCADE )

    def __str__(self):
        return "%s %s %s" %(self.id, self.track.id, self.track.plant.name)