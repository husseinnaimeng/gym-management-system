from django.urls import path
from .views import MemberCreateAPIView, WorkoutPlanCreateAPIView, MembershipCreateAPIView

urlpatterns = [
    path('member/create/', MemberCreateAPIView.as_view(), name='member-create'),
    path('workoutplan/create/', WorkoutPlanCreateAPIView.as_view(), name='workoutplan-create'),
    path('membership/create/', MembershipCreateAPIView.as_view(), name='membership-create'),
]
