from django.shortcuts import render, redirect
from django.views.generic import View


from notes.models import Note

class NoteList(View):
    def get(self, request, *args, **kwargs):
        context = {
            'notes' : Note.objects.all()
        }

        return render(request, 'list.html', context)

class NoteEdit(View):
    def get(self, request, *args, **kwargs):
        selected_id = kwargs['id']
        record  = Note.objects.get(id=selected_id)
        context = {
            'note': record
        }
        return render(request, 'edit.html',context) 

    def post(self, request, *args, **kwargs):
        selected_id = kwargs['id']
        record = Note.objects.get(id=selected_id)

        title = request.POST['title']
        note = request.POST['note']


        record.title = title
        record.note = note

        record.save()

        return redirect('note_list')


class NoteAdd(View):
    def get(self, request, *args, **kwargs):
        
        
        return render(request, 'add.html',{})

    def post(self, request, *args, **kwargs):
        # define the behavior when saving or a POST request
        title = request.POST['title']
        note = request.POST['note']

        Note.objects.create(title=title, note=note)

        return redirect('note_list')

class NoteDelete(View):
    def delete(self, request, *args, **kwargs):
        pass
