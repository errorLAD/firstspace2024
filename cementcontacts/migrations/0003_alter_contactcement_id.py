# Generated by Django 4.2 on 2024-08-19 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cementcontacts', '0002_auto_20230505_2028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactcement',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]