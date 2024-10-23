# Generated by Django 5.1.1 on 2024-10-03 13:35

import django.contrib.auth.models
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('clientinfo', '0002_initial'),
        ('inventory', '0002_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='userCustomPermission',
            fields=[
                ('permission_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='auth.permission')),
            ],
            options={
                'verbose_name': 'Custom Permission',
                'verbose_name_plural': 'Custom Permissions',
            },
            bases=('auth.permission',),
            managers=[
                ('objects', django.contrib.auth.models.PermissionManager()),
            ],
        ),
        migrations.CreateModel(
            name='CustomGroup',
            fields=[
                ('group_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='auth.group')),
                ('label', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=2500)),
                ('custom_permissions', models.ManyToManyField(blank=True, to='auth.permission')),
                ('store', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mes_groupes', to='clientinfo.store')),
            ],
            bases=('auth.group',),
            managers=[
                ('objects', django.contrib.auth.models.GroupManager()),
            ],
        ),
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('role', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('adresse_ip', models.GenericIPAddressField(blank=True, default='127.0.0.1', null=True)),
                ('EmployeeAt', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mes_employees', to='clientinfo.store')),
                ('entrepots_responsible', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='responsables', to='inventory.entrepot')),
                ('group', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='group_user', to='user.customgroup')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'user',
                'abstract': False,
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='cordinates',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.CharField(blank=True, default='', max_length=250, null=True)),
                ('longitude', models.CharField(blank=True, default='', max_length=250, null=True)),
                ('User', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mycoordinates', to='user.customuser')),
            ],
        ),
        migrations.CreateModel(
            name='Equipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(blank=True, default='', max_length=250, null=True)),
                ('date_created', models.DateTimeField()),
                ('store', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mes_equipes', to='clientinfo.store')),
            ],
        ),
        migrations.AddField(
            model_name='customuser',
            name='equipe_affiliated',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='mes_membres', to='user.equipe'),
        ),
        migrations.CreateModel(
            name='MyLogEntry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='myacts', to='user.customuser')),
                ('store', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ma_tracabilte', to='clientinfo.store')),
            ],
            options={
                'ordering': ['-timestamp'],
            },
        ),
    ]