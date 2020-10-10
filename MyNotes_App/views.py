from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import MyNotes_Model
from django.contrib import messages

from datetime import date
from django.db.models import Q

# Creating view to Display notes
def MyNotes_View(request, *args, **kwargs):
    # print(request.user.is_authenticated)
    if request.user.is_authenticated: 
        All_Notes = MyNotes_Model.objects.filter(Q(notes_username = request.user) & Q(notes_archived = False))
        return render(request,'MyNotes_DisplayNotes.html',
        {'all_notes_key': All_Notes})
    else:
        return redirect('accounts/Login')
    
# Creating view to Display Archived notes 
def MyNotes_Archived_View(request, *args, **kwargs):
    All_Notes = MyNotes_Model.objects.filter(Q(notes_username = request.user) & Q(notes_archived = True))
    return render(request, 'MyNotes_Archived.html',{'all_notes_key': All_Notes})

# Creating view to Archive notes
def MyNotes_ArchiveNote_View(request, note_id):
    Note_to_Archive = get_object_or_404(MyNotes_Model, id=note_id)
    Note_to_Archive.notes_archived = True
    Note_to_Archive.save()
    return HttpResponseRedirect('/')

# Creating a view to Restore archived notes
def MyNotes_RestoreNote_View(request, note_id):
    Note_to_Restore = get_object_or_404(MyNotes_Model, id=note_id)
    Note_to_Restore.notes_archived = False
    Note_to_Restore.save()
    return HttpResponseRedirect('/Archived')

# Creating a view to Save note
def MyNotes_SaveNote_View(request):
    if request.method == 'POST':
        Note_User = request.user
        # print(Note_User)
        Note_Favorite = request.POST.get('note-favorite', default="False")
        Note_Title = request.POST['note-title']
        Note_Description = request.POST['note-description']

        Note_Info = MyNotes_Model(notes_favorite = Note_Favorite, notes_title = Note_Title, notes_description = Note_Description, notes_created_date = date.today(), notes_username = Note_User)

        # Note_Info = MyNotes_Model(notes_title = Note_Title, notes_description = Note_Description)
        Note_Info.save()

        # messages.success(request, 'Note has been successfully saved.')
        return HttpResponseRedirect('/')

# Creating a view to Delete note
def MyNotes_DeleteNote_View(request, note_id):
    Note_to_Delete = get_object_or_404(MyNotes_Model, id=note_id)
    Note_to_Delete.delete()
    return HttpResponseRedirect('/Archived')

# Creating a view to Search functionality
def MyNotes_Search_View(request):
    # if request.method == 'POST':
    Search_string = request.GET.get('search')
    Filtered_Notes = MyNotes_Model.objects.filter(Q(notes_username = request.user) & (Q(notes_title__icontains = Search_string) | Q(notes_description__icontains = Search_string)))
    return render(request, 'MyNotes_DisplayNotes.html', {'all_notes_key': Filtered_Notes})

def MyNotes_EditNote_View(request, note_id):
    if request.method == 'POST':    
        Note_to_Fetch = get_object_or_404(MyNotes_Model, id=note_id)        
        if Note_to_Fetch.notes_username == str(request.user):
            return render(request, 'MyNotes_Edit.html', {'editable_note_key':Note_to_Fetch})
        else:
            return HttpResponse('<h3 class="text-info">404 - Object not found</h3>')

    else:
        return HttpResponse('<h3>Error occured! You can not access the note with this method</h3>')

def MyNotes_SaveChanges_View(request, note_id):
    if request.method == 'POST':
        Note_to_be_Edited = get_object_or_404(MyNotes_Model, id=note_id)
        Note_Favorite = request.POST.get('note-favorite')
        Note_Title = request.POST.get('note-title')
        Note_Description = request.POST.get('note-description')

        print(Note_Favorite)

        if Note_Favorite == 'True':
            Note_Favorite = True
        else:
            Note_Favorite = False
        
        # print(Note_Favorite)

        # if Note_to_be_Edited.notes_favorite != Note_Favorite | Note_to_be_Edited.notes_title != Note_Title |Note_to_be_Edited.notes_description != Note_Description:
        if Note_to_be_Edited.notes_title != Note_Title: 
            Note_to_be_Edited.notes_title = Note_Title
        #     Note_to_be_Edited.save(['notes_title'])

        if Note_to_be_Edited.notes_description != Note_Description:
            Note_to_be_Edited.notes_description = Note_Description
        
        Note_to_be_Edited.save()
        
        return redirect('/')
    
    else:
        return redirect('/')

def MyNotes_Grid_View(request):
    All_Notes = MyNotes_Model.objects.filter(Q(notes_username = request.user) & Q(notes_archived = False))
    return render(request, 'MyNotes_GridView.html',{'all_notes_key': All_Notes})