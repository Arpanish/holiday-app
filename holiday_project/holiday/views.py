from django.shortcuts import render
from django.views import View
from holiday.models import HolidayModel
from django.http import JsonResponse


# Create your views here.

class HolidayView(View):
    def get(self,request):
        query = HolidayModel.objects.all()
        return render(request,'holiday/holiday.html',{'query':query})
    
      
class HolidayUpdateView(View):
    def post(self,request):
        select_value = request.POST.get("select_value")
        print(select_value)
        id = request.POST.get("id")
        print(id)
        change_holiday_value = HolidayModel.objects.get(pk=id)
        print(change_holiday_value)
        change_holiday_value.is_holiday = select_value
        change_holiday_value.save() 
        return render(request,'holiday/holiday.html')


class RemarksView(View):
    def post(self,request):
        remarks_input_value= request.POST.get("remarks_input_value")  
        id = request.POST.get("remarks_id") 
        print(remarks_input_value)
        add_remarks = HolidayModel.objects.get(pk=id)
        add_remarks.remarks = remarks_input_value
        add_remarks.save()
        data={
                'remarks': remarks_input_value,
                'status':"success",
                'id':id
            }
        return JsonResponse({'data':data})


class RemarksCancelView(View):
     def post(self,request):
        remarks_input_value= request.POST.get("remarks_input_value")  
        id = request.POST.get("remarks_id") 
        print(remarks_input_value)
        add_remarks = HolidayModel.objects.get(pk=id)
        # add_remarks.remarks = remarks_input_value
        # add_remarks.save()
        data={
                'remarks': add_remarks.remarks,
                'id':id
            }
        return JsonResponse({'data':data})
