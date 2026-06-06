from django.shortcuts import render
from .models import Note
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from .forms import NoteForm

def note_list(request):

    notes = Note.objects.all().order_by(
        '-is_pinned',
        '-created_at'
    )
    return render(request,'notes/notes_list.html',{'notes': notes})

def note_detail(request, pk):
    
    note = get_object_or_404(
        Note,
        pk=pk
    )
    return render(request,'notes/note_detail.html',{'note': note})

def create_note(request):

    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('note_list')
        else:
            form.Noteform()

        return redirect(request,'notes/create_note.html',{'form':form})
    
def toggle_pin(request,pk):
    if request.method == 'POST':
        note = get_object_or_404(Note,pk=pk)
        note.is_pinned = not note.is_pinned
        note.save()

    return redirect('note_list')