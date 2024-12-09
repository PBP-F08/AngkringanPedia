# Generated by Django 5.1.2 on 2024-10-24 10:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodcatalog', '0002_remove_rating_user_remove_review_user'),
        ('main', '0002_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='recipe',
        ),
        migrations.CreateModel(
            name='RatingReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.PositiveIntegerField(blank=True, null=True)),
                ('content', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ratings_reviews', to='main.recipe')),
            ],
        ),
        migrations.DeleteModel(
            name='Rating',
        ),
        migrations.DeleteModel(
            name='Review',
        ),
    ]