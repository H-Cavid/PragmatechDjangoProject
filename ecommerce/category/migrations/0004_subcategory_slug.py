# Generated by Django 3.1.6 on 2021-03-01 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0003_subcategory'),
    ]

    operations = [
        migrations.AddField(
            model_name='subcategory',
            name='slug',
            field=models.SlugField(blank=True),
        ),
    ]
