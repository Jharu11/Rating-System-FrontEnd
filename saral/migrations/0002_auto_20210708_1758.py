# Generated by Django 3.2.5 on 2021-07-08 12:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('saral', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='new',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='saral.category'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(choices=[('Movie', 'Movie'), ('Show', 'Show'), ('Series', 'Series')], max_length=20),
        ),
    ]
