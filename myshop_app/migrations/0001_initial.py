# Generated by Django 4.0.1 on 2022-01-06 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('specs', models.TextField(max_length=1000)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]