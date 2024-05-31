from django.shortcuts import render, get_object_or_404
from django.views.decorators.cache import never_cache
from django.utils.decorators import method_decorator
from django.shortcuts import redirect
from django.http import HttpResponse
from django.template import loader
from . forms import pub1
from . forms import panchayath1
from . models1 import pub
from . models2 import panchayath
from . models3 import ads
from . forms import ads1
from . models4 import workemployee
from . forms1 import emp1
from . forms import workre
from . models5 import workrequest
from . models6 import notifition
from . forms import notifi
from datetime import date
from . models8 import entry12
from . forms import worken 
from . forms import workcom
from . models9 import workcomplete
from . models10 import complaints
from . forms import complain
from . models12 import reply2
from . forms import repl
from . models13 import user
from . forms import LoginForm
from . models14 import empattendence
from . forms import takeattendence
from . models15 import newwork
from . forms import newemp
from . models16 import feedbacks
from . forms import feed
from . models17 import workassign
from . models18 import salary
from . forms import salary12
from . forms import chat1
from . models19 import message1
from django.urls import reverse
from . models20 import reply12
from . forms import rep1
from . models21 import admin
from datetime import datetime
from reportlab.pdfgen import canvas
from io import BytesIO
from django.views import View
from django.http import FileResponse
from django.template.loader import get_template
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Frame, PageTemplate
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter, landscape
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle




def no_cache(view_func):
    decorated_view=never_cache(view_func)
    return decorated_view

def Ho(request):
    template=loader.get_template('index.html')
    return HttpResponse(template.render())

def publ(request):
    if request.method=="POST":
        fm=pub1(request.POST)
        if fm.is_valid():
            fm.save()
            return redirect('home')
    else:
        fm=pub1()
    return render(request,'public.html',{'fm':fm})


def log(request):
    template=loader.get_template('login.html')
    return HttpResponse(template.render())

@no_cache  
def admin1(request):
    user_id = request.session.get('admin_id')
    try:
        User =admin.objects.get(id=user_id)
    except admin.DoesNotExist:
        return redirect('home')
    ph=panchayath.objects.all().count()
    ad=ads.objects.all().count()
    wr=workemployee.objects.all().count()
    pu=pub.objects.all().count()
    print(ph)
    return render(request,'admin.html',{'ph':ph,'ad':ad,'wr':wr,'pu':pu})

@no_cache   
def pancha(request):
    user_id = request.session.get('admin_id')
    try:
        User =admin.objects.get(id=user_id)
    except admin.DoesNotExist:
        return redirect('home')
    if request.method=='POST':
        gf=panchayath1(request.POST)
        if gf.is_valid():
            gf.save()
            return redirect('ad')
    else:
        gf=panchayath1()

    return render(request,'panchayath.html',{'pa':gf})

@no_cache
def pavi(request):
    user_id = request.session.get('admin_id')
    try:
        User =admin.objects.get(id=user_id)
    except admin.DoesNotExist:
        return redirect('home')
    ph=panchayath.objects.all().values()
    return render(request,'panchayathview.html',{'ph':ph})

def adsr(request):
    if request.method=='POST':
        ad=ads1(request.POST)
        if ad.is_valid():
            ad.save()
            return redirect('home')
    else:
        ad=ads1()
    return render(request,'ads.html',{'a':ad})

def ac(request):
    adr=ads.objects.all().values()
    return render(request,'adsview.html',{'q':adr})

def we(request):
    if request.method=='POST':
        emw=emp1(request.POST)
        if emw.is_valid():
             emw.save()
             return redirect('home')
    else:
        emw=emp1()
    return render(request,'employee.html',{'p':emw})
def emp(request):
    emv=workemployee.objects.all().values()
    return render(request,'employeeview.html',{'r':emv})

@no_cache
def adsregi(request):
    user_id = request.session.get('panchayath_id')
    try:
        User =panchayath.objects.get(id=user_id)
    except panchayath.DoesNotExist:
        return redirect('home')
    adr=ads.objects.all().values()
    return render(request,'adsregistered.html',{'q':adr})


@no_cache
def empre(request):
    user_id = request.session.get('panchayath_id')
    try:
        User =panchayath.objects.get(id=user_id)
    except panchayath.DoesNotExist:
        return redirect('home')
    emv=workemployee.objects.all().values()
    return render(request,'employeeregistered.html',{'r':emv})


@no_cache
def wre(request):
    user_id = request.session.get('pub_id')
    id=pub.objects.get(id=user_id)
    try:
        User =pub.objects.get(id=user_id)
    except pub.DoesNotExist:
        return redirect('home')
    if request.method=='POST':
        wr=workre(request.POST,request.FILES)
        if wr.is_valid():
            f=wr.save(commit=False)
            f.user=id.id
            f.save()
            return redirect('we1')
    else:
        wr=workre()
    return render(request,'workrequest.html',{'p':wr})

