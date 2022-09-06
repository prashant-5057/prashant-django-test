from django.urls import path

from . import views

urlpatterns = [

    path('add-event/', views.EventView.as_view(), name='add_event'),
    path('event-interest/<int:pk>/',
         views.InterestAddRemoveApi.as_view(), name="event_interest"),
]
