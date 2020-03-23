# Generated by Django 2.2.7 on 2020-03-23 18:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0003_auto_20200323_1814'),
    ]

    operations = [
        migrations.CreateModel(
            name='Helper',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('telepone', models.IntegerField()),
                ('address', models.CharField(max_length=100)),
                ('payment_type', models.CharField(choices=[('1', 'Fruits'), ('2', 'Vegetables'), ('3', 'Dairy')], max_length=50)),
                ('description', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='nurse',
            name='city',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
    ]
