# Generated by Django 2.2.6 on 2019-11-05 00:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0007_auto_20191104_1332'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meal',
            name='drink_choice',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='restaurant.Beverage'),
        ),
        migrations.AlterField(
            model_name='meal',
            name='feedback',
            field=models.TextField(default='average', max_length=1000),
        ),
        migrations.AlterField(
            model_name='meal',
            name='food_choice',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='restaurant.Food'),
        ),
        migrations.AlterField(
            model_name='meal',
            name='meal_owner',
            field=models.CharField(default='a Pyfood customer:2019-11-05T00:56:05.712644', max_length=100),
        ),
        migrations.AlterField(
            model_name='meal',
            name='pub_date',
            field=models.DateTimeField(default='2019-11-05T00:56:05.712644', verbose_name='date published'),
        ),
        migrations.AlterField(
            model_name='meal',
            name='total_cost',
            field=models.DecimalField(decimal_places=2, default=3.0, max_digits=4),
        ),
    ]