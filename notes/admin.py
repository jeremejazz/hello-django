from django.contrib import admin
from notes.models import Note
# Register your models here.

class NoteAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'note', 'created_time', 'modified_time')
    


admin.site.register(Note, NoteAdmin)
    
