from django.shortcuts import render,HttpResponse,redirect
from .models import *


# Create your views here.
def crud_a(request):
    uid=create_crud_a_details.objects.all()
    ctx={
        'uid':uid
    }
    return render(request,'crud_a.html',ctx)

def adddata_crud_a(request):
    if request.POST:
        item_name=request.POST['name']
        item_discription=request.POST['discription']
        create_crud_a_details.objects.create(item_name=item_name,item_discription=item_discription)
        return redirect(crud_a)
    else:
        return render(request,'crud_a.html')

def editdata_crud_a(request,id):
    uid=create_crud_a_details.objects.get(id=id)
    if request.POST:
        item_name=request.POST["name"]
        item_discription=request.POST['discription']
        uid.item_name=item_name
        uid.item_discription=item_discription
        uid.save()
        return redirect(crud_a)
    else:
        return render(request,'crud_a.html')

def deletedata_crud_a(request,id):
    uid=create_crud_a_details.objects.get(id=id)
    if request.POST:
        uid.delete()
        return redirect(crud_a)
    else:
        return render(request,'crud_a.html')
    



def crud_b(request):
    uid=create_crud_b_details.objects.all()
    context={
        'uid':uid
    }
    return render(request,'crud_b.html',context)

def adddata_crud_b(request):
    if request.POST:
       name=request.POST["item_name"] 
       category=request.POST["item_category"] 
       action=request.POST["item_action"] 
       create_crud_b_details.objects.create(name=name,category=category,action=action)
       return redirect(crud_b)
    else:
        return render(request,'crud_b.html')

def editdata_crud_b(request,id):
    uid=create_crud_b_details.objects.get(id=id)
    if request.POST:
        name=request.POST["item_name"]
        category=request.POST["item_category"]
        action=request.POST["item_action"]
        uid.name=name
        uid.category=category
        uid.action=action
        uid.save()
        return redirect(crud_b)
    else:
        return render(request,'crud_b.html')
    
def deletedata_crud_b(request,id):
    uid=create_crud_b_details.objects.get(id=id)
    if request.POST:
        uid.delete()
        return redirect(crud_b)
    else:
        return render(request,'crud_b.html')
    



def crud_c(request):
    uid=create_crud_c_details.objects.all()
    ctx={
        'uid':uid
    }
    return render(request,'crud_c.html',ctx)

def adddata_crud_c(request):
    if request.POST:
        name=request.POST['name']
        discription=request.POST['discription']
        create_crud_c_details.objects.create(name=name,discription=discription)
        return redirect(crud_c)
    else:
        return render(request,'crud_c.html')

def editdata_crud_c(request,id):
    uid=create_crud_c_details.objects.get(id=id)
    if request.POST:
        name=request.POST['name']
        discription=request.POST['discription']
        uid.name=name
        uid.discription=discription
        uid.save()
        return redirect(crud_c)
    else:
        return render(request,'crud_c.html')

def deletedata_crud_c(request,id):
    uid=create_crud_c_details.objects.get(id=id)
    if request.POST:
        uid.delete()
        return redirect(crud_c)
    else:
        return render(request,'crud_c.html')
    



def crud_d(request):
    uid=create_crud_d_details.objects.all()
    ctx={ 'uid': uid}
    return render(request,'crud_d.html',ctx)

def adddata_crud_d(request):
    if request.POST:
        person_name=request.POST['person_name']
        person_emailid=request.POST['person_emailid']
        create_crud_d_details.objects.create(person_name=person_name,person_emailid=person_emailid)
        return redirect(crud_d)
    else:
        return render(request,'crud_d.html')
    
def editdata_crud_d(request,id):
    uid=create_crud_d_details.objects.get(id=id)
    if request.POST:
        person_name=request.POST['person_name']
        person_emailid=request.POST['person_emailid']
        uid.person_name=person_name
        uid.person_emailid=person_emailid
        uid.save()
        return redirect(crud_d)
    else:
        return render(request,'crud_d.html')

def deletedata_crud_d(reqeust,id):
    uid=create_crud_d_details.objects.get(id=id)
    if reqeust.POST:
        uid.delete()
        return redirect(crud_d)
    else:
        return render(reqeust,'crud_d.html')