@no_cache
def wor(request):
    user_id = request.session.get('panchayath_id')
    try:
        User =panchayath.objects.get(id=user_id)
    except panchayath.DoesNotExist:
        return redirect('home')
    emv=workrequest.objects.all().values()
    return render(request,'workrequestregistered.html',{'m':emv})
def edit(request,id):
    if request.method=='POST':
        mydata=workrequest.objects.get(id=id)
        fm=workre(request.POST,instance=mydata)
        if fm.is_valid():
            fm.save()
            return redirect('workrequestview')
    else:
        mydata=workrequest.objects.get(id=id)
        fm=workre(instance=mydata)
    return render(request,'workrequestedit.html',{'p':fm})


@no_cache
def worv(request):
    user_id = request.session.get('pub_id')
    try:
        User =pub.objects.get(id=user_id)
    except pub.DoesNotExist:
        return redirect('home')
    emv=workrequest.objects.filter(user=user_id)
    return render(request,'workrequestview.html',{'m':emv})

def delete(request,id):
    mydata=workrequest.objects.get(id=id)
    mydata.delete()
    return redirect('workrequestview')

@no_cache
def notific(request):
    user_id = request.session.get('panchayath_id')
    try:
        User =panchayath.objects.get(id=user_id)
    except panchayath.DoesNotExist:
        return redirect('home')
    if request.method=='POST':
        nf=notifi(request.POST)
        if nf.is_valid():
            nf=nf.save(commit=False)
            nf.date=date.today()
            nf.save()
            return redirect('notification')
    else:
         nf=notifi()
    return render(request,'notification.html',{'jw':nf})

@no_cache
def novi(request):
    user_id = request.session.get('panchayath_id')
    try:
        User =panchayath.objects.get(id=user_id)
    except panchayath.DoesNotExist:
        return redirect('home')
    fm=notifition.objects.all().values()
    return render(request,'notificationview.html',{'fm':fm})

@no_cache
def noviw(request):
    user_id = request.session.get('pub_id')
    try:
        User =pub.objects.get(id=user_id)
    except pub.DoesNotExist:
        return redirect('home')
    fm=notifition.objects.filter(user='PUBLIC')
    return render(request,'notificationviewreg.html',{'fm':fm})

@no_cache
def noviw1(request):
    user_id = request.session.get('ads_id')
    try:
        User =ads.objects.get(id=user_id)
    except ads.DoesNotExist:
        return redirect('home')
    fm=notifition.objects.filter(user='ADS')
    return render(request,'notificationviewreg1.html',{'fm':fm})

def noedit(request,id):
    if request.method=='POST':
        mdata=notifition.objects.get(id=id)
        fm=notifi(request.POST,instance=mdata)
        if fm.is_valid():
            fm.save()
            return redirect('ee')
    else:
        mdata=notifition.objects.get(id=id)
        fm=notifi(instance=mdata)
    return render(request,'notificationedit.html',{'fm':fm})

def nodelete(request,id):
    mdata=notifition.objects.get(id=id)
    mdata.delete()
    return redirect('ee')

@no_cache
def empree(request):
    user_id = request.session.get('ads_id')
    try:
        User =ads.objects.get(id=user_id)
    except ads.DoesNotExist:
        return redirect('home')
    emv=workemployee.objects.all().values()
    return render(request,'employeeregistered2.html',{'r':emv})


def workentry2(request):
    if request.method=='POST':
        wr=worken(request.POST)
        if wr.is_valid():
            wr.save()
    else:
        wr=worken()
    return render(request,'workentry.html',{'wa':wr})

def workentry3(request,id):
    if request.method=='POST':
        medata=panchayath.objects.get(id=id)
        fm=worken(request.POST)
        if fm.is_valid():
            f=fm.save(commit=False)
            f.panchayathid=medata.id
            f.save()
    else:
        medata=panchayath.objects.get(id=id)
        fm=worken()
    return render(request,'workentry.html',{'fm':fm})

@no_cache
def workview(request,id):
    user_id = request.session.get('admin_id')
    try:
        User =admin.objects.get(id=user_id)
    except admin.DoesNotExist:
        return redirect('home')
    fm=entry12.objects.filter(panchayathid=id).values()
    return render(request,'workentryview.html',{'fm':fm})

