# Generated by Django 2.2.4 on 2019-08-29 01:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('report', '0002_auto_20190828_0750'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReportResponse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=255)),
                ('author', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('report', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='report.Report')),
            ],
        ),
    ]
