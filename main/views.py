from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Task

from django.views.generic import CreateView, UpdateView, DeleteView

from .forms import TaskForm

# Create your views here.
def home(request):
    tasks = Task.objects.all()
    task_form = TaskForm()
    print(task_form)
    return render(request, 'base.html', {'tasks': tasks, 'task_form': task_form })

def add_task(request):
  # create a ModelForm instance using the data in request.POST
  form = TaskForm(request.POST)
  # validate the form
  print(form)
  if form.is_valid():
    # don't save the form to the db until it
    # has the cat_id assigned
    new_task = form.save(commit=False)
    new_task.id = id
    new_task.save()
  return redirect('base.html') # id=id






# class TaskCreate(CreateView):
#     model = Task
#     fields = ['description', 'time', 'person']
#     success_url = '/'
#     def form_valid(self, form):
#     # Assign the logged in user (self.request.user)
#         form.instance.user = self.request.user  # form.instance is the cat
#     # Let the CreateView do its job as usual
#         return super().form_valid(form)



# class TaskList(ListView):
#     model = Task