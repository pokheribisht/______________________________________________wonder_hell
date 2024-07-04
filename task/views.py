from typing import Any
from django.shortcuts import render

# Create your views here.
from django.views.generic import *
from .models import Task
from .forms import TaskFrom
from django.urls import reverse_lazy

#  Rendering the html file 
class HomeTemplate(TemplateView):
    template_name  = 'task/home.html'

class Successful(TemplateView):
    template_name = 'task/task_complition_successfuly.html'

# let creat the actual data know 
# creating the Create view which creat the task 
class CreateTask(CreateView):
    model = Task
    form_class= TaskFrom
    template_name = 'task/task_creation.html'
    success_url  = reverse_lazy('T_success')
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['feedback'] = "fuck this shit man : "
        return context
 
 



class DisplayTask(TemplateView):
    template_name = 'task/display_task'    


        



class TaskDetails(ListView):
    model = Task
    template_name = 'task/display_task.html'
    context_object_name = 'data'


from django.views.generic import DetailView
class MoreInfo(DetailView):
    model = Task
    template_name = 'task/complete_detail.html'
    context_object_name = 'task'


    

class D_detail(ListView):
    model = Task
    template_name = 'task/details.html'
    context_object_name = 'data'


class UpdateTask(UpdateView):
    model = Task
    form_class = TaskFrom
    template_name = 'task/task_creation.html'
    success_url = reverse_lazy('t_details')
    
# let delete the task  . that does't need any more : 

class TaskForDel(ListView):
    model = Task 
    template_name = 'task/delete_task.html'
    context_object_name = 'data'




class DeleteSuccess(TemplateView):
    template_name = 'task/delete_success.html'
    
class DeleteTask(DeleteView):   
    model = Task
    template_name = 'task/task_confirm_delete.html'
    success_url = reverse_lazy('del_succ')







