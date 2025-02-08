from django.urls import path
from .views import CommentCreateView, CommentDeleteView

urlpatterns = [
    path("<int:pk>/comment/", CommentCreateView.as_view(), name="comment-create"),
    path("comment/<int:pk>/delete/", CommentDeleteView.as_view(), name="comment-delete"),
]
