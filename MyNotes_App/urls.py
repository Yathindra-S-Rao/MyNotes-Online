from django.urls import path
from django.conf.urls import include
from . import views

urlpatterns = [
    path('', views.MyNotes_View),
    # path('AddNote/', MyNotes_AddNote_View),
    path('Archived/', views.MyNotes_Archived_View),
    path('ArchiveNote/<int:note_id>/', views.MyNotes_ArchiveNote_View),
    path('RestoreNote/<int:note_id>/', views.MyNotes_RestoreNote_View),
    path('SaveNote/', views.MyNotes_SaveNote_View),
    path('DeleteNote/<int:note_id>/', views.MyNotes_DeleteNote_View),
    path('Search/', views.MyNotes_Search_View),
    path('Edit/<int:note_id>/', views.MyNotes_EditNote_View),
    path('SaveChanges/<int:note_id>/', views.MyNotes_SaveChanges_View),
    path('Grid/', views.MyNotes_Grid_View),
]