# Generated by Django 5.0 on 2024-02-19 01:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_useraccount_balance'),
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='user_reviews',
        ),
        migrations.CreateModel(
            name='BorrowedBook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('borrowing_date', models.DateField(auto_now_add=True)),
                ('is_returned', models.BooleanField(default=False)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.book')),
                ('user_account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='borrowed_books', to='accounts.useraccount')),
            ],
        ),
        migrations.CreateModel(
            name='ReturnTransaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('return_date', models.DateField(auto_now_add=True)),
                ('returned_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('borrowed_book', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='return_transaction', to='books.borrowedbook')),
            ],
        ),
    ]
