# Generated by Django 2.1.1 on 2018-09-30 16:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('backendapp', '0002_auto_20180925_1800'),
    ]

    operations = [
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
        migrations.AddField(
            model_name='category',
            name='img',
            field=models.ImageField(default=1, upload_to=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='plant',
            name='stage_1day',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='plant',
            name='stage_1des',
            field=models.CharField(default='a', max_length=120),
        ),
        migrations.AddField(
            model_name='plant',
            name='stage_1det',
            field=models.TextField(default='a'),
        ),
        migrations.AddField(
            model_name='plant',
            name='stage_2day',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='plant',
            name='stage_2des',
            field=models.CharField(default='a', max_length=120),
        ),
        migrations.AddField(
            model_name='plant',
            name='stage_2det',
            field=models.TextField(default='a'),
        ),
        migrations.AddField(
            model_name='plant',
            name='stage_3day',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='plant',
            name='stage_3des',
            field=models.CharField(default='a', max_length=120),
        ),
        migrations.AddField(
            model_name='plant',
            name='stage_3det',
            field=models.TextField(default='a'),
        ),
        migrations.AddField(
            model_name='plant',
            name='stage_4det',
            field=models.TextField(default='a'),
        ),
    ]