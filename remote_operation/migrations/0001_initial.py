# Generated by Django 2.1.1 on 2019-07-25 02:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(default=0, max_length=50, verbose_name='设备所属类别')),
                ('ip_port', models.CharField(default=0, max_length=20, verbose_name='ip_port')),
                ('status', models.CharField(default=0, max_length=20, verbose_name='状态')),
                ('number', models.CharField(default=0, max_length=20, verbose_name='设备号')),
            ],
            options={
                'verbose_name': '设备信息',
                'verbose_name_plural': '设备信息',
                'db_table': 'device',
            },
        ),
    ]
