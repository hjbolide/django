from django.contrib import admin

from .decorators import superuser_only_view

import models
import forms

from .util import filter_by_site


def register_models(model_list):
    for m in model_list:
        n = None
        if isinstance(m, tuple):
            m, n = m
        admin.site.register(m, admin_class=n)


class ModelAdminWithUser(admin.ModelAdmin):

    """
    Attach current_user to the form.
    """

    def get_form(self, request, obj=None, **kwargs):
        form = super(ModelAdminWithUser, self).get_form(request, obj, **kwargs)
        form.current_user = request.user
        return form


class SiteModelAdmin(ModelAdminWithUser):

    def get_queryset(self, request):
        qs = super(SiteModelAdmin, self).get_queryset(request)
        return filter_by_site(request, qs)


class PageAdmin(SiteModelAdmin):

    list_display = ('name', 'display_name', 'html_id')

    form = forms.PageAdminForm


class CategoryAdmin(SiteModelAdmin):

    list_display = ('name', )

    form = forms.CategoryAdminForm


class EntityAdmin(ModelAdminWithUser):

    list_display = ('name', 'dob', 'gender', 'type', 'display_categories')

    form = forms.EntityAdminForm

    def get_queryset(self, request):
        # show the entity if one of its categories belongs to user's site
        qs = super(EntityAdmin, self).get_queryset(request)
        if not request.user.is_superuser:
            result = filter(lambda x: len(filter_by_site(request, x.categories.all())) > 0, qs)
            entityids = frozenset([x.id for x in result])
            return qs.filter(pk__in=entityids)
        return qs


class SiteAdmin(ModelAdminWithUser):

    list_display = ('name', 'url', 'type', 'user')

    def get_queryset(self, request):
        qs = super(SiteAdmin, self).get_queryset(request)
        if not request.user.is_superuser:
            return qs.filter(pk__in=request.user.site_set.all)
        return qs


class ContactAdmin(SiteModelAdmin):

    form = forms.ContactAdminForm

    list_display = ('email', 'phone', 'mobile', 'site', 'address', )


class RosterRuleAdmin(SiteModelAdmin):

    list_display = ('entity', 'display_week', )

    form = forms.RosterRuleAdminForm


class HiddenModelAdmin(ModelAdminWithUser):

    """
    Hidden to all users except super users.
    """

    def get_model_perms(self, request):
        perms = super(HiddenModelAdmin, self).get_model_perms(request)
        if not request.user.is_superuser:
            perms['hidden'] = True
        return perms

    def get_queryset(self, request):
        qs = super(HiddenModelAdmin, self).get_queryset(request)
        if not request.user.is_superuser:
            qs.delete()
        return qs

    @superuser_only_view
    def changelist_view(self, request, extra_context=None):
        return super(HiddenModelAdmin, self).changelist_view(request, extra_context)

    @superuser_only_view
    def add_view(self, request, form_url='', extra_context=None):
        return super(HiddenModelAdmin, self).add_view(
            request, form_url, extra_context)

    @superuser_only_view
    def history_view(self, request, object_id, extra_context=None):
        return super(HiddenModelAdmin, self).history_view(
            request, object_id, extra_context)

    @superuser_only_view
    def delete_view(self, request, object_id, extra_context=None):
        return super(HiddenModelAdmin, self).delete_view(
            request, object_id, extra_context)

    @superuser_only_view
    def change_view(self, request, object_id, form_url='', extra_context=None):
        return super(HiddenModelAdmin, self).change_view(
            request, object_id, form_url, extra_context)


class SiteTypeModelAdmin(HiddenModelAdmin):
    pass


class EntityTypeModelAdmin(HiddenModelAdmin):
    pass


admin_models = [
    (models.SiteType, SiteTypeModelAdmin),
    (models.EntityType, EntityTypeModelAdmin),
    (models.Site, SiteAdmin),
    (models.Contact, ContactAdmin),
    (models.Entity, EntityAdmin),
    (models.Category, CategoryAdmin),
    (models.Page, PageAdmin),
    (models.RosterRule, RosterRuleAdmin),
]

register_models(admin_models)
