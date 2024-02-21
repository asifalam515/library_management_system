# Generated by Django 5.0 on 2024-02-20 04:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_useraccount_balance'),
        ('books', '0003_alter_book_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='book',
        ),
        migrations.RemoveField(
            model_name='review',
            name='user',
        ),
        migrations.AddField(
            model_name='review',
            name='borrowed_book',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='books.borrowedbook'),
        ),
        migrations.AddField(
            model_name='review',
            name='user_account',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='accounts.useraccount'),
        ),
        migrations.AlterField(
            model_name='review',
            name='comment',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='review',
            name='rating',
            field=models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)]),
        ),
    ]