from django.shortcuts import render
from django.http import JsonResponse


from .models import *


def recruitmentForm(request):
    data={
        'status':None,
        'message':None
    }

    if request.method == 'POST':
        fullname=request.POST.get('fullname')
        registrationNumber=request.POST.get('registrationNumber').upper()
        department=request.POST.get('department')
        section=request.POST.get('section')
        srmmail=request.POST.get('srmmail')
        personalmail=request.POST.get('personalmail')
        mobile=request.POST.get('mobile')
        whatsappnumber=request.POST.get('whatsappnumber')
        year=request.POST.get('year')
        domain1=request.POST.get('domain1')
        domain2=request.POST.get('domain2')
        linkedin=request.POST.get('linkedin')
        github=request.POST.get('github')
        resume=request.POST.get('resume')
        question1=request.POST.get('question1')
        question2=request.POST.get('question2')

        try:
            if(srmmail.split('@')[1]!='srmist.edu.in'):
                data['status']='error'
                data['message']='Invalid SRM Mail'
                return render(request,'recruitmentForm.html',data)
            
            search=Registrations.objects.filter(srmmail=srmmail)
            if(search):
                data['status']='error'
                data['message']='Email Already Registered ..XX '
                return render(request,'recruitmentForm.html',data)

            obj=Registrations(fullname=fullname,registrationNumber=registrationNumber,department=department,section=section,srmmail=srmmail,personalmail=personalmail,mobile=mobile,whatsappnumber=whatsappnumber,year=year,domain1=domain1,domain2=domain2,linkedin=linkedin,github=github,resume=resume,question1=question1,question2=question2)
            obj.save()
            data['status']='success'
            data['message']='Registered Seccessfully !!!'

        except Exception as e:
            data['status']='error'
            data['message']=str(e)
            print(e)

        return render(request,'recruitmentForm.html',data)
        
    return render(request,'recruitmentForm.html',data)