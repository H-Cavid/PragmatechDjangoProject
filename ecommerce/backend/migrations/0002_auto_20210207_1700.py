# Generated by Django 3.1.6 on 2021-02-07 13:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='is_phone_status',
            field=models.BooleanField(default=False),
        ),
        migrations.CreateModel(
            name='UserOtp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('otp', models.CharField(max_length=6)),
                ('rpt', models.IntegerField(default=3)),
                ('date', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_otp', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]