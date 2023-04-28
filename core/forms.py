from django import forms

from core.models import Task


class TaskForm(forms.ModelForm):
    deadline = forms.DateTimeField(
        widget=forms.widgets.DateTimeInput(attrs={"type": "datetime-local"}),
        required=False,
    )

    class Meta:
        model = Task
        fields = ["title", "content", "deadline"]
