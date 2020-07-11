from django.forms import ModelForm
from .models import Post,Category,Author,Comment
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ["title", "desc", "img", "author", "category"]

class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ["cat_name"]

class AuthorForm(ModelForm):
    class Meta:
        model = Author
        fields = "__all__"

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ["body"]


#REGISTER
class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

