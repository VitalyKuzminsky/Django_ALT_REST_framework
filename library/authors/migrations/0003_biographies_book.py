# Generated by Django 3.2.8 on 2023-01-12 18:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authors', '0002_alter_author_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('authors', models.ManyToManyField(to='authors.Author')),
            ],
        ),
        migrations.CreateModel(
            name='Biographies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(blank=True, null=True)),
                ('author', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='authors.author')),
            ],
        ),
    ]