def workedit(request,id):
    if request.method=='POST':
        medata=entry12.objects.get(id=id)
        fm=worken(request.POST,instance=medata)
        if fm.is_valid():
            fm.save()
            return redirect('ad')
    else:
        medata=entry12.objects.get(id=id)
        fm=worken(instance=medata)
    return render(request,'workentryedit.html',{'fm':fm})

def workdelete(request,id,pid):
    fm=entry12.objects.filter(panchayathid=pid).values()
    medata=entry12.objects.get(id=id)
    medata.delete()
    return redirect('pav')
    #return render(request, 'workentryview.html',{'fm':fm})

@no_cache
def workview2(request):
    user_id = request.session.get('ads_id')
    try:
        User =ads.objects.get(id=user_id)
    except ads.DoesNotExist:
        return redirect('home')
    fm=entry12.objects.all().values()
    return render(request,'workentryview2.html',{'fm':fm})

@no_cache
def woco(request,id):
    user_id = request.session.get('ads_id')
    try:
        User =ads.objects.get(id=user_id)
    except ads.DoesNotExist:
        return redirect('home')
    if request.method=='POST':
        medata=entry12.objects.get(id=id)
        wr=workcom(request.POST)
        if wr.is_valid():
            nf=wr.save(commit=False)
            nf.todate=date.today()
            nf.workentryid=medata.id
            nf.save()
            return redirect('e2')
    else:
        medata=entry12.objects.get(id=id)
        wr=workcom()
    return render(request,'workcomplete.html',{'fm':wr})

@no_cache
def workcomview(request):
    user_id = request.session.get('panchayath_id')
    try:
        User =panchayath.objects.get(id=user_id)
    except panchayath.DoesNotExist:
        return redirect('home')
    fm=workcomplete.objects.all().values()
    return render(request,'workcompleteview.html',{'fm':fm})

def workcomview2(request):
    fm=workcomplete.objects.all().values()
    return render(request,'workcompleteview2.html',{'fm':fm})

def workcomview21(request,id):
    fm=workcomplete.objects.filter(workentryid=id).values()
    return render(request,'workcompleteview2.html',{'fm':fm})

def workcompleteedit(request,id):
    if request.method=='POST':
        wdata=workcomplete.objects.get(id=id)
        gm=workcom(request.POST,instance=wdata)
        if gm.is_valid():
            gm.save()
    else:
        wdata=workcomplete.objects.get(id=id)
        gm=workcom(instance=wdata)
    return render(request,'workcompleteedit.html',{'fm':gm})

def workcompletedelete(request,id):
    wdata=workcomplete.objects.get(id=id)
    wdata.delete()
    return redirect('e2')

@no_cache
def complaint12(request):
    user_id = request.session.get('pub_id')
    try:
        User =pub.objects.get(id=user_id)
    except pub.DoesNotExist:
        return redirect('home')
    if request.method=='POST':
        cr=complain(request.POST)
        if cr.is_valid():
            cr=cr.save(commit=False)
            cr.user=user_id
            cr.todate=date.today()
            cr.save()
            return redirect('we1')
    else:
        cr=complain()
    return render(request,'complaints.html',{'pr':cr})

@no_cache
def compview(request):
    user_id = request.session.get('admin_id')
    try:
        User =admin.objects.get(id=user_id)
    except admin.DoesNotExist:
        return redirect('home')
    cp=complaints.objects.all().values()
    return render(request,'complaintsview.html',{'cp':cp})

@no_cache
def compview2(request):
    user_id = request.session.get('pub_id')
    try:
        User =pub.objects.get(id=user_id)
    except pub.DoesNotExist:
        return redirect('home')
    cp=complaints.objects.filter(user=user_id)
    return render(request,'complaintsview2.html',{'cp':cp})

def complaintedit(request,id):
    if request.method=='POST':
        cpdata=complaints.objects.get(id=id)
        cd=complain(request.POST,instance=cpdata)
        if cd.is_valid():
            cd.save()
    else:
        cpdata=complaints.objects.get(id=id)
        cd=complain(instance=cpdata)
    return render(request,'complaintsedit.html',{'cr':cd})

def complaindelete(request,id):
    cpdata=complaints.objects.get(id=id)
    cpdata.delete()
    return redirect('cv2')

def replies1(request,id):
    if request.method=='POST':
        rdata=complaints.objects.get(id=id)
        rp=repl(request.POST)
        if rp.is_valid():
            rp=rp.save(commit=False)
            rp.redate=date.today()
            rp.replyid=rdata.id
            rp.save()
            return redirect('cv')
    else:
        rp=repl()
    return render(request,'replies.html',{'rp':rp})

