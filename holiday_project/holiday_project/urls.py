"""holiday_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from holiday.views import HolidayView, RemarksView, HolidayUpdateView, RemarksCancelView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',HolidayView.as_view(),name="homepage"),
    path('remarks/',RemarksView.as_view(),name='remarksview'),
    path('remarkscancel/',RemarksCancelView.as_view(),name='remarksviewcancel'),
    path('holidayupdate/',HolidayUpdateView.as_view(),name="holidayupdate"),

]
