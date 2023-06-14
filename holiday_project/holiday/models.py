
from django.db import models

# Create your models here.
class CalendarYear(models.Model):
    year = models.CharField(max_length=5)
    def __str__(self):
        return str(self.year)

class HolidayModel(models.Model):
    year = models.ForeignKey(CalendarYear, related_name="calendar_year_day", on_delete=models.CASCADE)
    month = models.CharField(max_length=20)
    day = models.CharField(max_length=3)
    weekday = models.CharField(max_length=5)
    is_holiday = models.BooleanField(default=False)
    remarks = models.CharField(max_length=255)

    def __str__(self):
        return str(self.year)