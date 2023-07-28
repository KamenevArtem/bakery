# Generated by Django 4.2.3 on 2023-07-28 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cakeorder', '0002_alter_cake_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.CharField(blank=True, choices=[('Готовится', 'Готовится'), ('Доставляется', 'Доставляется'), ('Доставлен', 'Доставлен')], default='Готовится', max_length=400, verbose_name='Статус заказа'),
        ),
        migrations.AlterField(
            model_name='cake',
            name='name',
            field=models.CharField(blank=True, default='Созданый пользователем', max_length=50, verbose_name='Название'),
        ),
    ]
