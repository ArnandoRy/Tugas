# Generated by Django 4.1.2 on 2022-11-22 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_jenis_barang_jenis_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kelas', models.CharField(max_length=8)),
                ('nama', models.CharField(max_length=50)),
                ('nim', models.IntegerField()),
                ('jurusan', models.CharField(max_length=50)),
                ('waktu_posting', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AlterField(
            model_name='jenis',
            name='nama',
            field=models.CharField(max_length=20),
        ),
    ]
