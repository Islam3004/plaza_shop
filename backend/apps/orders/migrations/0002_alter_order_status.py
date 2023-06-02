# Generated by Django 3.2.9 on 2022-02-10 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.PositiveSmallIntegerField(choices=[('Новый', 1), ('Подтвержден', 2), ('Отправлен', 3), ('Доставлен', 4), ('Архивирован', 5)], db_index=True, default=1, verbose_name='Статус'),
        ),
    ]
