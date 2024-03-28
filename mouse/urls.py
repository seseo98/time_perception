from django.urls import path
from .views import track_mouse_page, track_mouse, view_mouse_events

app_name = "mouse"
urlpatterns = [
    path('', track_mouse_page, name='track-mouse-page'),
    path('/track-mouse/', track_mouse, name='track-mouse'),
    path('/view-events/', view_mouse_events, name='view-events'),
]