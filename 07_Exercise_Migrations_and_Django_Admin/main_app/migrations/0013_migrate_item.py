# Generated by Django 4.2.4 on 2023-10-29 14:41

from django.db import migrations


def update_rarity_based_on_price(apps, schema_editor):
    Item = apps.get_model('main_app', 'Item')

    all_items = Item.objects.all()

    for item in all_items:
        if item.price <= 10:
            item.rarity = "Rare"
        elif 11 <= item.price <= 20:
            item.rarity = "Very Rare"
        elif 21 <= item.price <= 30:
            item.rarity = "Extremely Rare"
        else:
            item.rarity = "Mega Rare"

    Item.objects.bulk_update(all_items, ['rarity'])


def reverse_rarity_update(apps, schema_editor):
    Item = apps.get_model('main_app', 'Item')

    all_items = Item.objects.all()

    for item in all_items:
        item.rarity = "empty"

    Item.objects.bulk_update(all_items, ['rarity'])


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0012_item'),
    ]

    operations = [
        migrations.RunPython(update_rarity_based_on_price, reverse_code=reverse_rarity_update),
    ]
