from django.shortcuts import render
from .forms import CreateNewList, Delete
from .models import ToDoList
from django.http import HttpResponseRedirect, HttpResponse

# Create your views here.

def home(response):
    return render(response, 'main/home.html', {})

def create(response):
    if response.method == 'POST':
        form = CreateNewList(response.POST)
        if form.is_valid():
            n = form.cleaned_data['name']
            t = ToDoList(name = n)
            t.save()
            response.user.todolist.add(t)
        return HttpResponseRedirect('/view')
    else:
        form = CreateNewList()
        print("You dont have an account. Create one now")
    return render(response, 'main/create.html', {'form':form})

def view(response):
    return render(response, 'main/view.html', {})

def list(response, id):
    ls = ToDoList.objects.get(id = id)
    if response.method == 'POST':
        if ls in response.user.todolist.all():
            if response.POST.get('save'):
                for item in ls.item_set.all():
                    if response.POST.get('c' + str(item.id)) == 'clicked':
                        item.complete = True
                    else:
                        item.complete = False
                    item.save()
                    print('Saved!')
            elif response.POST.get('newItem'):
                txt = response.POST.get('new')
                if len(txt) > 2:
                    ls.item_set.create(text = txt, complete = False)
                else:
                    print('invalid name')
                print('Added!')
    return render(response, 'main/list.html', {'ls':ls})

def dele(response):
    form = Delete()
    if response.method == 'POST':
        user = response.POST.get('del')
        ls = ToDoList.objects.get(id = int(user))
        ls.delete()
    return render(response, 'main/delete.html', {'form':form})
