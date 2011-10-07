# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Season'
        db.create_table('core_season', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('year_start', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('year_end', self.gf('django.db.models.fields.CharField')(max_length=10)),
        ))
        db.send_create_signal('core', ['Season'])

        # Adding model 'Conference'
        db.create_table('core_conference', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('abbr', self.gf('django.db.models.fields.CharField')(max_length=10)),
        ))
        db.send_create_signal('core', ['Conference'])

        # Adding model 'School'
        db.create_table('core_school', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('abbr', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('mascot', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('conference', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Conference'])),
        ))
        db.send_create_signal('core', ['School'])

        # Adding model 'Team'
        db.create_table('core_team', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('school', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.School'])),
            ('season', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Season'])),
            ('record', self.gf('django.db.models.fields.CharField')(max_length=20)),
        ))
        db.send_create_signal('core', ['Team'])

        # Adding model 'Game'
        db.create_table('core_game', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date', self.gf('django.db.models.fields.DateTimeField')()),
            ('season', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Season'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('channel', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('away_team', self.gf('django.db.models.fields.related.ForeignKey')(related_name='away_team', to=orm['core.School'])),
            ('away_score', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('home_team', self.gf('django.db.models.fields.related.ForeignKey')(related_name='home_team', to=orm['core.School'])),
            ('home_score', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal('core', ['Game'])

        # Adding model 'Pick'
        db.create_table('core_pick', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('profile', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['profiles.Profile'])),
            ('game', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Game'])),
            ('winner', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.School'])),
            ('home_score', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('away_score', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('is_tie_breaker', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('core', ['Pick'])


    def backwards(self, orm):
        
        # Deleting model 'Season'
        db.delete_table('core_season')

        # Deleting model 'Conference'
        db.delete_table('core_conference')

        # Deleting model 'School'
        db.delete_table('core_school')

        # Deleting model 'Team'
        db.delete_table('core_team')

        # Deleting model 'Game'
        db.delete_table('core_game')

        # Deleting model 'Pick'
        db.delete_table('core_pick')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'core.conference': {
            'Meta': {'object_name': 'Conference'},
            'abbr': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'core.game': {
            'Meta': {'object_name': 'Game'},
            'away_score': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'away_team': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'away_team'", 'to': "orm['core.School']"}),
            'channel': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'date': ('django.db.models.fields.DateTimeField', [], {}),
            'home_score': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'home_team': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'home_team'", 'to': "orm['core.School']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'season': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Season']"})
        },
        'core.pick': {
            'Meta': {'object_name': 'Pick'},
            'away_score': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'game': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Game']"}),
            'home_score': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_tie_breaker': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'profile': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['profiles.Profile']"}),
            'winner': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.School']"})
        },
        'core.school': {
            'Meta': {'object_name': 'School'},
            'abbr': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'conference': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Conference']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mascot': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'core.season': {
            'Meta': {'object_name': 'Season'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'year_end': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'year_start': ('django.db.models.fields.CharField', [], {'max_length': '10'})
        },
        'core.team': {
            'Meta': {'object_name': 'Team'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'record': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'school': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.School']"}),
            'season': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Season']"})
        },
        'profiles.profile': {
            'Meta': {'object_name': 'Profile'},
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        }
    }

    complete_apps = ['core']