@no_cache
def rep12(request,id):
    user_id = request.session.get('pub_id')
    try:
        User =pub.objects.get(id=user_id)
    except pub.DoesNotExist:
        return redirect('home')
    cp=reply2.objects.filter(replyid=id).values()
    return render(request,'replyview.html',{'cp':cp})

@no_cache   
def rep13(request,id):
    user_id = request.session.get('admin_id')
    try:
        User =admin.objects.get(id=user_id)
    except admin.DoesNotExist:
        return redirect('home')
    cp=reply2.objects.filter(replyid=id).values()
    return render(request,'replyview2.html',{'cp':cp})

def replyedit(request,id):
    if request.method=='POST':
        rdata=reply2.objects.get(id=id)
        fm=repl(request.POST,instance=rdata)
        if fm.is_valid():
            fm.save()
    else:
        rdata=reply2.objects.get(id=id)
        fm=repl(instance=rdata)
    return render(request,'replyedit.html',{'rp':fm})

def repdelete1(request,id):
    rdata=reply2.objects.get(id=id)
    rdata.delete()
    return redirect('cv')

def login1(request,usertype):
    print(usertype)
    if usertype=="public":
        if request.method == 'POST':
            form = LoginForm(request.POST)
            if form.is_valid():
                email =form.cleaned_data['email']
                password =form.cleaned_data['password']
                try:
                    User =pub.objects.get(emailid=email, password=password)
                    request.session['pub_id'] = User.id
                    return redirect('we1')
                except pub.DoesNotExist:
                    form.add_error(None, 'Invalid username or password.')
        else:
            form = LoginForm()
        return render(request, 'login.html', {'form': form})


    if usertype=="ads":
        if request.method == 'POST':
            form = LoginForm(request.POST)
            if form.is_valid():
                email =form.cleaned_data['email']
                password =form.cleaned_data['password']
                try:
                    User =ads.objects.get(adsemail=email,adspassword=password)
                    request.session['ads_id'] = User.id
                    return redirect('we4')
                except ads.DoesNotExist:
                    form.add_error(None, 'Invalid username or password.')
        else:
            form = LoginForm()
        return render(request, 'login.html', {'form': form})

    if usertype=="employee":
        if request.method == 'POST':
            form = LoginForm(request.POST)
            if form.is_valid():
                email =form.cleaned_data['email']
                password =form.cleaned_data['password']
                try:
                    User =workemployee.objects.get(emusername=email,empassword=password)
                    request.session['employee_id'] = User.id
                    return redirect('we34')
                except workemployee.DoesNotExist:
                    form.add_error(None, 'Invalid username or password.')
        else:
            form = LoginForm()
        return render(request, 'login.html', {'form': form})
    if usertype=="panchayath":
        if request.method == 'POST':
            form = LoginForm(request.POST)
            if form.is_valid():
                email =form.cleaned_data['email']
                password =form.cleaned_data['password']
                try:
                    User =panchayath.objects.get(panchayath_email=email,panchayath_password=password)
                    request.session['panchayath_id'] = User.id
                    return redirect('we2')
                except panchayath.DoesNotExist:
                    form.add_error(None, 'Invalid username or password.')
        else:
            form = LoginForm()
        return render(request, 'login.html', {'form': form})

    if usertype=="admin":
        if request.method == 'POST':
            form = LoginForm(request.POST)
            if form.is_valid():
                email =form.cleaned_data['email']
                password =form.cleaned_data['password']
                try:
                    User =admin.objects.get(emailid=email,password=password)
                    request.session['admin_id'] = User.id
                    return redirect('ad')
                except admin.DoesNotExist:
                    form.add_error(None, 'Invalid username or password.')
        else:
            form = LoginForm()
        return render(request, 'login.html', {'form': form})
    

def logout(request):
    request.session.clear()
    return redirect('home')
  
 
def dashboard(request):
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('login')
    try:
        User =pub.objects.get(id=user_id)
    except pub.DoesNotExist:
        return redirect('login')
    
    return render(request,'Dashboard.html',{'ser': User})


@no_cache   
def empatt(request):
    user_id = request.session.get('ads_id')
    try:
        User =ads.objects.get(id=user_id)
    except ads.DoesNotExist:
        return redirect('home')
    emv=workemployee.objects.all().values()
    return render(request,'employeeregistered3.html',{'r':emv})



def attview(request):
    emv=empattendence.objects.all().values()
    return render(request,'attendenceview.html',{'cp':emv})


# def newemploye(request):
#     user_id = request.session.get('employee_id')
#     if request.method=='POST':
#         rdata=workemployee.objects.get(id=user_id)
#         rp=newemp(request.POST)
#         if rp.is_valid():
#             r=rp.save(commit=False)
#             r.empid=rdata.id
#             r.save()
#             return redirect('we34')
#     else:
#         rp=newemp()
#     return render(request,'newworkemployee.html',{'rp':rp})
#def empatt1(request):
    #emv=workemployee.objects.all().values()
    #return render(request,'employeeview2.html',{'r':emv})

