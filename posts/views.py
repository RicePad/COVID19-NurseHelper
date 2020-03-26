from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import (TemplateView, ListView, DetailView, 
                                 View, CreateView, RedirectView, DeleteView)
from django.contrib import messages                       
from django.http import Http404
from braces.views import SelectRelatedMixin

from .forms import PostForm
from .models import Post
from django.contrib.auth import get_user_model

User = get_user_model()
# Create your views here.

class PostListView(ListView):
    model = Post
    select_related = ("user", "group")
    context_object_name = "post_list"
    template_name = "post_list.html"


class UserPosts(ListView):
    model = Post
    template_name = "user_post_list.html"

    def get_queryset(self):
        try:
            self.post_user = User.objects.prefetch_related("posts").get(
                username__iexact=self.kwargs.get("username")
            )
        except User.DoesNotExist:
            raise Http404
        else:
            return self.post_user.posts.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["post_user"] = self.post_user
        return context

class PostDetailView(SelectRelatedMixin, DetailView):
    model = Post
    select_related = ("user", "group")
    template_name = "post_detail.html"

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(
            user__username__iexact=self.kwargs.get("username")
        )

class PostCreateView(LoginRequiredMixin, CreateView):
    fields = ('message','group')
    model = Post
    template_name = "post_form.html"

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)

class DeletePostView(LoginRequiredMixin, SelectRelatedMixin, DeleteView):
    model = Post
    select_related = ("user", "group")
    success_url = reverse_lazy("posts:all")
    template_name = "post_confirm_delete.html"
    
    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user_id=self.request.user.id)

    def delete(self, *args, **kwargs):
        messages.success(self.request, "Post Deleted")
        return super().delete(*args, **kwargs)

    
    



