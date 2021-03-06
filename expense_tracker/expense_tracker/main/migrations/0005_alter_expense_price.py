# Generated by Django 4.0.2 on 2022-02-26 20:39

from django.db import migrations, models
import expense_tracker.main.validators


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_expense_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='price',
            field=models.FloatField(validators=[expense_tracker.main.validators.positive_num_validator]),
        ),
    ]
