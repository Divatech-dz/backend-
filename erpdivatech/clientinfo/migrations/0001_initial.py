# Generated by Django 5.1.1 on 2024-10-03 13:35

import django.contrib.auth.models
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='clientinfoCustomPermission',
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
            name='CompteEntreprise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nature', models.CharField(choices=[('Caisse', 'Caisse'), ('Banque', 'Banque'), ('CCP', 'CCP'), ('Autres', 'Autres')], max_length=30)),
                ('label', models.CharField(blank=True, default='', max_length=2500, null=True)),
                ('numCompte', models.CharField(blank=True, default='', max_length=2500, null=True)),
                ('journal', models.CharField(blank=True, default='', max_length=2500, null=True)),
                ('monnaie', models.CharField(blank=True, default='', max_length=2500, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Devise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reference', models.CharField(blank=True, default='', max_length=2500, null=True)),
                ('designation', models.CharField(blank=True, default='', max_length=2500, null=True)),
                ('symbole', models.CharField(blank=True, default='', max_length=2500, null=True)),
                ('actif', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Journal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(blank=True, default='', max_length=2500, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PlanComptableAccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='PlanComptableClass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='store',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('location', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('code', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('nAdherent', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('denomination', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('raisonSocial', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('address1', models.CharField(blank=True, default='', max_length=300, null=True)),
                ('address2', models.CharField(blank=True, default='', max_length=300, null=True)),
                ('address3', models.CharField(blank=True, default='', max_length=300, null=True)),
                ('CodePostal', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('phone1', models.CharField(blank=True, default='', max_length=30, null=True)),
                ('phone2', models.CharField(blank=True, default='', max_length=30, null=True)),
                ('phone3', models.CharField(blank=True, default='', max_length=30, null=True)),
                ('fax1', models.CharField(blank=True, default='', max_length=30, null=True)),
                ('fax2', models.CharField(blank=True, default='', max_length=30, null=True)),
                ('fax3', models.CharField(blank=True, default='', max_length=30, null=True)),
                ('mobile1', models.CharField(blank=True, default='', max_length=30, null=True)),
                ('mobile2', models.CharField(blank=True, default='', max_length=30, null=True)),
                ('mobile3', models.CharField(blank=True, default='', max_length=30, null=True)),
                ('monnaie', models.CharField(blank=True, default='', max_length=10, null=True)),
                ('IdentificationFis', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('registreCom', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('articleImpo', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('identifiantStatistique', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('banque', models.CharField(blank=True, default='', max_length=250, null=True)),
                ('compteBancaire', models.CharField(blank=True, default='', max_length=250, null=True)),
                ('compteCCP', models.CharField(blank=True, default='', max_length=250, null=True)),
                ('capitaleSocial', models.CharField(blank=True, default='', max_length=250, null=True)),
                ('product_variant', models.BooleanField(blank=True, default=False, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Taxes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('libelle', models.CharField(blank=True, default='', max_length=2500, null=True)),
                ('taux', models.CharField(blank=True, default='', max_length=2500, null=True)),
                ('type_taxe', models.CharField(choices=[('TVA', 'TVA'), ('DOUAN', 'DOUAN')], max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='typeClient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_desc', models.CharField(blank=True, default='', max_length=2500, null=True)),
                ('dateCreation', models.DateField(blank=True, default='2023-08-22', null=True)),
                ('montant_min', models.DecimalField(decimal_places=2, default=0, max_digits=150)),
                ('percent', models.DecimalField(decimal_places=2, default=0, max_digits=3)),
            ],
        ),
        migrations.CreateModel(
            name='ValeurDevise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valeur', models.CharField(blank=True, default='', max_length=2500, null=True)),
                ('date', models.DateField(blank=True, default='2023-08-22', null=True)),
            ],
        ),
    ]
