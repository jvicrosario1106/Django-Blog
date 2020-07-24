from django.forms import ModelForm
from .models import Post,Category,Author,Comment,Newsletter
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth.models import User



class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ["title", "desc", "img", "author", "category","completed"]

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

class NewsletterForm(ModelForm):
    class Meta:
        model = Newsletter
        fields = ["email"]


#REGISTER
class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "password1", "password2"]


class ChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ["username","first_name", "last_name"]