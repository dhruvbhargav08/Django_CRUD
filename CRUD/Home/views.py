from django.shortcuts import render,HttpResponse,redirect
from Home.models import Employe,Department
# Create your views here.
def home(request):
    return render(request,"home.html")
def show(request):
    empdata=Employe.objects.all()
    deptdata=Department.objects.all()
    context={"empdata":empdata,"deptdata": deptdata}
    return render(request,"show.html",context)
def sendemp(request):
    if request.method=="POST":
        ID=request.POST.get("id")
        Name=request.POST.get("name")
        Department=request.POST.get("department")
        Employe(ID=ID,Name=Name,Department=Department).save()
        return render(request,"home.html")
    else:
        return HttpResponse("Page not found")
def senddept(request):
    if request.method=="POST":
        ID=request.POST.get("id")
        Name=request.POST.get("name")
        Department(ID=ID,Name=Name).save()
        return render(request,"home.html")
    else:
        return HttpResponse("Page not found")
def deleteemp(request):
    ID=request.GET.get("id")
    obj=Employe.objects.filter(ID=ID)
    obj.delete()
    return redirect("/show")
def editemp(request):
    ID=request.GET.get("id")
    data=Employe.objects.filter(ID=ID)
    Name=data[0].Name
    Department=data[0].Department
    context={
        "ID": ID,
        "Name": Name,
        "Department":Department
    }
    return render(request,"editemp.html",context)
def deletedept(request):
    ID=request.GET.get("id")
    obj=Department.objects.filter(ID=ID)
    name=obj[0].Name
    data=Employe.objects.filter(Department=name)
    for d in data :
        d.Department=""
        d.save()
    obj.delete()
    return redirect("/show")
def editdept(request):
    ID=request.GET.get("id")
    data=Department.objects.filter(ID=ID)
    Name=data[0].Name
    context={
        "ID": ID,
        "Name": Name,
    }
    return render(request,"editdept.html",context)
