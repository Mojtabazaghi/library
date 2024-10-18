from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('computer_list/',views.computer_list,name='computer_list'),
    path('monitor_list/',views.monitor_list,name='monitor_list'),
    path('add_computer/',views.add_computer,name='add_computer'),
    path('add_monitor/',views.add_monitor,name='add_monitor'),

    path('detail_computer/<int:computer_id>/',views.detail_computer,name='detail_computer'),

    path('detail_monitor/<int:monitor_id>/',views.detail_monitor,name='detail_monitor'),

    path('delete_computer/<int:computer_id>/',views.delete_computer,name='delete_computer'),


    path('delete_monitor/<int:monitor_id>/',views.delete_monitor,name='delete_monitor'),


    path('edit_computer/<int:computer_id>/',views.edit_computer,name='edit_computer'),


    path('edit_monitor/<int:monitor_id>/',views.edit_monitor,name='edit_monitor'),

    path('signup/',views.signup,name='signup'),

    path('signin/',views.singin,name='signin'),
    path('signout/',views.signout,name='signout'),

    path('about_us/',views.about_us,name='about_us'),
    path('detail_computer/<int:computer_id>/Comment/', views.add_computer_comment, name='add_computer_comment'),

    path('detail_monitor/<int:monitor_id>/Comment/', views.add_monitor_comment, name='add_monitor_comment'),
    path('error/',views.error,name='error'),














]