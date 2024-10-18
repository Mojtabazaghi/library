from django.shortcuts import render,redirect,get_object_or_404
from .models import Computer,Monitor,Comment
from django .db.models import Q
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from .forms import CommentForm



def home(request):

    is_admin=request.user.is_staff
    messages=f' Welcome {request.user.username} User ' if not is_admin else f' Welcome {request.user.username} Admin  '
    return render(request,'home.html',{'messages':messages})

def computer_list(request):
    query= request.GET.get('q')
    if query:
        computers=Computer.objects.filter(Q(computer_name__icontains=query))
         # |Q(cpu__icontains=query)|Q(ram__icontains=query)|Q(graphic__icontains=query))
    else:
         computers=Computer.objects.all()

    is_admin=request.user.is_staff
    messages=f' Welcome {request.user.username} User ' if not is_admin else f' Welcome {request.user.username} Admin '
    return render(request,'computer_list.html',{'computers':computers,'messages':messages,'query':query})


def monitor_list(request):
    query=request.GET.get('q')
    if query:
        monitors=Monitor.objects.filter(Q(monitor_name__icontains=query))
    else:
        monitors=Monitor.objects.all()
    is_admin = request.user.is_staff
    messages = f' Welcome {request.user.username} User ' if not is_admin else f' Welcome {request.user.username} Admin '
    return render(request,'monitor_list.html',{'monitors':monitors,'messages':messages,'query':query})

def add_computer(request):
    if not request.user.is_authenticated:
        return redirect('signin')
    if not request.user.is_staff:
        return redirect('home')
    if request.method=='POST':
        computer_name=request.POST.get('computer_name')
        computer_price=request.POST.get('computer_price')
        cpu=request.POST.get('cpu')
        ram=request.POST.get('ram')
        graphic=request.POST.get('graphic')
        Computer.objects.create(computer_name=computer_name,computer_price=computer_price,cpu=cpu,ram=ram,graphic=graphic)
    return render(request,'add_computer.html')

def add_monitor(request):
    if not request.user.is_authenticated:
        return redirect('signin')
    if not request.user.is_staff:
        return redirect('homr')
    if request.method=='POST':
        monitor_name=request.POST.get('monitor_name')
        monitor_price=request.POST.get('monitor_price')
        fullhd=request.POST.get('fullhd')
        oled=request.POST.get('oled')
        Monitor.objects.create(monitor_name=monitor_name,monitor_price=monitor_price,fullhd=fullhd,oled=oled)
    return render(request,'add_monitor.html')


def detail_computer(request,computer_id):
    computer=get_object_or_404(Computer,id=computer_id)
    comments=Comment.objects.filter(computer_id=computer_id).order_by('created_at')
    is_admin = request.user.is_staff
    messages = f' Welcome {request.user.username} User ' if not is_admin else f' Welcome {request.user.username} Admin '
    # comments=Comment.objects.filter(computer_id=computer_id).order_by('created_at')
    return render (request,'detail_computer.html',{'computer':computer,'messages':messages,'comments':comments})

def detail_monitor(request, monitor_id):
    monitor = get_object_or_404(Monitor, id=monitor_id)
    comments = Comment.objects.filter(monitor_id=monitor_id).order_by('created_at')
    is_admin = request.user.is_staff
    messages = f' Welcome {request.user.username} User ' if not is_admin else f' Welcome {request.user.username} Admin '
    return render(request, 'detail_monitor.html', {'monitor': monitor, 'messages': messages, 'comments': comments})

def delete_computer(request,computer_id):
    if not request.user.is_authenticated:
        return redirect('signin')
    if not request.user.is_staff:
        return redirect('hom')
    computer=get_object_or_404(Computer,id=computer_id)
    if request.method=='POST':
        computer.delete()
        Comment.objects.filter(computer_id=computer_id).delete()
        return redirect('computer_list')
    return render(request,'delete_computer.html',{'computer':computer})


def delete_monitor(request,monitor_id):
    if not request.user.is_authenticated:
        return redirect('signin')
    if not request.user.is_staff:
        return redirect('home')
    monitor=get_object_or_404(Monitor,id=monitor_id)
    if request.method=='POST':
        monitor.delete()
        Comment.objects.filter(monitor_id=monitor_id).delete()
        return redirect('monitor_list')
    return render(request,'delete_monitor.html',{'monitor':monitor})



def edit_computer(request,computer_id):
    if not request.user.is_authenticated:
        return redirect('signin')
    if not request.user.is_staff:
        return redirect('home')
    computer=get_object_or_404(Computer,id=computer_id)
    if request.method=='POST':
        computer.computer_name=request.POST.get('computer_name')
        computer.computer_price=request.POST.get('computer_price')
        computer.cpu=request.POST.get('cpu')
        computer.ram=request.POST.get('ram')
        computer.graphic=request.POST.get('graphic')
        computer.save()
        return redirect('computer_list')
    return render(request,'edit_computer.html',{'computer':computer})


def edit_monitor(request,monitor_id):
    if not request.user.is_authenticated:
        return redirect('signin')
    if not request.user.is_staff:
        return redirect('home')
    monitor=get_object_or_404(Monitor,id=monitor_id)
    if request.method=='POST':
        monitor.monitor_name=request.POST.get('monitor_name')
        monitor.monitor_price=request.POST.get('monitor_price')
        monitor.fullhd=request.POST.get('fullhd')
        monitor.oled=request.POST.get('oled')
        monitor.save()
        return redirect('monitor_list')
    return render(request,'edit_monitor.html',{'monitor':monitor})



def signup(request):
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            user=form.save()
            login(request,user)
            return redirect('home')
    else:
        form=UserCreationForm()

    return render(request,'signup.html',{'form':form})



def singin(request):
    if request.method=='POST':
        form=AuthenticationForm(request,request.POST)
        if form.is_valid():
            user=form.get_user()
            login(request,user)
            return redirect('home')
    else:
        form=AuthenticationForm()

    return render(request,'signin.html',{'form':form})


def signout(request):
    logout(request)
    return redirect('home')


def about_us(request):
    return render(request,'about_us.html')


def add_computer_comment(request,computer_id):
    if not request.user.is_authenticated:
        return redirect('signin')
    computer=get_object_or_404(Computer,id=computer_id)
    if request.method=='POST':
        form=CommentForm(request.POST)
        if form.is_valid():
            comment=form.save(commit=False)
            comment.computer_id=computer_id
            comment.username=request.user.username
            comment.save()
            return redirect('detail_computer',computer_id=computer_id)
    else:
        form=CommentForm()
    is_admin = request.user.is_staff
    messages = f' Welcome {request.user.username} User ' if not is_admin else f' Welcome {request.user.username} Admin  '
    return render(request,'add_computer_comment.html',{'form':form,'computer':computer,'messages':messages})




def add_monitor_comment(request,monitor_id):
    if not request.user.is_authenticated:
        return redirect('signin')
    monitor=get_object_or_404(Monitor,id=monitor_id)
    if request.method=='POST':
        form=CommentForm(request.POST)
        if form.is_valid():
            comment=form.save(commit=False)
            comment.monitor_id=monitor_id
            comment.username=request.user.username
            comment.save()
            return redirect('detail_monitor',monitor_id=monitor_id)
    else:
        form=CommentForm()
    is_admin = request.user.is_staff
    messages = f' Welcome {request.user.username} User ' if not is_admin else f' Welcome {request.user.username} Admin  '
    return render(request,'add_monitor_comment.html',{'form':form,'monitor':monitor, 'messages':messages})



def error(request,exception):
    return render(request,'error.html',status=404)



















