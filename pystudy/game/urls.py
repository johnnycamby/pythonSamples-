from game.views import AllGamesList

__author__ = 'johnny'

from django.conf.urls import patterns, include, url

urlpatterns = patterns('game.views',
                       url(r'^invite$', 'new_invitation', name='game_invite'),
                       url(r'^invitation/(?P<pk>\d+)/$', 'accept_invitation', name='game_accept'),
                       url(r'^game/(?P<pk>\d+)/$', 'game_detail', name='game_detail'),
                       url(r'^game/(?P<pk>\d+)/do_move$', 'game_do_move', name='game_do_move'),
                       url(r'^game/all', AllGamesList.as_view())
                       )

'''
============ Regex ==============
- d = digit
- + = one or more
- d+ = one or more digit
- () = mean group
- ?P = give it a name pk
- pk is primary key capture with a Named Group
'''