@no_cache
def newemp7(request):
    user_id = request.session.get('employee_id')
    try:
        User =workemployee.objects.get(id=user_id)
    except workemployee.DoesNotExist:
        return redirect('home')
    emv=newwork.objects.filter(empid=user_id)
    return render(request,'newemployeeview.html',{'r':emv})

@no_cache

def publichome1(request):
    user_id = request.session.get('pub_id')
    try:
        User =pub.objects.get(id=user_id)
    except pub.DoesNotExist:
        return redirect('home')
    
    return render(request,'publichome.html',{'ser': User})
@no_cache
def panchayathhome1(request):
    user_id = request.session.get('panchayath_id')
    try:
        User =panchayath.objects.get(id=user_id)
    except panchayath.DoesNotExist:
        return redirect('home')
    
    return render(request,'panchayathhome.html',{'ser': User})
@no_cache
def employeehome1(request):
    user_id = request.session.get('employee_id')
    try:
        User =workemployee.objects.get(id=user_id)
    except workemployee.DoesNotExist:
        return redirect('home')
    
    return render(request,'employeehome.html',{'ser': User})

@no_cache
def adshome1(request):
    user_id = request.session.get('ads_id')
    try:
        User =ads.objects.get(id=user_id)
    except ads.DoesNotExist:
        return redirect('home')
    
    return render(request,'adshome.html',{'ser': User})

@no_cache
def pubprofile(request):
    user_id = request.session.get('pub_id')
    try:
        User =pub.objects.get(id=user_id)
    except pub.DoesNotExist:
        return redirect('home')
    id = request.session.get('pub_id')
    cp=pub.objects.get(id=id)
    return render(request,'publicprofile.html',{'cp':cp})

@no_cache
def adsprofile1(request):
    user_id = request.session.get('ads_id')
    try:
        User =ads.objects.get(id=user_id)
    except ads.DoesNotExist:
        return redirect('home')
    cp=ads.objects.get(id=user_id)
    return render(request,'adsprofile.html',{'q':cp})

@no_cache
def employeeprofile1(request):
    user_id = request.session.get('employee_id')
    try:
        User =workemployee.objects.get(id=user_id)
    except workemployee.DoesNotExist:
        return redirect('home')
    cp=workemployee.objects.get(id=user_id)
    return render(request,'employeeprofile.html',{'r':cp})

@no_cache
def panchayathprofile1(request):
    user_id = request.session.get('panchayath_id')
    try:
        User =panchayath.objects.get(id=user_id)
    except panchayath.DoesNotExist:
        return redirect('home')
    cp=panchayath.objects.get(id=user_id)
    return render(request,'panchayathprofile.html',{'ph':cp})

def adsproedit(request,id):
    if request.method=='POST':
        cpdata=ads.objects.get(id=id)
        cd=ads1(request.POST,instance=cpdata)
        if cd.is_valid():
            cd.save()
            return redirect('we4')
    else:
        cpdata=ads.objects.get(id=id)
        cd=ads1(instance=cpdata)
    return render(request,'adsedit.html',{'q':cd})

def publicproedit(request,id):
    if request.method=='POST':
        cpdata=pub.objects.get(id=id)
        cd=pub1(request.POST,instance=cpdata)
        if cd.is_valid():
            cd.save()
            return redirect('we1')
    else:
        cpdata=pub.objects.get(id=id)
        cd=pub1(instance=cpdata)
    return render(request,'publicedit.html',{'q':cd})

def empproedit(request,id):
    if request.method=='POST':
        cpdata=workemployee.objects.get(id=id)
        cd=emp1(request.POST,instance=cpdata)
        if cd.is_valid():
            cd.save()
            return redirect('we34')
    else:
        cpdata=workemployee.objects.get(id=id)
        cd=emp1(instance=cpdata)
    return render(request,'employeeedit.html',{'p':cd})

def panchayathedit(request):
    id = request.session.get('panchayath_id')
    if request.method=='POST':
        cpdata=panchayath.objects.get(id=id)
        cd=panchayath1(request.POST,instance=cpdata)
        if cd.is_valid():
            cd.save()
            return redirect('we2')
    else:
        cpdata=panchayath.objects.get(id=id)
        cd=panchayath1(instance=cpdata)
    return render(request,'panchayathedit.html',{'pa':cd})

