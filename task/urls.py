from .  import views 
from django.urls import path


urlpatterns = [

    path('', views.HomeTemplate.as_view(), name = 'home'),
    path('create/', views.CreateTask.as_view(), name = 'create'),
    path('t_/', views.Successful.as_view(), name = 'T_success'),
    path('t_details/', views.TaskDetails.as_view(), name= 't_details'),
    path('d_details/<int:pk> ', views.MoreInfo.as_view(), name = 'moreinfo'),
    path('d_detail/', views.D_detail.as_view(), name ='monalisa'),
    path('update_info/<int:pk> ', views.UpdateTask.as_view(), name = 'updateinfo'),
    path('del_su/' ,views.DeleteSuccess.as_view(), name= 'del_succ'),
    path('task_for_del/' , views.TaskForDel.as_view(), name= 'task_del'),
    path('delete_task/<int:pk> /', views.DeleteTask.as_view(), name='delete-the-task'),









    
]