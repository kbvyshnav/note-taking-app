from django.urls import path
from .import views

urlpatterns = [
    path('',views.note_list,name='note_list'),
    path('create/',views.create_note,name='create_note'),
    path('<int:pk>/',views.note_detail,name='note_detail'),
    path('<int:pk>/pin/',views.toggle_pin,name='toggle_pin'),
    path('<int:pk>/edit/',views.edit_note, name='edit_note'),
    path('<int:pk>/delete/',views.delete_note, name='delete_note'),

]