from django import forms
from manage_post.models import Rating

class CommentForm(forms.ModelForm):

    CHOICES = [
        (5, str("5 " + chr(11088))),
        (4, str("4 " + chr(11088))),
        (3, str("3 " + chr(11088))),
        (2, str("2 " + chr(11088))),
        (1, str("1 " + chr(11088))),
    ]

    value = forms.ChoiceField(label='calificacion',
                              choices=CHOICES,
                              widget=forms.Select())

    description = forms.CharField(required=True,
                                  label=False,
                                  widget=forms.Textarea(attrs={'rows': 5, 'cols': 70, 'placeholder': 'Ingresa tu comentario aqui'}))

    class Meta:
        model = Rating
        fields = [
            'value',
            'description',
        ]
