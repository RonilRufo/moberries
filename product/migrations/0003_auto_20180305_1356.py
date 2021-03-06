# Generated by Django 2.0.2 on 2018-03-05 13:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_remove_pizza_sizes'),
    ]

    operations = [
        migrations.CreateModel(
            name='PizzaVariation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=7)),
                ('pizza', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='variations', to='product.Pizza')),
                ('size', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='pizza_variations', to='product.PizzaSize')),
            ],
            options={
                'verbose_name': 'Pizza Variation',
                'verbose_name_plural': 'Pizza Variations',
            },
        ),
        migrations.AlterUniqueTogether(
            name='pizzavariation',
            unique_together={('pizza', 'size')},
        ),
    ]
