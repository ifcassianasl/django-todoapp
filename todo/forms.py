from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Div, HTML, Field
from .models import Todo


class TodoForm(forms.Form):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['title'] = forms.CharField(label='Título', max_length=80)

        self.fields['todo_items'] = forms.CharField(
            widget=forms.Textarea, label='Itens')

        self.helper = FormHelper()
        self.helper.layout = Layout(
            Div(
                Field('title'), css_class="mb-3"
            ),
            Div(
                Field('todo_items', rows='4'), css_class="mb-3"
            ),
            Submit('submit', 'Salvar', css_class="btn btn-primary float-end"),
        )

    class Meta:
        model = Todo
        fields = ("title")
