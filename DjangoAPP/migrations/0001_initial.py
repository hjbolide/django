# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Site'
        db.create_table(u'DjangoAPP_site', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')()),
            ('modified_at', self.gf('django.db.models.fields.DateTimeField')()),
            ('type', self.gf('django.db.models.fields.CharField')(max_length=16, null=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], blank=True)),
        ))
        db.send_create_signal(u'DjangoAPP', ['Site'])

        # Adding model 'Contact'
        db.create_table(u'DjangoAPP_contact', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=10, null=True)),
            ('mobile', self.gf('django.db.models.fields.CharField')(max_length=10, null=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75, null=True)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=125)),
            ('longitude', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('latitude', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('site', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['DjangoAPP.Site'])),
        ))
        db.send_create_signal(u'DjangoAPP', ['Contact'])

        # Adding model 'Entity'
        db.create_table(u'DjangoAPP_entity', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('type', self.gf('django.db.models.fields.CharField')(max_length=16, null=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('dob', self.gf('django.db.models.fields.DateField')(null=True)),
            ('gender', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('price', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('data', self.gf('django.db.models.fields.BinaryField')(null=True)),
        ))
        db.send_create_signal(u'DjangoAPP', ['Entity'])

        # Adding M2M table for field categories on 'Entity'
        m2m_table_name = db.shorten_name(u'DjangoAPP_entity_categories')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('entity', models.ForeignKey(orm[u'DjangoAPP.entity'], null=False)),
            ('category', models.ForeignKey(orm[u'DjangoAPP.category'], null=False))
        ))
        db.create_unique(m2m_table_name, ['entity_id', 'category_id'])

        # Adding model 'Category'
        db.create_table(u'DjangoAPP_category', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=16)),
            ('desc', self.gf('django.db.models.fields.CharField')(max_length=200, null=True)),
            ('site', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['DjangoAPP.Site'])),
        ))
        db.send_create_signal(u'DjangoAPP', ['Category'])

        # Adding M2M table for field entities on 'Category'
        m2m_table_name = db.shorten_name(u'DjangoAPP_category_entities')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('category', models.ForeignKey(orm[u'DjangoAPP.category'], null=False)),
            ('entity', models.ForeignKey(orm[u'DjangoAPP.entity'], null=False))
        ))
        db.create_unique(m2m_table_name, ['category_id', 'entity_id'])

        # Adding model 'Page'
        db.create_table(u'DjangoAPP_page', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('html_id', self.gf('django.db.models.fields.CharField')(max_length=16, null=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=16)),
            ('display_name', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('desc', self.gf('django.db.models.fields.TextField')(null=True)),
            ('data', self.gf('django.db.models.fields.BinaryField')(null=True)),
            ('site', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['DjangoAPP.Site'])),
        ))
        db.send_create_signal(u'DjangoAPP', ['Page'])

        # Adding model 'RosterRule'
        db.create_table(u'DjangoAPP_rosterrule', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('week_mask', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('date', self.gf('django.db.models.fields.DateField')(null=True)),
            ('entity', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['DjangoAPP.Entity'], null=True)),
        ))
        db.send_create_signal(u'DjangoAPP', ['RosterRule'])


    def backwards(self, orm):
        # Deleting model 'Site'
        db.delete_table(u'DjangoAPP_site')

        # Deleting model 'Contact'
        db.delete_table(u'DjangoAPP_contact')

        # Deleting model 'Entity'
        db.delete_table(u'DjangoAPP_entity')

        # Removing M2M table for field categories on 'Entity'
        db.delete_table(db.shorten_name(u'DjangoAPP_entity_categories'))

        # Deleting model 'Category'
        db.delete_table(u'DjangoAPP_category')

        # Removing M2M table for field entities on 'Category'
        db.delete_table(db.shorten_name(u'DjangoAPP_category_entities'))

        # Deleting model 'Page'
        db.delete_table(u'DjangoAPP_page')

        # Deleting model 'RosterRule'
        db.delete_table(u'DjangoAPP_rosterrule')


    models = {
        u'DjangoAPP.category': {
            'Meta': {'object_name': 'Category'},
            'desc': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True'}),
            'entities': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['DjangoAPP.Entity']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '16'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['DjangoAPP.Site']"})
        },
        u'DjangoAPP.contact': {
            'Meta': {'object_name': 'Contact'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '125'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitude': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'longitude': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'mobile': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['DjangoAPP.Site']"})
        },
        u'DjangoAPP.entity': {
            'Meta': {'object_name': 'Entity'},
            'categories': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['DjangoAPP.Category']", 'symmetrical': 'False', 'blank': 'True'}),
            'data': ('django.db.models.fields.BinaryField', [], {'null': 'True'}),
            'dob': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'price': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True'})
        },
        u'DjangoAPP.page': {
            'Meta': {'object_name': 'Page'},
            'data': ('django.db.models.fields.BinaryField', [], {'null': 'True'}),
            'desc': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'display_name': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'html_id': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '16'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['DjangoAPP.Site']"})
        },
        u'DjangoAPP.rosterrule': {
            'Meta': {'object_name': 'RosterRule'},
            'date': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'entity': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['DjangoAPP.Entity']", 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'week_mask': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        u'DjangoAPP.site': {
            'Meta': {'object_name': 'Site'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified_at': ('django.db.models.fields.DateTimeField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True'}),
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