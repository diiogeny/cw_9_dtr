from django.shortcuts import get_object_or_404, redirect
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import CreateView, DeleteView
from .models import Comment
from ads.models import Ad
from django.views import View
from django.forms.models import model_to_dict
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt


class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    fields = ['text']
    template_name = 'comments/comment_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.ad = get_object_or_404(Ad, pk=self.kwargs['pk'])
        return super().form_valid(form)

class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Comment
    template_name = 'comments/comment_confirm_delete.html'

    def test_func(self):
        return self.get_object().author == self.request.user

    def get_success_url(self):
        return reverse_lazy('ad-detail', kwargs={'pk': self.object.ad.pk})

@method_decorator(csrf_exempt, name='dispatch')
class CommentCreateView(LoginRequiredMixin, View):
    def post(self, request, ad_id):
        ad = get_object_or_404(Ad, id=ad_id)
        text = request.POST.get('text')
        if not text:
            return JsonResponse({'error': 'Комментарий не может быть пустым'}, status=400)

        comment = Comment.objects.create(ad=ad, author=request.user, text=text)
        return JsonResponse(model_to_dict(comment), status=201)

@method_decorator(csrf_exempt, name='dispatch')
class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, View):
    def test_func(self):
        comment = get_object_or_404(Comment, id=self.kwargs['comment_id'])
        return self.request.user == comment.author  # Только автор может удалять

    def delete(self, request, comment_id):
        comment = get_object_or_404(Comment, id=comment_id)
        comment.delete()
        return JsonResponse({'message': 'Комментарий удален'}, status=200)