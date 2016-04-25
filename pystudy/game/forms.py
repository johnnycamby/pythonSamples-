import django
from django.core.exceptions import ValidationError

__author__ = 'johnny'

from django.forms import ModelForm
from .models import Invitation, Move, BOARD_SIZE


# generate a form form db table
# ModelForm => generate html elements/ input(s) for one's form
class InvitationForm(ModelForm):
    class Meta:
        model = Invitation
        exclude = ['from_user']
        #if django.VERSION >= (1, 6):
        #fields = '__all__'

class MoveForm(ModelForm):
    class Meta:
        model = Move
        exclude = ('game', 'by_first_player', 'comment')

    def clean(self):
        game = self.instance.game
        x = self.cleaned_data.get('x')
        y = self.cleaned_data.get('y')
        if not game or not game.status == 'A' or not game.is_empty(x, y):
            raise ValidationError('Illegal move')
        return self.cleaned_data