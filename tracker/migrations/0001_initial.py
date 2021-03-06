# Generated by Django 4.0.4 on 2022-06-15 14:56

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position_name', models.CharField(max_length=250)),
                ('company_name', models.CharField(max_length=250)),
                ('location', models.CharField(max_length=250)),
                ('date_applied', models.DateTimeField(default=django.utils.timezone.now)),
                ('applied_via', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Interview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('interview_date', models.DateTimeField()),
                ('interviwer', models.CharField(max_length=200)),
                ('type', models.CharField(max_length=200)),
                ('thoughts', models.TextField(blank=True, null=True)),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tracker.job')),
            ],
        ),
    ]
