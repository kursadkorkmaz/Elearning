# Generated by Django 3.2 on 2021-05-01 07:11

from django.db import migrations
import embed_video.fields


class Migration(migrations.Migration):

    dependencies = [
        ('elearn', '0010_tutorial_course'),
    ]

    operations = [
        migrations.AddField(
            model_name='tutorial',
            name='video',
            field=embed_video.fields.EmbedVideoField(blank=True, null=True),
        ),
    ]
