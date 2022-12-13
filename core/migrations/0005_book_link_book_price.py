# Generated by Django 4.1.3 on 2022-12-01 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0004_rename_cod_book_review_book_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="book",
            name="link",
            field=models.CharField(default=None, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name="book",
            name="price",
            field=models.FloatField(default=None, null=True),
        ),
    ]