from django.urls import path
from .views import PassengerView, PassengerSingleView, TripView, TripSingleView

urlpatterns = [
    path('passenger', PassengerView.as_view()),
    path('passenger/<int:id>', PassengerSingleView.as_view()),
    path('trip', TripView.as_view()),
    path('trip/<int:id>', TripSingleView.as_view()),
]