from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required, user_passes_test
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Ad, Category

class AdListView(ListView):
    model = Ad
    template_name = "ads/ad_list.html"
    context_object_name = "ads"

    def get_queryset(self):
        return Ad.objects.filter(status="published").order_by("-published_at")

class AdDetailView(DetailView):
    model = Ad
    template_name = 'ads/ad_detail.html'
    context_object_name = 'ad'

class AdCreateView(LoginRequiredMixin, CreateView):
    model = Ad
    fields = ["title", "description", "image", "price", "category"]
    template_name = "ads/ad_form.html"
    success_url = reverse_lazy("ad-list")

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class AdUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Ad
    fields = ["title", "description", "image", "price", "category"]
    template_name = "ads/ad_form.html"

    def test_func(self):
        return self.get_object().author == self.request.user

class AdDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Ad
    success_url = reverse_lazy("ad-list")

    def test_func(self):
        return self.get_object().author == self.request.user

@login_required
@user_passes_test(lambda u: u.is_staff)
def moderation_list(request):
    ads = Ad.objects.filter(status="moderation")
    return render(request, "ads/moderation_list.html", {"ads": ads})

@login_required
@user_passes_test(lambda u: u.is_staff)
def approve_ad(request, ad_id):
    ad = get_object_or_404(Ad, id=ad_id)
    ad.status = "published"
    ad.published_at = timezone.now()
    ad.save()
    return redirect("moderation-list")

@login_required
@user_passes_test(lambda u: u.is_staff)
def reject_ad(request, ad_id):
    ad = get_object_or_404(Ad, id=ad_id)
    ad.status = "rejected"
    ad.save()
    return redirect("moderation-list")
