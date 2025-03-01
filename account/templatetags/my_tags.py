from django import template
import jdatetime
from django import template
from datetime import datetime

from khayyam.jalali_datetime import JalaliDatetime

register = template.Library()


@register.filter
def to_jalali(date):
    if date:
        jalali_date = jdatetime.datetime.fromgregorian(datetime=date)
        return jalali_date.strftime('%Y/%m/%d')  # Customize the format as needed
    return ''


@register.filter
def to_jalali(value):
    from datetime import datetime

    if not value or not isinstance(value, datetime):
        return "تاریخ نامعتبر"  # Invalid date
    return JalaliDatetime(value).strftime("%d %B %Y")

















# @register.simple_tag
# def calculate_episodes_and_duration(series):
#     total_duration_seconds = 0
#     total_episodes_count = 0
#
#     for season in series.seasons.all():
#         total_duration_seconds += season.total_duration_seconds()
#         total_episodes_count += season.number_of_episodes()
#
#     total_duration_formatted = format_duration(total_duration_seconds)
#
#     return {
#         'total_duration': total_duration_formatted,
#         'total_episodes': total_episodes_count
#     }
