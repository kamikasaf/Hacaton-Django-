# Generated by Django 4.0.5 on 2022-06-06 11:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(max_length=13)),
                ('address', models.TextField()),
                ('email', models.EmailField(max_length=254)),
                ('pay_choices', models.CharField(choices=[('cash', 'Наличными'), ('card', 'Оплата картой'), ('debt', 'В долг')], max_length=15)),
                ('order_comments', models.TextField(blank=True, null=True)),
                ('shopping_cart', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='order', to='cart.shoppingcart')),
            ],
        ),
    ]
