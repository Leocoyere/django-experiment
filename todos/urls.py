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
    path('postendpoint', views.post_example, name='post_example')
]