from django.urls import path
from .views import (
    AdListView, AdDetailView, AdCreateView, AdUpdateView, AdDeleteView, moderation_list, approve_ad, reject_ad)

urlpatterns = [
    path('', AdListView.as_view(), name='ad-list'),
    path('ads/<int:pk>/', AdDetailView.as_view(), name='ad-detail'),
    path('ads/new/', AdCreateView.as_view(), name='ad-create'),
    path('ads/<int:pk>/edit/', AdUpdateView.as_view(), name='ad-edit'),
    path('ads/<int:pk>/delete/', AdDeleteView.as_view(), name='ad-delete'),

    path("moderation/", moderation_list, name="moderation-list"),
    path("moderation/approve/<int:ad_id>/", approve_ad, name="approve-ad"),
    path("moderation/reject/<int:ad_id>/", reject_ad, name="reject-ad"),
]
