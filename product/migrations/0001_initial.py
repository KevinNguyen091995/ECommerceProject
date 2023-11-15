# Generated by Django 4.2.7 on 2023-11-14 18:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('tag', models.CharField(choices=[('el', 'Electronics'), ('cl', 'Clothes'), ('fo', 'Food'), ('ot', 'Other')], default='ot', max_length=2)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.user')),
            ],
        ),
    ]