def newempedit1(request,id):
    if request.method=='POST':
        cpdata=newwork.objects.get(id=id)
        cd=newemp(request.POST,instance=cpdata)
        if cd.is_valid():
            cd.save()
            return redirect('we34')
    else:
        cpdata=newwork.objects.get(id=id)
        cd=newemp(instance=cpdata)
    return render(request,'newemployeeedit.html',{'q':cd})

def newempdelete(request,id):
    cpdata=newwork.objects.get(id=id)
    cpdata.delete()
    return redirect('we34')

@no_cache
def newemployee2(request):
    user_id = request.session.get('panchayath_id')
    try:
        User =panchayath.objects.get(id=user_id)
    except panchayath.DoesNotExist:
        return redirect('home')
    cp=newwork.objects.all().values()
    return render(request,'newemployeelistview.html',{'r':cp})

@no_cache
def feed1(request):
    user_id = request.session.get('employee_id')
    # user=workemployee.objects.get(id=user_id)
    try:
        User=workemployee.objects.get(id=user_id)
    except workemployee.DoesNotExist:
        return redirect('home')
    if request.method=='POST':
        # user_id=workemployee.objects.get(id=id)
        rp=feed(request.POST)
        if rp.is_valid():
            rp=rp.save(commit=False)
            rp.currentdate=date.today()
            rp.employeeid=User.id
            rp.save()
            return redirect('we34')
    else:
        rp=feed()
    return render(request,'feedback.html',{'rp':rp})

@no_cache
def feedbacks2(request):
    user_id = request.session.get('employee_id')
    try:
        User =workemployee.objects.get(id=user_id)
    except workemployee.DoesNotExist:
        return redirect('home')
    emv=feedbacks.objects.filter(employeeid=user_id)
    return render(request,'feedbackview.html',{'r':emv})

@no_cache
def feedbacksadmin(request):
    user_id = request.session.get('admin_id')
    try:
        User =admin.objects.get(id=user_id)
    except admin.DoesNotExist:
        return redirect('home')
    emv=feedbacks.objects.all().values()
    return render(request,'feedbackadmin.html',{'r':emv})

def fededit1(request,id):
    if request.method=='POST':
        cpdata=feedbacks.objects.get(id=id)
        cd=feed(request.POST,instance=cpdata)
        if cd.is_valid():
            cd.save()
            return redirect('we34')
    else:
        cpdata=feedbacks.objects.get(id=id)
        cd=feed(instance=cpdata)
    return render(request,'feedbackedit.html',{'rp':cd})

def feddelete1(request,id):
    cpdata=feedbacks.objects.get(id=id)
    cpdata.delete()
    return redirect('we34') 

def ads2(request,id):
    myid=id
    emv=ads.objects.all().values()
    return render(request,'adsview2.html',{'r':emv,'mid':myid})

def assign12(request,id,mid):
    a=workassign()
    a.adsid=id
    a.workrequestid=mid
    a.currentdate=date.today()
    a.save()
    return redirect('fe')


@no_cache
def empatt1(request):
    user_id = request.session.get('admin_id')
    try:
        User =admin.objects.get(id=user_id)
    except admin.DoesNotExist:
        return redirect('home')
    emv=workemployee.objects.all().values()
    return render(request,'employeeviewad2.html',{'r':emv})
    
def payment(request,id):
    if request.method=='POST':
        my=workemployee.objects.get(id=id)
        rp=salary12(request.POST)
        if rp.is_valid():
            rp=rp.save(commit=False)
            rp.current_date=date.today()
            rp.worker_id=my.id
            rp.save()
            b=workemployee.objects.filter(id=id).update(payment_status=1)
            success_message='Registration was successful'
            request.session['success_message']=success_message
            return redirect('ad')
    else:
        my=workemployee.objects.get(id=id)
        rp=salary12()
    return render(request,'paymentindex.html',{'rp':rp}) 

def chat(request):
    reid=request.session.get('employee_id')
    emv=ads.objects.all().values()
    return render(request,'chatbox.html',{'r':emv,'rei':reid})
    # template=loader.get_template('chatbox.html')
    # return HttpResponse(template.render())

def chats(request,id):
    user_id = request.session.get('employee_id')
    reid=ads.objects.get(id=id)
    rei=workemployee.objects.get(id=user_id)
    if request.method=='POST':
        user_id = request.session.get('employee_id')
        rp=chat1(request.POST)
        if rp.is_valid():
            rp=rp.save(commit=False)
            rp.current_date=date.today()
            rp.sender_id=rei
            rp.reciever_id=reid
            rp.save()
            return redirect('chatss', id=id)
    else:
        emv=ads.objects.all().values()
        s=ads.objects.filter(id=id).values()
        rp=chat1()
        wo=reply12.objects.filter(reciever_id=rei,sender_id=reid)
        wp=message1.objects.filter(reciever_id=reid,sender_id=rei)
    return render(request,'chatbox.html',{'r':emv,'s':s,'form':rp,'wp':wp,'wo':wo})

