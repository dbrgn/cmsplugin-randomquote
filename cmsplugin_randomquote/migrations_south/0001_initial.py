# -*- coding: utf-8 -*-
from south.db import db
from south.v2 import SchemaMigration


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Quote'
        db.create_table('cmsplugin_randomquote_quote', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('quote_text', self.gf('django.db.models.fields.TextField')()),
            ('author', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('cmsplugin_randomquote', ['Quote'])


    def backwards(self, orm):
        # Deleting model 'Quote'
        db.delete_table('cmsplugin_randomquote_quote')


    models = {
        'cmsplugin_randomquote.quote': {
            'Meta': {'object_name': 'Quote'},
            'author': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'quote_text': ('django.db.models.fields.TextField', [], {})
        }
    }

    complete_apps = ['cmsplugin_randomquote']
