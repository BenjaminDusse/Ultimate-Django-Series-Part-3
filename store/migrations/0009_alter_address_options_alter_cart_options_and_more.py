# Generated by Django 4.1.2 on 2022-11-14 07:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("store", "0008_alter_promotion_options"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="address",
            options={"verbose_name": "Addresses", "verbose_name_plural": "Address"},
        ),
        migrations.AlterModelOptions(
            name="cart",
            options={"verbose_name": "Carts", "verbose_name_plural": "Cart"},
        ),
        migrations.AlterModelOptions(
            name="cartitem",
            options={"verbose_name": "CartItems", "verbose_name_plural": "CartItem"},
        ),
        migrations.AlterModelOptions(
            name="collection",
            options={
                "verbose_name": "Collections",
                "verbose_name_plural": "Collection",
            },
        ),
        migrations.AlterModelOptions(
            name="customer",
            options={
                "ordering": ["user__first_name", "user__last_name"],
                "permissions": [("view_history", "Can view history")],
                "verbose_name": "Customers",
                "verbose_name_plural": "Customer",
            },
        ),
        migrations.AlterModelOptions(
            name="order",
            options={
                "permissions": [("cancel_order", "Can cancel order")],
                "verbose_name": "Orders",
                "verbose_name_plural": "Order",
            },
        ),
        migrations.AlterModelOptions(
            name="orderitem",
            options={"verbose_name": "OrderItems", "verbose_name_plural": "OrderItem"},
        ),
        migrations.AlterModelOptions(
            name="product",
            options={"verbose_name": "Products", "verbose_name_plural": "Product"},
        ),
        migrations.AlterModelOptions(
            name="review",
            options={"verbose_name": "Reviews", "verbose_name_plural": "Review"},
        ),
    ]