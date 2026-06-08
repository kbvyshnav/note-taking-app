from django.shortcuts import render
from .models import Note
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.contrib import messages
from django.db.models import Q
from .forms import NoteForm

def note_list(request):

    query = request.GET.get('q', '').strip()

    notes = Note.objects.all()

    if query:
        notes = notes.filter(
            Q(title__icontains=query) | Q(content__icontains=query)
        )

    notes = notes.order_by(
        '-is_pinned',
        '-created_at'
    )

    return render(request,'notes/note_list.html',{
        'notes': notes,
        'query': query,
        'note_count': notes.count(),
    })

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
            note = form.save()
            messages.success(request, f'Note "{note.title}" was created successfully.')
            return redirect('note_list')
    else:
        form = NoteForm()

    return render(request,'notes/create_note.html',{'form':form})
    

    
def toggle_pin(request,pk):
    if request.method == 'POST':
        note = get_object_or_404(Note,pk=pk)
        note.is_pinned = not note.is_pinned
        note.save()

        if note.is_pinned:
            messages.success(request, f'Note "{note.title}" was pinned.')
        else:
            messages.success(request, f'Note "{note.title}" was unpinned.')

    return redirect('note_list')

def edit_note(request,pk):
    note = get_object_or_404(Note, pk=pk)

    if request.method == 'POST':
        form = NoteForm(request.POST, instance=note)

        if form.is_valid():
            note = form.save()
            messages.success(request, f'Note "{note.title}" was updated successfully.')
            return redirect('note_detail', pk=note.pk)

    else:
        form = NoteForm(instance=note)

    return render(request, 'notes/edit_note.html', {'form':form, 'note':note,})

def delete_note(request, pk):
    note = get_object_or_404(Note, pk=pk)

    if request.method == "POST":
        title = note.title
        note.delete()

        messages.success(request, f'Note "{title}" was deleted.')
        return redirect('note_list')
    
    return render(request, 'notes/delete_note.html', {'note': note})