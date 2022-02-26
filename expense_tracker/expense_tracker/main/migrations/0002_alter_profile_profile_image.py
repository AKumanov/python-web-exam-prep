# Generated by Django 4.0.2 on 2022-02-26 19:44

from django.db import migrations, models
import expense_tracker.main.validators


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_image',
            field=models.ImageField(blank=True, default='images/user.png', null=True, upload_to='images/', validators=[expense_tracker.main.validators.MaxFileSizeInMbValidator]),
        ),
    ]
