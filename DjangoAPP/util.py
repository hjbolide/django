from django.utils.translation import ugettext as _

from collections import OrderedDict
from .widgets import WeekMaskWidget


def filter_by_site(request, queryset):
    if request.user.is_superuser:
        return queryset
    return queryset.filter(site__in=request.user.site_set.all)


def get_week(value, translate=False):
    data = []
    for i in range(7):
        mask_ = 1 << i
        if mask_ & value:
            data.append(mask_)
    if not translate:
        return data

    week_mappings = OrderedDict(WeekMaskWidget.CHOICES)
    return map(lambda x: _(week_mappings[x]), data)