@no_cache
def total(request, id):
    user_id = request.session.get('admin_id')
    try:
        User =admin.objects.get(id=user_id)
    except admin.DoesNotExist:
        return redirect('home')
    rid=id
    present_count = empattendence.objects.filter(employeeid=id, attendence='P').count()
    total_salary = present_count * 330  # Multiply by 330
    return render(request, 'totalsalary.html', {'r': present_count, 'total_salary': total_salary,'m':rid})

def chat12(request):
    user_id = request.session.get('ads_id')
    # Get the unique sender IDs
    # unique_ids = message1.objects.values_list('sender_id', flat=True).distinct(reciever_id=user_id)
    unique_ids = message1.objects.filter(reciever_id=user_id).values_list('sender_id', flat=True).distinct()

    # Create a list of dictionaries containing ID and name pairs
    users_info = [{'id': id, 'name': workemployee.objects.get(pk=id).emname} for id in unique_ids]

    print(users_info)
    
    # Pass the list of dictionaries to the template
    return render(request, 'chatboxuser.html', {'users_info': users_info})

def chat123(request,id):
    user_id = request.session.get('ads_id')
    reid=workemployee.objects.get(id=id)
    rei=ads.objects.get(id=user_id)
    if request.method=='POST':
        rp=rep1(request.POST)
        if rp.is_valid():
            rp=rp.save(commit=False)
            rp.current_date=date.today()
            rp.sender_id=rei
            rp.reciever_id=reid
            rp.save()
            return redirect('cha', id=id)
    else:
        user_id= request.session.get('ads_id')
        unique_ids = message1.objects.filter(reciever_id=user_id).values_list('sender_id', flat=True).distinct()
        s=workemployee.objects.filter(id=id).values()
        cr=rep1()
    
        wp=reply12.objects.filter(reciever_id=reid,sender_id=rei)
        mess=message1.objects.filter(reciever_id=user_id,sender_id=id)
        users_info = [{'id': id, 'name': workemployee.objects.get(pk=id).emname} for id in unique_ids]
    return render(request, 'chatboxuser.html', {'users_info': users_info,'s':s,'mess':mess,'cr':cr,'wp':wp})
    
@no_cache
def adsadmin(request):
    user_id = request.session.get('admin_id')
    try:
        User =admin.objects.get(id=user_id)
    except admin.DoesNotExist:
        return redirect('home')
    adr=ads.objects.all().values()
    return render(request,'adsadminview.html',{'q':adr})

@no_cache
def employadmin(request):
    user_id = request.session.get('admin_id')
    try:
        User =admin.objects.get(id=user_id)
    except admin.DoesNotExist:
        return redirect('home')
    adr=workemployee.objects.all().values()
    return render(request,'employeeadminview.html',{'r':adr})

@no_cache
def panchaythadmin(request):
    user_id = request.session.get('admin_id')
    try:
        User =admin.objects.get(id=user_id)
    except admin.DoesNotExist:
        return redirect('home')
    adr=panchayath.objects.all().values()
    return render(request,'panchayviewadmin.html',{'ph':adr})

@no_cache
def publicadmin(request):
    user_id = request.session.get('admin_id')
    try:
        User =admin.objects.get(id=user_id)
    except admin.DoesNotExist:
        return redirect('home')
    adr=pub.objects.all().values()
    return render(request,'publicadmin.html',{'fm':adr})


