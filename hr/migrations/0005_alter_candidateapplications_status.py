# Generated by Django 5.0.3 on 2024-03-22 04:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hr', '0004_alter_selectcandidatejob_candidate_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidateapplications',
            name='status',
            field=models.CharField(choices=[('pandding', 'pandding'), ('selected', 'selected')], default='pending', max_length=20),
        ),
    ]
