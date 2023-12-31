# Generated by Django 4.2.4 on 2023-09-19 11:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('movie', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_price', models.FloatField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='TicketType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.FloatField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.FloatField(default=0)),
                ('payment_methods', models.IntegerField(choices=[(1, 'Bank-card'), (2, 'Balance.kg'), (3, 'Mbank')], default=1)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tickets.order')),
                ('seat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movie.seat')),
                ('show_time', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movie.showtime')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tickets.tickettype')),
            ],
        ),
    ]
