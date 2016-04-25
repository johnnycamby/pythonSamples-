from django.contrib.auth.models import User
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.core.urlresolvers import reverse_lazy
from game.models import Game
from django import forms
# Create your views here.

@login_required
def home(request):
    my_games = Game.objects.games_for_user(request.user)
    active_games = my_games.filter(status="A")
    finished_games = my_games.exclude(status="A")
    waiting_games = active_games.filter(next_to_move=request.user)
    other_games = active_games.exclude(next_to_move=request.user)

    invitations = request.user.invitations_received.all()

    # dictionary containing a list of game-type
    context = {
        'other_games': other_games,
        'waiting_games': waiting_games,
        'finished_games': finished_games,
        'invitations':invitations
    }
    # using 'RequestContext' to provide data to a template
    return render(request, "user/home.html", context)

# allows new users to signup for the site and create a new user account
# It inherits from 'CreateView' that is a class that uses a form to create a new model object then validate it and save it to the db
class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = "user/signup.html"
    success_url = reverse_lazy('user_home')
