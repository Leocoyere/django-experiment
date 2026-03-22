from django.urls import path

from . import views

urlpatterns = [
    path('hello', views.hello_world_view, name='hello_world'),
    path('', views.hello_python_view, name='hello_python'),
    path('html', views.hello_html_view, name='hello_html'),
    path('special', views.special_view, name='special_view'),
    path('helloname/<str:name>', views.hello_path, name='hello_path'),
    path('helloquery', views.hello_query, name='hello_query'),
    path('submitendpoint', views.submit_example, name='submit_example'),
    path('postendpoint', views.post_example, name='post_example'),
    path('submitform', views.submit_form, name='submit_form'),
    path('templating', views.template_view, name='template_view'),
    path('todos', views.todos_view, name='todos_view'),
    path('person/<int:person_id>', views.person_details, name='person_details'),
    path('delete_todo/<int:todo_id>', views.delete_todo, name='delete_todo'),
    path('toggle_todo/<int:todo_id>', views.toggle_todo_done, name='toggle_todo_done'),
]