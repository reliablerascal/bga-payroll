# Generated by Django 2.0.2 on 2018-06-11 18:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('payroll', '0013_add_employerpopulation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='position',
            name='employer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='positions', to='payroll.Employer'),
        ),
    ]
