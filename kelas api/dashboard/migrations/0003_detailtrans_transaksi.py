# Generated by Django 4.1.2 on 2022-10-25 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_barang_waktu_posting_alter_barang_kodebrg'),
    ]

    operations = [
        migrations.CreateModel(
            name='Detailtrans',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kodetrans', models.CharField(max_length=10)),
                ('kodebrg', models.CharField(max_length=8)),
                ('qty', models.IntegerField()),
                ('subtotal', models.BigIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Transaksi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kodetrans', models.CharField(max_length=10)),
                ('tggltrans', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]