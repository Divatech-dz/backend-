# Generated by Django 5.1.1 on 2024-10-03 13:35

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('clientinfo', '0002_initial'),
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BoiteArchive',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('date_facturation_fournisseur', models.DateTimeField()),
                ('date_facturation_transitaire', models.DateTimeField()),
                ('montant', models.DecimalField(decimal_places=2, default=0, max_digits=35)),
                ('typedocument', models.CharField(default='', max_length=255)),
                ('label', models.CharField(default='', max_length=255)),
                ('document', models.FileField(upload_to='media/document')),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='The name of the event.', max_length=100)),
                ('description', models.TextField(default='', help_text='The name of the event.')),
                ('event_date', models.DateField(help_text='The date of the event.')),
                ('remember_months', models.IntegerField(default=0, help_text='Number of months in advance to remember the event.')),
                ('remind_days_before', models.IntegerField(default=0, help_text='Number of days before the event to send a reminder.')),
            ],
        ),
        migrations.CreateModel(
            name='RequeteSalarie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(default=datetime.datetime.now)),
                ('objet', models.CharField(default='', max_length=255)),
                ('message', models.TextField(default='')),
                ('reponse', models.TextField(default='')),
                ('datereponse', models.DateTimeField(default=datetime.datetime.now)),
                ('destinataire', models.CharField(default='', max_length=255)),
                ('store', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='clientinfo.store')),
                ('user', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='user.customuser')),
            ],
        ),
        migrations.CreateModel(
            name='Salarie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(default='', max_length=255)),
                ('nomarabe', models.CharField(default='', max_length=255)),
                ('fonction', models.CharField(default='', max_length=255)),
                ('fonctionarabe', models.CharField(default='', max_length=255)),
                ('email', models.CharField(default='', max_length=255)),
                ('phone', models.CharField(default='', max_length=255)),
                ('ccp', models.CharField(default='', max_length=255)),
                ('association', models.CharField(default='', max_length=255)),
                ('actif', models.BooleanField(default=True)),
                ('num_assurancesocial', models.CharField(default='', max_length=255)),
                ('datenaiss', models.DateTimeField(default=datetime.datetime.now)),
                ('lieu_naissance', models.CharField(default='', max_length=255)),
                ('lieu_naissancearabe', models.CharField(default='', max_length=255)),
                ('echellon', models.CharField(default='', max_length=255)),
                ('degre', models.CharField(default='', max_length=255)),
                ('cout_heure', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('salaire', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('prime_espece', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('dateDebut', models.DateField(default=datetime.datetime.now, help_text='The date of start.')),
                ('dateEnd', models.DateField(default=datetime.datetime.now, help_text='The date of start.')),
                ('store', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='clientinfo.store')),
                ('user', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='user.customuser')),
            ],
        ),
        migrations.CreateModel(
            name='Renumeration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mois', models.CharField(default='', max_length=255)),
                ('virement_valide', models.BooleanField(default=False)),
                ('salarie', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='gestionRH.salarie')),
            ],
        ),
        migrations.CreateModel(
            name='ReglementCompte',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateSortie', models.DateTimeField()),
                ('montant', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('note', models.TextField(default='')),
                ('salarie', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mes_reglementscompte', to='gestionRH.salarie')),
            ],
        ),
        migrations.CreateModel(
            name='PrixSocial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('motif', models.CharField(default='', max_length=255)),
                ('montanttotal', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('montantperMonth', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('nombre_months', models.CharField(default='', max_length=255)),
                ('salarie', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mes_prox_social', to='gestionRH.salarie')),
            ],
        ),
        migrations.CreateModel(
            name='PrimeMotivation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('motif', models.CharField(default='', max_length=255)),
                ('valide', models.BooleanField(default=True)),
                ('montant', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('viremenet', models.BooleanField(default=True)),
                ('salarie', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mes_primesmotivation', to='gestionRH.salarie')),
            ],
        ),
        migrations.CreateModel(
            name='Pointage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(default=datetime.datetime.now)),
                ('temps_arrive', models.TimeField(default='09:00:00')),
                ('temps_depart', models.TimeField(default='17:00:00')),
                ('salarie', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mon_pointage', to='gestionRH.salarie')),
            ],
        ),
        migrations.CreateModel(
            name='HeureSup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_heure', models.CharField(default='', max_length=255)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('datetimedeb', models.DateTimeField(default=datetime.datetime.now)),
                ('datetimeend', models.DateTimeField(default=datetime.datetime.now)),
                ('motif', models.CharField(default='', max_length=255)),
                ('valide', models.BooleanField(default=True)),
                ('store', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='clientinfo.store')),
                ('user', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='user.customuser')),
                ('salarie', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mes_heure_sup', to='gestionRH.salarie')),
            ],
        ),
        migrations.CreateModel(
            name='Contrat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_contrat', models.CharField(default='', max_length=255)),
                ('numero_decision_recrutement', models.CharField(default='', max_length=255)),
                ('numero_pv_installation', models.CharField(default='', max_length=255)),
                ('datedeb', models.DateTimeField(default=datetime.datetime.now)),
                ('datesignature', models.DateTimeField(default=datetime.datetime.now)),
                ('datefin', models.DateTimeField(default=datetime.datetime.now)),
                ('type_contrat', models.CharField(default='', max_length=255)),
                ('salarie', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ma_contrat', to='gestionRH.salarie')),
            ],
        ),
        migrations.CreateModel(
            name='Conge',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateDebut', models.DateTimeField(default=datetime.datetime.now)),
                ('dateFin', models.DateTimeField(default=datetime.datetime.now)),
                ('type_conge', models.TextField(default='')),
                ('nbrJourPris', models.IntegerField(default='0')),
                ('salarie', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mon_conge', to='gestionRH.salarie')),
            ],
        ),
        migrations.CreateModel(
            name='AvanceSalaire',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('motif', models.CharField(default='', max_length=255)),
                ('montant', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('salarie', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mes_avances_salaire', to='gestionRH.salarie')),
            ],
        ),
        migrations.CreateModel(
            name='Absence',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('nombre_heure', models.CharField(default='', max_length=255)),
                ('motif', models.CharField(default='', max_length=255)),
                ('minusSource', models.CharField(default='', max_length=255)),
                ('justifie', models.BooleanField(default=False)),
                ('store', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='clientinfo.store')),
                ('user', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='user.customuser')),
                ('salarie', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mes_absences', to='gestionRH.salarie')),
            ],
        ),
    ]
