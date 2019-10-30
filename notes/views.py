from django.shortcuts import render, redirect, get_object_or_404
from .models import Note


def note_list_view(request):
    to_do_list = Note.objects.filter(finished=False)
    finished_list = Note.objects.filter(finished=True)
    context = {'to_do_list': to_do_list, 'finished_list': finished_list}
    return render(request, "note_list.html", context)

def finish_item(request, id):
    note = get_object_or_404(Note, id=id)
    note.finished = True
    note.save()
    return redirect('note-list')

def recover_item(request, id):
    note = get_object_or_404(Note, id=id)
    note.finished = False
    note.save()
    return redirect('note-list')

def delete_item(request, id):
    note = get_object_or_404(Note, id=id)
    note.delete()
    return redirect('note-list')
