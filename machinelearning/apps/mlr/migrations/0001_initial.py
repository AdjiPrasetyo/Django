# Generated by Django 3.1.6 on 2021-02-20 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dataset',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('luas_lahan', models.IntegerField()),
                ('jumlah_pokok', models.IntegerField()),
                ('jumlah_tbs', models.IntegerField()),
                ('umur', models.IntegerField()),
                ('hasil_produksi', models.IntegerField()),
            ],
        ),
    ]
