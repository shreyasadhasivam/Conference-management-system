# Generated by Django 5.0.3 on 2024-03-31 10:33

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(choices=[('chair', 'Chair'), ('author', 'Author'), ('reviewer', 'Reviewer')], max_length=50)),
                ('country_region', models.CharField(max_length=100)),
                ('google_scholar_id', models.CharField(blank=True, max_length=100, null=True)),
                ('semantic_scholar_id', models.CharField(blank=True, max_length=100, null=True)),
                ('dblp_id', models.CharField(blank=True, max_length=100, null=True)),
                ('orcid_id', models.CharField(blank=True, max_length=100, null=True)),
                ('open_review_id', models.CharField(blank=True, max_length=100, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
