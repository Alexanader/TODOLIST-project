# Generated by Django 2.0.7 on 2019-02-10 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Plan', '0003_auto_20190207_1624'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plantodo',
            name='description',
            field=models.TextField(),
        ),
    ]