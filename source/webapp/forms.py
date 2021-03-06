from django import forms

from webapp.models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['summary', 'description', 'status', 'type_task']

# class TaskForm(forms.Form):
#     summary = forms.CharField(max_length=200, required=True, label='Заголовок',
#                               widget=forms.TextInput(attrs={'class': "form-control"}))
#     description = forms.CharField(max_length=3000, required=False, label='Описание',
#                                   widget=forms.Textarea(attrs={'class': "form-control"}))
#     status = forms.ModelChoiceField(queryset=Status.objects.all(), required=True, label='Статус', empty_label=None,
#                                     widget=forms.Select(attrs={'class': "form-control"}))
#     type_task = forms.ModelMultipleChoiceField(queryset=Task_type.objects.all(), required=True, label='Тип')
