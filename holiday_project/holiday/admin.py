from django.contrib import admin
from holiday.models import HolidayModel, CalendarYear
# Register your models here.

@admin.register(CalendarYear)
class CalendarYearAdmin(admin.ModelAdmin):
    list_display = ['id', 'year']



@admin.register(HolidayModel)
class HolidayModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'year', 'month', 'day', 'weekday', 'is_holiday', 'remarks']
