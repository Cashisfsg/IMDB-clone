from django.forms import Form, TextInput, CharField, Textarea

from .models import *


class MovieCommentForm(Form):
    text = CharField(label='Comment',
                     widget=Textarea(attrs={
                         'placeholder': 'Leave a comment here.',
                         'class': 'outline-none text-black-26 p-3 rounded text-base font-normal',
                         'rows': 3
                     }))