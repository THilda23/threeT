# Generated by Django 4.2.7 on 2023-11-27 04:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('threeT', '0005_type_info1_type_info2_type_info3'),
    ]

    operations = [
        migrations.AddField(
            model_name='type',
            name='nick',
            field=models.CharField(default='nick', max_length=100),
        ),
    ]