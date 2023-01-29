from django.urls import path
from . import views
urlpatterns=[
    path('' , views.welcome, name= 'welcome'),
    path('example_learning/' , views.example_learning, name= 'example_learning'),


    path('choose_verb_group/' , views.choose_verb_group, name= 'choose_verb_group'),
    path('choose_phrase_group/' , views.choose_phrase_group, name= 'choose_phrase_group'),
    path('choose_new_thing_group/' , views.choose_new_thing_group, name= 'choose_new_thing_group'),



    path('verbs_court' , views.verbs_court, name= 'verbs_court'),
    path('verbs_restaurant' , views.verbs_restaurant, name= 'verbs_restaurant'),
    path('verbs_airport' , views.verbs_airport, name= 'verbs_airport'),
    path('verbs_hotel' , views.verbs_hotel, name= 'verbs_hotel'),

    path('phrases_say' , views.phrases_say, name= 'phrases_say'),
    path('phrases_off' , views.phrases_off, name= 'phrases_off'),
    path('phrases_afraid' , views.phrases_afraid, name= 'phrases_afraid'),

    path('new_things_me_too' , views.new_things_me_too, name= 'new_things_me_too'),
    path('new_things_ithink' , views.new_things_ithink, name= 'new_things_ithink'),
    path('new_things_very' , views.new_things_very, name= 'new_things_very'),
]