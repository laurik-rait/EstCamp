# Generated by Django 4.2.1 on 2023-05-31 06:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TicketType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('limit', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owner_name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('issue_date', models.DateTimeField(auto_now_add=True, verbose_name='issued at')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tickets.tickettype')),
            ],
        ),
    ]