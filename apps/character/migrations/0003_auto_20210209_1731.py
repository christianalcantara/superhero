# Generated by Django 3.1.6 on 2021-02-09 17:31

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("character", "0002_auto_20210209_1722"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="character",
            options={
                "ordering": ("created",),
                "verbose_name": "Character",
                "verbose_name_plural": "Characters",
            },
        ),
        migrations.AlterField(
            model_name="character",
            name="name",
            field=models.CharField(
                db_index=True, max_length=100, unique=True, verbose_name="Name"
            ),
        ),
    ]
