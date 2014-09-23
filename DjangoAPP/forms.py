from django import forms
from .models import Category

import widgets
import models


class ModelFormBySite(forms.ModelForm):

    """
    Form that filters out related objs which are not visible to current user.
    """

    rel_field_model_map = {}

    def __init__(self, *args, **kwargs):
        super(ModelFormBySite, self).__init__(*args, **kwargs)
        if not self.current_user.is_superuser:
            if 'site' in self.fields:
                self.fields['site'].queryset = self.current_user.site_set
            for f in self.rel_field_model_map:
                model = self.rel_field_model_map[f]
                self.fields[f].queryset = model.objects.filter(
                    site__in=self.current_user.site_set.all)


class HiddenFieldsForm(ModelFormBySite):

    hidden_fields = []

    def __init__(self, *args, **kwargs):
        super(HiddenFieldsForm, self).__init__(*args, **kwargs)
        for f in self.hidden_fields:
            self.fields[f].widget = forms.HiddenInput()


class ContactAdminForm(HiddenFieldsForm):

    hidden_fields = ['latitude', 'longitude', 'zoom', 'heading', 'pitch']

    google_map = forms.Field(
        widget=widgets.GoogleMapWidget(
            data={
                'elem_id': 'map_canvas',
                'source_elem_id': 'id_address',
                'elem_inline_styles': ['width:380px;', 'height:200px;', 'margin-right:20px;', ],
                'has_pano': True,
            }
        ), required=False)

    class Meta:
        model = models.Contact


class RosterRuleAdminForm(ModelFormBySite):

    def __init__(self, *args, **kwargs):
        super(RosterRuleAdminForm, self).__init__(*args, **kwargs)
        self.fields['week_mask'].widget = widgets.WeekMaskWidget()
        categories = Category.objects.filter(site__in=self.current_user.site_set.all)
        entityids = []
        for category in categories:
            entityids.extend([x.id for x in category.entity_set.all()])
        entityids = frozenset(entityids)
        self.fields['entity'].queryset = self.fields['entity']\
            .queryset.filter(pk__in=entityids)


class EntityAdminForm(ModelFormBySite):

    rel_field_model_map = {'categories': Category}

    type = forms.ModelChoiceField(
        queryset=models.EntityType.objects.all(), widget=widgets.EntityTypeSelect()
    )

    class Meta:
        model = models.Entity


class CategoryAdminForm(ModelFormBySite):

    pass


class PageAdminForm(ModelFormBySite):

    pass
