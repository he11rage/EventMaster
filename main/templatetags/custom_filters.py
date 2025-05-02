from django import template
from datetime import datetime

register = template.Library()

def get_ru_month_name(month_number):
    months = {
        1: 'января', 2: 'февраля', 3: 'марта', 4: 'апреля', 5: 'мая', 6: 'июня',
        7: 'июля', 8: 'августа', 9: 'сентября', 10: 'октября', 11: 'ноября', 12: 'декабря'
    }
    return months.get(month_number, '')

@register.filter
def ru_date(value):
    if isinstance(value, datetime):  # Проверяем, что переданный объект — это дата
        return f"{value.day} {get_ru_month_name(value.month)} {value.year}"
    return value
