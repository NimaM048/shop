from django import template
from django.utils.timezone import localtime
import jdatetime


register = template.Library()

@register.filter
def sum(queryset, attr):
    if not queryset:
        return 0
    return sum(
        getattr(obj, attr)() if callable(getattr(obj, attr, None)) else getattr(obj, attr, 0)
        for obj in queryset
    )

register = template.Library()

@register.filter
def to_jalali(date):
    if not date:
        return ""
    date = localtime(date)  
    jalali_date = jdatetime.datetime.fromgregorian(datetime=date)
    return jalali_date.strftime('%Y/%m/%d') 


