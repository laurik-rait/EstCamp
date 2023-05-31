# Generated by Django 4.2.1 on 2023-05-31 08:40

from django.db import migrations, models
import precise_bbcode.fields


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='_text_rendered',
            field=models.TextField(blank=True, editable=False, null=True),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='text',
            field=precise_bbcode.fields.BBCodeTextField(no_rendered_field=True),
        ),
    ]
