# Generated by Django 5.0.3 on 2024-03-28 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("switchkey", "0012_rename_projectenvironmentfeaturestorage_featurestorage"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="featurestorage",
            options={
                "verbose_name": "Feature Storage",
                "verbose_name_plural": "Features Storage",
            },
        ),
        migrations.AddField(
            model_name="organizationgroup",
            name="project",
            field=models.ManyToManyField(
                blank=True,
                related_name="project_groups",
                to="switchkey.organizationproject",
            ),
        ),
        migrations.AlterField(
            model_name="projectenvironmentuser",
            name="features",
            field=models.JSONField(blank=True, default=dict),
        ),
    ]