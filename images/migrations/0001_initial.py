# Generated by Django 4.1 on 2023-12-17 21:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Image",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=128)),
                ("slug", models.SlugField(max_length=128)),
                ("description", models.TextField(blank=True)),
                ("url", models.URLField(max_length=2000)),
                ("image", models.ImageField(upload_to="images/%Y/%m/%d/")),
                ("created", models.DateField(auto_now_add=True)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="image_created",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "users_like",
                    models.ManyToManyField(
                        blank=True,
                        related_name="images_liked",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "ordering": ["-created"],
            },
        ),
        migrations.AddIndex(
            model_name="image",
            index=models.Index(
                fields=["-created"], name="images_imag_created_d57897_idx"
            ),
        ),
    ]