def generate_pdf(request, workentryid):
    # Retrieve the workcomplete instance based on the workentryid
    work_entry = get_object_or_404(workcomplete, id=workentryid)

    # Create a BytesIO buffer to receive the PDF data
    buffer = BytesIO()

    # Create the PDF object using ReportLab with landscape orientation
    doc = SimpleDocTemplate(buffer, pagesize=landscape(letter))

    # Define styles for the document
    styles = getSampleStyleSheet()
    style_heading = styles["Heading1"]
    style_subheading = styles["Heading2"]  # New style for subheading
    style_normal = styles["Normal"]

    # Create the content elements
    elements = []

    # Add a heading
    elements.append(Paragraph("Rural Employment Portal", style_heading))
    elements.append(Spacer(1, 12))  # Add some space below the heading

    # Add a subheading for Work Complete Details
    elements.append(Paragraph("Work Complete Details", style_subheading))
    elements.append(Spacer(1, 12))  # Add some space below the subheading

    # Add work entry details
    work_entry_details = [
        ["Work Entry ID:", str(work_entry.workentryid)],
        ["Complete Work Details:", work_entry.completeworkdetails],
        ["Current Details:", work_entry.currentdetails],
        ["To Date:", work_entry.todate.strftime('%Y-%m-%d') if work_entry.todate else 'N/A']
    ]

    # Create a table for the work entry details
    table = Table(work_entry_details, colWidths=[200, 350], hAlign="LEFT")
    table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.grey),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.whitesmoke),
        ("ALIGN", (0, 0), (-1, -1), "CENTER"),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("BOTTOMPADDING", (0, 0), (-1, 0), 12),
        ("BACKGROUND", (0, 1), (-1, -1), colors.beige),
        ("GRID", (0, 0), (-1, -1), 1, colors.black)
    ]))

    elements.append(table)

    # Build the PDF document
    doc.build(elements)

    # File response with PDF mime type
    buffer.seek(0)
    response = HttpResponse(buffer, content_type="application/pdf")
    response["Content-Disposition"] = f'attachment; filename="{workentryid}_workcomplete.pdf"'

    return response



@no_cache
def salarypass(request):
    user_id = request.session.get('ads_id')
    try:
        User =ads.objects.get(id=user_id)
    except ads.DoesNotExist:
        return redirect('home')
    b=workemployee.objects.all().values()
    
    return render(request,'salarypassed.html',{'r':b})



def attendence12(request,id):
    if request.method=='POST':
        empdata=workemployee.objects.get(id=id)
        today = date.today()
        existing_attendance = empattendence.objects.filter(employeeid=id, current_date=today)
        if not existing_attendance.exists():
            jp=takeattendence(request.POST)
            if jp.is_valid():
                jp=jp.save(commit=False)
                jp.current_date=date.today()
                jp.employeeid=empdata.id
                jp.save()
                return redirect('we3')
        else:
            a = 'Attendance for this worker on the same date already exists'
            return render(request, 'attendence.html', {'a': a})
    else:
        jp=takeattendence()
    return render(request,'attendence.html',{'m':jp})


@no_cache
def notiemploy(request):
    user_id = request.session.get('employee_id')
    try:
        User =workemployee.objects.get(id=user_id)
    except workemployee.DoesNotExist:
        return redirect('home')
    fm=notifition.objects.filter(user='EMPLOYEE')
    return render(request,'notificationemploy.html',{'fm':fm})


# def woat(request,id):
#     userid=request.session.get('Home_id')
#     # print("id",user_id)
#     if not userid:
#         return redirect('new')
#     try:
#         User=Home.objects.get(id=userid)
#     except Home.DoesNotExist:
#         return redirect('new')
#     today = date.today()
#     existing_attendance = Home7.objects.filter(WORKER_id=id, CURRENTDATE=today)

#     # if existing_attendance.exists():
#     #     a = 'Attendance for this worker on the same date already exists'
#     #     return render(request, 'workeratt.html', {'a': a})
#     if request.method=='POST':
#         c=date.today()
#         if not existing_attendance.exists():
#             fm= woratt(request.POST)
#             my=Home1.objects.get(id=id)
#             if fm.is_valid():
#                 f=fm.save(commit=False)
#                 f.WORKER_id=my.id
#                 f.CURRENTDATE=date.today()
#                 f.currentmonth = datetime.now().month
#                 f.save()
#                 return redirect("agencyworkerattenance")
#         else:
#             a = 'Attendance for this worker on the same date already exists'
#         return render(request, 'workeratt.html', {'a': a})
           
#     else:
#         my=Home1.objects.get(id=id)
#         fm=woratt()
#     return render(request,'workeratt.html',{'fm1223':fm})


# def ads2(request):
#     emv=ads.objects.all().values()
#     return render(request,'chatbox.html',{'r':emv})

# def chats(request,id):
#     emv=ads.objects.all().values()
#     s=ads.objects.filter(id=id).values()
#     rp=chat1()
#     return render(request,'chatbox.html',{'r':emv,'s':s,'form':rp})

# Create your views here.

@no_cache
def newemploye(request):
    user_id= request.session.get('employee_id')
    user=workemployee.objects.filter(id=user_id)
    print(user_id)
    try:
        User =workemployee.objects.get(id=user_id)
    except workemployee.DoesNotExist:
        return redirect('home')
    if request.method=='POST':
        rp=newemp(request.POST)
        if rp.is_valid():
            rp=rp.save(commit=False)
            rp.empid=user_id
            rp.save()
            return redirect('we34')
    else:
        rp=newemp()
    return render(request,'newworkemployee.html',{'rp':rp})
