from django import forms

from .models import Deck
from .models import Card

from django.contrib.auth.models import User

class DeckForm(forms.ModelForm):

    class Meta:
        model = Deck
        fields = ('title', 'description','limit_view_cards',)

class CardForm(forms.ModelForm):

    class Meta:
        model = Card
        fields = ('phrase', 'translation','level',)

class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('first_name', 'last_name','username', 'password','email',)