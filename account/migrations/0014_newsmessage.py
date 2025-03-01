# Generated by Django 5.1.3 on 2025-01-14 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0013_usersession'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewsMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='عنوان')),
                ('date', models.DateField(auto_now_add=True, verbose_name='تاریخ ایجاد')),
                ('body', models.TextField(verbose_name='متن پیام')),
                ('detail_link', models.URLField(blank=True, null=True, verbose_name='لینک جزئیات')),
            ],
            options={
                'verbose_name': 'پیام خبری',
                'verbose_name_plural': 'پیام\u200cهای خبری',
            },
        ),
    ]
