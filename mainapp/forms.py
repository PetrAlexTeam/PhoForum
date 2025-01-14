from django import forms
from .models import *

class AddTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'content', 'image', 'resource', 'year', 'grade', 'category', 'answer']

    def save(self, commit=True):
        task = super(AddTaskForm, self).save(commit=False)
        if commit:
            similar = Task.similar.get(task)
            print(similar)
            if similar:
                print(similar)
                raise Exception("Task is very simmilar") #TODO Shoow error msg to user
        super().save()
        return task
