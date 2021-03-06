# Generated by Django 2.1.1 on 2018-10-01 18:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=120)),
                ('img', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='PlantCycle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plant_height_cm', models.IntegerField()),
                ('plant_height_days', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('description', models.TextField()),
                ('price', models.IntegerField()),
                ('img', models.ImageField(upload_to='')),
                ('quantity', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ProductItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backendapp.Order')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.IntegerField()),
                ('city', models.CharField(max_length=120)),
                ('block', models.IntegerField(blank=True, null=True)),
                ('street', models.CharField(max_length=120)),
                ('avenue', models.IntegerField(blank=True, null=True)),
                ('house_number', models.IntegerField()),
                ('apt_number', models.IntegerField(blank=True, null=True)),
                ('del_instructions', models.CharField(max_length=120)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Stage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('days', models.IntegerField()),
                ('description', models.CharField(max_length=120)),
                ('details', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='TrackingHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('planted_on', models.DateField(auto_now_add=True)),
                ('active', models.BooleanField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Accessory',
            fields=[
                ('product_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='backendapp.Product')),
            ],
            bases=('backendapp.product',),
        ),
        migrations.CreateModel(
            name='Plant',
            fields=[
                ('product_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='backendapp.Product')),
                ('scientific_name', models.CharField(max_length=120)),
                ('location', models.TextField()),
                ('watering_frequency', models.IntegerField()),
                ('fertilizing_frequency', models.IntegerField()),
                ('date_created', models.DateField(auto_now_add=True)),
                ('color', models.CharField(max_length=120)),
                ('care_level', models.CharField(choices=[('easy', 'easy'), ('moderate', 'moderate'), ('expert', 'expert')], max_length=120)),
                ('lighting', models.CharField(choices=[('dim', 'dim'), ('moderate', 'moderate'), ('bright', 'bright')], max_length=120)),
                ('pet_friendly', models.BooleanField()),
                ('size', models.CharField(choices=[('desktop', 'desktop'), ('ground', 'ground'), ('tall', 'tall')], max_length=120)),
                ('theme', models.CharField(max_length=120)),
                ('season', models.CharField(choices=[('summer', 'summer'), ('fall', 'fall'), ('spring', 'spring'), ('winter', 'winter')], max_length=120)),
                ('stage_1day', models.IntegerField(default=1)),
                ('stage_2day', models.IntegerField(default=1)),
                ('stage_3day', models.IntegerField(default=1)),
                ('stage_1des', models.CharField(default='a', max_length=120)),
                ('stage_2des', models.CharField(default='a', max_length=120)),
                ('stage_3des', models.CharField(default='a', max_length=120)),
                ('stage_1det', models.TextField(default='a')),
                ('stage_2det', models.TextField(default='a')),
                ('stage_3det', models.TextField(default='a')),
                ('stage_4det', models.TextField(default='a')),
                ('tracking_code', models.TextField(default='a')),
            ],
            bases=('backendapp.product',),
        ),
        migrations.AddField(
            model_name='productitem',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backendapp.Product'),
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backendapp.Category'),
        ),
        migrations.AddField(
            model_name='order',
            name='items',
            field=models.ManyToManyField(through='backendapp.ProductItem', to='backendapp.Product'),
        ),
        migrations.AddField(
            model_name='order',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='trackinghistory',
            name='plant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backendapp.Plant'),
        ),
    ]
