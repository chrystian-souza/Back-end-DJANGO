# Generated by Django 4.2.5 on 2023-10-25 23:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stockADS', '0003_alter_categorias_options_alter_products_options_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='products',
            old_name='caregory',
            new_name='category',
        ),
    ]