from django.urls import path
from .views import LessonListView, LessonDetailView, LessonCreateView, LessonUpdateView, LessonDeleteView


urlpatterns = [
    path('lessons/', LessonListView.as_view(), name='lesson_list'),
    path('lessons/create/', LessonCreateView.as_view(), name='lesson_create'),
    path('lessons/<slug:slug>/update/', LessonUpdateView.as_view(), name='lesson_update'),
    path('lessons/<slug:slug>/delete/', LessonDeleteView.as_view(), name='lesson_delete'),
    path('lessons/<slug:slug>/', LessonDetailView.as_view(), name='lesson_detail'),
]
