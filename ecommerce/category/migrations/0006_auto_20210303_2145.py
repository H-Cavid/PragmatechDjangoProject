# Generated by Django 3.1.5 on 2021-03-03 17:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0005_auto_20210302_1133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subcategory',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sub_categories', to='category.category'),
        ),
    ]