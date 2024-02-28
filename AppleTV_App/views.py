from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Student, Signup, Signin
from .forms import StudentForm, Register, Login

# Create your views here.
def log(request):
    members= Student.objects.all
    return render(request, 'loglist.html',{'members':members})

def insert(request):
    print("insert 1 entered")
    if request.method == 'POST':
        print("if entered")
        form= Login(request.POST or None)
        print(form)
        if form.is_valid():
            print('valid')
            form.save()
            print('form data',form.cleaned_data)
        var=form.data.get('name')
        #print('var',var)
        print('form data vals', form.data.get('name'))
        print('>>',Signup.objects.all().values('Aid')[0]['Aid'])
        print("\n\n")
        
        stu= Signup.objects.all().values('Aid')
        print('>>>',stu)
        
        for i in range(len(Signup.objects.all().values('Aid'))):
            print(var, Signup.objects.all().values('Aid')[i]['Aid'])
            if (var == Signup.objects.all().values('Aid')[i]['Aid']):
                print('match')
                print(var, Signup.objects.all().values('Aid')[i]['Aid'])
                print("\n\n")
                    #form.save()
                    #return HttpResponse(request='first_page2.html')
                    #return render(request, 'show.html', {'stu': stu})
                return HttpResponseRedirect('/show3')
                
        return render(request,'fail.html',{'fail': 'Invalid'})
    
    else:
        print("Else entered")
        form= Register(request.POST)
        print(form)
        if form.is_valid():
            form.save()
            trial= form.cleaned_data['name']
            return HttpResponseRedirect('/show')
        #return render(request,'insert.html',{'form':form})
        '''
        # this is a reference for registarion page.
        if request.method == 'POST':
        form= StudentForm(request.POST)
        print(form)
        var=form.cleaned_data
        print(var['name'])
        print(Student.objects.all().values('name')[1]['name'])
        print("\n\n")
    
        if form.is_valid():
            for i in range(len(Student.objects.all().values('name'))):
                print(var['name'], Student.objects.all().values('name')[i]['name'])
                if (var['name'] == Student.objects.all().values('name')[i]['name']):
                    print('match')
                    print(var['name'], Student.objects.all().values('name')[i]['name'])
                    print("\n\n")
                    return render(request,'fail.html')
            form.save()
            return HttpResponseRedirect('/show')
        '''

    return render(request,'insert.html')
    '''
    form = StudentForm(request.POST or None)
    #stu.Stduent.objects.all()
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/show')
    return render(request,'insert.html',{'form':form})
    '''

def insert2(request):
    print("insert 2 entered")
    if request.method == 'POST':
        form= Register(request.POST)
        print('correct page',form)
        var=form.cleaned_data
        print(var['Aid'], var['pswd'])
        #print(Signup.objects.all().values('Aid')[0]['Aid'])
        #print(Signup.objects.all().values('name')[1]['name'])
        print("\n\n")
    
        if form.is_valid():
            for i in range(len(Signup.objects.all().values('Aid'))):
                print(var['Aid'], Signup.objects.all().values('Aid')[i]['Aid'])
                if (var['Aid'] == Signup.objects.all().values('Aid')[i]['Aid']):
                    #and if var['pswd'] == Signup.objects.all().values('pswd')[i]['pswd']
                    print('match')
                    print(var['Aid'], Signup.objects.all().values('Aid')[i]['Aid'])
                    print("\n\n user exists in DB")
                    return render(request, 'fail.html', {'desc': 'exists'})
            print("Yupp")
            #return render(request, 'show.html')
            form.save()
            stu= Signup.objects.all()
            print("data feed working")
            print(stu.values())
            return render(request, 'show.html', {'stu': stu})        
            #return HttpResponseRedirect('/show')
    print("Wrong page")
    return render(request, 'insert2.html')

'''
            stu = Student.objects.get(id=id)
    form = StudentForm(request.POST, instance=stu)
    if(form.is_valid()):
        form.save()
        return HttpResponseRedirect('/show')
    return render(request,'update.html',{'student':stu})
'''

def mainpage(request):
    return 

def show(request):
    stu= Signup.objects.all()       #Change to Signup

    #if not (var.name in stu and var.age in stu or var.address in stu):
    print(stu.values) #give tab space
    print("This function 1")
    return render(request,'first_page.html')
    #return render(request,'show.html',{'stu':stu})  #actual return, give tab space
    #return render(request,'fail.html')      #modified return (test)

def show3(request):
    stu= Signup.objects.all()       #Change to Signup

    #if not (var.name in stu and var.age in stu or var.address in stu):
    print(stu.values) #give tab space
    print("This function 3")
    return render(request,'first_page2.html')

def show2(request):
    #stu= Signup.objects.all()       #Change to Signup  ---------- keep alive
    print("show 2 entered")
    stu= Signup.objects.all()
    return render(request, 'show.html', {'stu': stu})
    #if not (var.name in stu and var.age in stu or var.address in stu):
    #print(stu.values) #give tab space -------- keep alive
    #print("This function 2") --------------- keep alive
    #return render(request,'insert.html') ----------- keep alive
    #return render(request,'show.html',{'stu':stu})  #actual return, give tab space
    #return render(request,'fail.html')      #modified return (test)

# URL call functions start
def tag1(request):
    return render(request, 'premieres.html')

def tag2(request):
    return render(request, 'Top Charts.html')

def tag3(request):
    return render(request, 'Popular with Fans of Ted Lasso.html')

def tag4(request):
    return render(request, 'Major League Baseball.html')

def tag5(request):
    return render(request, 'Binge Entire Seasons.html')

def tag6(request):
    return render(request, 'Top Movies.html')

def tag7(request):
    return render(request, 'Latest originals.html')



def tag11(request):
    return render(request, 'store.xhtml')

def tag12(request):
    return render(request, 'mac.xhtml')

def tag13(request):
    return render(request, 'iPad.xhtml')

def tag14(request):
    return render(request, 'iPhone.xhtml')

def tag15(request):
    return render(request, 'watch.xhtml')

def tag16(request):
    return render(request, 'AirPods.xhtml')

def tag17(request):
    return render(request, 'AppleTV.xhtml')

def tag18(request):
    return render(request, 'accesories.xhtml')

def tag19(request):
    return render(request, 'apple_store.xhtml')

def tag20(request):
    return render(request, 'support.xhtml')

def tag21(request):
    return render(request, 'cart.html')



def MLS(request):
    return render(request, 'MLS.html')

def AppleTV(request):
    return render(request, 'first_page.html')

def MLS2(request):
    return render(request, 'MLS2.html')

def AppleTV2(request):
    return render(request, 'first_page2.html')

#URL call functions end

def go(request):
    stu= Student.objects.all()
    var= Student(request.POST or None)
    #vname= Student.objects.get(name= name)
    #vage= Student.objects.get(age=age)
    if not var in stu:
        return render(request,'go.html',{'stu':stu})

    return render(request, 'fail.html')
    for x in stu:
        if not (x.name in var and x.age in var and x.address in var):
            return render(request,'go.html',{'stu':stu})
    
    return render(request, 'fail.html')
    
def get_data(name):
    vname= Signup.objects.get(name= name)
    return vname

def delete(request):
    pass

def update(request, id):
    stu = Signup.objects.get(id=id)
    form = Register(request.POST, instance=stu)
    if(form.is_valid()):
        form.save()
        return HttpResponseRedirect('/show')
    return render(request,'update.html',{'student':stu})

def delete(request, id):
    stu = Signup.objects.get(id=id)
    stu.delete()
    return HttpResponseRedirect('/show2')