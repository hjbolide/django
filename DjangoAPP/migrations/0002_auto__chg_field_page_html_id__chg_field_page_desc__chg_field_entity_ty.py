# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Page.html_id'
        db.alter_column(u'DjangoAPP_page', 'html_id', self.gf('django.db.models.fields.CharField')(default='', max_length=16))

        # Changing field 'Page.desc'
        db.alter_column(u'DjangoAPP_page', 'desc', self.gf('django.db.models.fields.TextField')(default=''))

        # Changing field 'Entity.type'
        db.alter_column(u'DjangoAPP_entity', 'type', self.gf('django.db.models.fields.CharField')(default='', max_length=16))

        # Changing field 'Category.desc'
        db.alter_column(u'DjangoAPP_category', 'desc', self.gf('django.db.models.fields.CharField')(default='', max_length=200))

        # Changing field 'Contact.mobile'
        db.alter_column(u'DjangoAPP_contact', 'mobile', self.gf('django.db.models.fields.CharField')(default='', max_length=10))

        # Changing field 'Contact.phone'
        db.alter_column(u'DjangoAPP_contact', 'phone', self.gf('django.db.models.fields.CharField')(default='', max_length=10))

        # Changing field 'Contact.email'
        db.alter_column(u'DjangoAPP_contact', 'email', self.gf('django.db.models.fields.EmailField')(default='', max_length=75))

        # Changing field 'Site.type'
        db.alter_column(u'DjangoAPP_site', 'type', self.gf('django.db.models.fields.CharField')(default='', max_length=16))

    def backwards(self, orm):

        # Changing field 'Page.html_id'
        db.alter_column(u'DjangoAPP_page', 'html_id', self.gf('django.db.models.fields.CharField')(max_length=16, null=True))

        # Changing field 'Page.desc'
        db.alter_column(u'DjangoAPP_page', 'desc', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'Entity.type'
        db.alter_column(u'DjangoAPP_entity', 'type', self.gf('django.db.models.fields.CharField')(max_length=16, null=True))

        # Changing field 'Category.desc'
        db.alter_column(u'DjangoAPP_category', 'desc', self.gf('django.db.models.fields.CharField')(max_length=200, null=True))

        # Changing field 'Contact.mobile'
        db.alter_column(u'DjangoAPP_contact', 'mobile', self.gf('django.db.models.fields.CharField')(max_length=10, null=True))

        # Changing field 'Contact.phone'
        db.alter_column(u'DjangoAPP_contact', 'phone', self.gf('django.db.models.fields.CharField')(max_length=10, null=True))

        # Changing field 'Contact.email'
        db.alter_column(u'DjangoAPP_contact', 'email', self.gf('django.db.models.fields.EmailField')(max_length=75, null=True))

        # Changing field 'Site.type'
        db.alter_column(u'DjangoAPP_site', 'type', self.gf('django.db.models.fields.CharField')(max_length=16, null=True))

    models = {
        u'DjangoAPP.category': {
            'Meta': {'object_name': 'Category'},
            'desc': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'entities': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['DjangoAPP.Entity']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '16'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['DjangoAPP.Site']"})
        },
        u'DjangoAPP.contact': {
            'Meta': {'object_name': 'Contact'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '125'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitude': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'longitude': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'mobile': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['DjangoAPP.Site']"})
        },
        u'DjangoAPP.entity': {
            'Meta': {'object_name': 'Entity'},
            'categories': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['DjangoAPP.Category']", 'symmetrical': 'False', 'blank': 'True'}),
            'data': ('django.db.models.fields.BinaryField', [], {'null': 'True', 'blank': 'True'}),
            'dob': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'price': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '16', 'blank': 'True'})
        },
        u'DjangoAPP.page': {
            'Meta': {'object_name': 'Page'},
            'data': ('django.db.models.fields.BinaryField', [], {'null': 'True', 'blank': 'True'}),
            'desc': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'display_name': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'html_id': ('django.db.models.fields.CharField', [], {'max_length': '16', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '16'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['DjangoAPP.Site']"})
        },
        u'DjangoAPP.rosterrule': {
            'Meta': {'object_name': 'RosterRule'},
            'date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'entity': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['DjangoAPP.Entity']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'week_mask': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        u'DjangoAPP.site': {
            'Meta': {'object_name': 'Site'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 4, 25, 0, 0)', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 4, 25, 0, 0)', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '16', 'blank': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']", 'blank': 'True'})
        },
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['DjangoAPP']