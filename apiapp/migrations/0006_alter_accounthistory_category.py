# Generated by Django 3.2.7 on 2021-12-15 14:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('apiapp', '0005_accounthistory_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accounthistory',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='category', to='apiapp.category'),
        ),
    ]