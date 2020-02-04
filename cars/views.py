
from django.shortcuts import render, redirect  
from cars.forms import CarForm,EditForm,MoveForm
from cars.models import Car  

# Create your views here.  
def carview(request):  
    if request.method == "POST":  
        form = CarForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/show')  
            except:  
                pass  
    else:  
        form = CarForm
    return render(request,'index.html',{'form':form})  
def show(request):  
    cars = Car.objects.all()  
    return render(request,"show.html",{'cars':cars})  
def edit(request, id):  
    car = Car.objects.get(cid=id)  
    return render(request,'edit.html', {'car':car})  

def destroy(request, id):  
    car = Car.objects.get(cid=id)  
    car.delete()  
    return redirect("/show")  

def move(request,id):
    car1 = Car.objects.get(cid=id)
    form = MoveForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            sid = form.cleaned_data['sid']
            car2 = Car.objects.get(cid=sid)
            temp1 = Car.objects.filter(cid=id)
            temp2 = Car.objects.filter(cid=sid)
            temp1.update(cname = car2.cname, ccolor = car2.ccolor)
            temp2.update(cname = car1.cname, ccolor = car1.ccolor)
            return redirect("/show")
   
    return render(request,'move.html', {'form':form,'car':car1})

def update(request, id):  
    car = Car.objects.get(cid=id)  
    form = EditForm(request.POST, instance = car)  
    if form.is_valid():  
        form.save()
        return redirect("/show")  
    return render(request, 'edit.html', {'form': form})  