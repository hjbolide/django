import os

from django.forms import widgets
from django import forms
from django.conf import settings
from django.template import loader
from django.utils.html import format_html
from django.utils.translation import ugettext_lazy as e_
from django.utils.encoding import force_text
from django.utils.safestring import mark_safe


class GoogleMapWidget(forms.Widget):

    template_name = 'admin/google_map.html'

    class Media:
        js = (
            settings.GOOGLE_MAPS_URL % settings.GOOGLE_MAPS_API_KEY,
            'DjangoAPP/js/gmap.js'
        )

    def __init__(self, attrs=None, data=None):
        super(GoogleMapWidget, self).__init__(attrs=attrs)
        self.data = data
        
    def _get_options(self, defaults, options):
        return {x: options.get(x, y) for x, y in defaults}

    def get_map_options(self, options):

        lat, lng = settings.DEFAULT_MAP_CENTRE
        
        defaults = [('lat', lat),
                    ('lng', lng),
                    ('zoom', settings.DEFAULT_MAP_ZOOM),
                    ('reflect_longitude_elem_id', 'id_longitude'),
                    ('reflect_latitude_elem_id', 'id_latitude'),
                    ('reflect_zoom_elem_id', 'id_zoom')]
        return self._get_options(defaults, options)
    
    def get_pano_options(self, options):
        
        defaults = [('heading', 0),
                    ('pitch', 0),
                    ('reflect_heading_elem_id', 'id_heading'),
                    ('reflect_pitch_elem_id', 'id_pitch')]
        return self._get_options(defaults, options)
        
    def make_map_context(self, attrs=None):
        return self.build_attrs(
            attrs,
            elem_id=self.data.get('elem_id', 'map_canvas'),
            source_elem_id=self.data.get('source_elem_id', 'id_address'),
            map_options=self.get_map_options(self.data.get('map_options', {})),
            has_pano=self.data.get('has_pano', True),
            pano_options=self.get_pano_options(self.data.get('pano_options', {})),
            elem_inline_styles=self.data.get('elem_inline_styles', None))
        
    def render(self, name, value, attrs=None):
        context = self.make_map_context(attrs=attrs)
        return loader.render_to_string(self.template_name, context)


class WeekMaskWidget(forms.CheckboxSelectMultiple):

    CHOICES = (
        (0b00000001, e_('Monday')),
        (0b00000010, e_('Tuesday')),
        (0b00000100, e_('Wednesday')),
        (0b00001000, e_('Thursday')),
        (0b00010000, e_('Friday')),
        (0b00100000, e_('Saturday')),
        (0b01000000, e_('Sunday')),
    )

    def __init__(self, attrs=None):
        super(WeekMaskWidget, self).__init__(attrs=attrs, choices=self.CHOICES)

    def render(self, name, value, attrs=None, choices=()):
        data = []
        for i in range(7):
            mask_ = 1 << i
            if mask_ & value:
                data.append(mask_)
        return super(WeekMaskWidget, self).render(name, data, attrs=attrs, choices=choices)

    def value_from_datadict(self, data, files, name):
        days = super(WeekMaskWidget, self).value_from_datadict(data, files, name)
        if not days:
            return 0
        return reduce(lambda x, y: x | y, map(int, days), 0)


class EntityTypeSelect(forms.Select):

    def render_option(self, selected_choices, option_value, option_label):
        from .models import EntityType
        option_value = force_text(option_value)
        if option_value in selected_choices:
            selected_html = mark_safe(' selected="selected"')
            if not self.allow_multiple_selected:
                # Only allow for a single selection.
                selected_choices.remove(option_value)
        else:
            selected_html = ''
        is_person = False
        if option_value:
            entity_type = EntityType.objects.filter(pk=option_value).first()
            is_person = entity_type.is_person
        return format_html('<option data-is_person="{0}" value="{1}"{2}>{3}</option>',
                           is_person,
                           option_value,
                           selected_html,
                           force_text(option_label))