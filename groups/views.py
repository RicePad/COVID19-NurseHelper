from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView, ListView, DetailView, View, CreateView, RedirectView
from django.urls import reverse
from .models import Group, GroupMember
from . import models
from django.contrib import messages
from django.db import IntegrityError


# Create your views here.
class CreateGroupView(CreateView):
    fields = ("name", "description")
    model = Group
    context_object_name = "create_group"

class SingleGroup(DetailView):
    model = Group
    context_object_name = "single_group_detail"

class ListGroups(ListView):
    model = Group
    context_object_name = "list_group"
    template_name = "group_list.html"


class JoinGroup(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        return reverse("groups:single",kwargs={"slug": self.kwargs.get("slug")})

    def get(self, request, *args, **kwargs):
        group = get_object_or_404(Group,slug=self.kwargs.get("slug"))

        try:
            GroupMember.objects.create(user=self.request.user,group=group)

        except IntegrityError:
            messages.warning(self.request,("Warning, already a member of {}".format(group.name)))

        else:
            messages.success(self.request,"You are now a member of the {} group.".format(group.name))

        return super().get(request, *args, **kwargs)

class LeaveGroup(RedirectView):
    
    def get_redirect_url(self, *args, **kwargs):
        return reverse("groups:single",kwargs={"slug": self.kwargs.get("slug")})

    def get(self, request, *args, **kwargs):

        try:

            membership = GroupMember.objects.filter(
                user=self.request.user,
                group__slug=self.kwargs.get("slug")
            ).get()

        except GroupMember.DoesNotExist:
            messages.warning(
                self.request,
                "You can't leave this group because you aren't in it."
            )
        else:
            membership.delete()
            messages.success(
                self.request,
                "You have successfully left this group."
            )
        return super().get(request, *args, **kwargs)