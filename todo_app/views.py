from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from todo_app.models import todo

# Create your views here.
def index(request):
    to_dos = todo.objects.all()
    return render(request, 'index.html', {'to_dos':to_dos})

def add(request):
    if request.method == 'GET':
        return render(request, 'add.html')
    else:
        title = request.POST['title']
        description = request.POST['description']
        
        data = todo.objects.create (title=title, description=description)
        data.save()

        return redirect ('index')

def delete(request, id):
    to_do = todo.objects.get(id=id)
    to_do.delete()
    
    return redirect('index') 

def edit(request, id):
    to_do = todo.objects.get(id=id)
    if request.method == 'GET':
       return render(request, 'edit.html', {'to_do':to_do}) 
 
    else:
        title = request.POST['title']
        description = request.POST['description']
        to_do.title = title
        to_do.description = description
        # OR to_do.title = request.POST['title']
        #    to_do>description = request.POST['description']
        to_do.save()
        return redirect('index')