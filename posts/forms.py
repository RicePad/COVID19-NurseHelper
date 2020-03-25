from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        fields = ("message", "group")
        model = Post
    

    def __init__(self, *args, **kwargs):
        user = kwargs.pop("user", None)
        super().__init__(*args, **kwargs)
        if user is None:
            self.fields["group"].queryset = (
                Group.objects.filter(
                    pk__in=user.groups.values_list("group__pk")
                )
            )
