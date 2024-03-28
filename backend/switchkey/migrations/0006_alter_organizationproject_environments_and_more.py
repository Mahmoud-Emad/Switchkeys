# Generated by Django 5.0.3 on 2024-03-28 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("switchkey", "0005_alter_organization_members"),
    ]

    operations = [
        migrations.AlterField(
            model_name="organizationproject",
            name="environments",
            field=models.ManyToManyField(
                blank=True,
                related_name="project_environments",
                to="switchkey.projectenvironment",
            ),
        ),
        migrations.AlterField(
            model_name="organizationproject",
            name="groups",
            field=models.ManyToManyField(
                blank=True,
                related_name="project_groups",
                to="switchkey.organizationgroup",
            ),
        ),
    ]
