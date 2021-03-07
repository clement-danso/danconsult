# Generated by Django 2.1 on 2021-03-02 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0005_quoterequest'),
    ]

    operations = [
        migrations.CreateModel(
            name='products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('product_description', models.CharField(max_length=200)),
                ('product_picture', models.ImageField(upload_to='Products/')),
                ('product_price', models.CharField(max_length=50)),
                ('product_url', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': 'Products',
            },
        ),
    ]
