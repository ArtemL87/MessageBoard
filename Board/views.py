from django.shortcuts import render
from django.views.generic import \
    ListView, DetailView, UpdateView, DeleteView
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic.edit import CreateView
from django.core.mail import send_mail
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.models import User
from .models import Post, Category, Comment
from .forms import PostForm, CommentForm

class PostList(ListView):
    model = Post
    ordering = '-time_in'
    template_name = 'posts.html'
    context_object_name = 'post'
    paginate_by = 10


class PostDetail(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'
    queryset = Post.objects.all()


@method_decorator(login_required(login_url = '/sign/login/'), name='dispatch')
class PostCreate(CreateView, PermissionRequiredMixin):
    permission_required = ('post.add_post',)
    form_class = PostForm
    model = Post
    template_name = 'post_create.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = User.objects.get(id=self.request.user.id)
        return super().form_valid(form)

    success_url = reverse_lazy('post_list')


@method_decorator(login_required(login_url = '/sign/login/'), name='dispatch')
class PostUpdate(UpdateView, PermissionRequiredMixin):
    permission_required = ('post.change_post',)
    form_class = PostForm
    model = Post
    template_name = 'post_edit.html'
    success_url = reverse_lazy('post_list')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = User.objects.get(id=self.request.user.id)
        return super().form_valid(form)

@method_decorator(login_required(login_url = '/sign/login/'), name='dispatch')
class PostDelete(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('post_list')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = User.objects.get(id=self.request.user.id)
        return super().form_valid(form)


@method_decorator(login_required(login_url = '/sign/login/'), name='dispatch')
class NewComment(CreateView, PermissionRequiredMixin):
    permission_required = ('comment.add_comment',)
    form_class = CommentForm
    model = Comment
    template_name = 'comment_edit.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user_com = User.objects.get(id=self.request.user.id)
        return super().form_valid(form)

    success_url = reverse_lazy('post_list')


@method_decorator(login_required(login_url = '/sign/login/'), name='dispatch')
class CommentList(ListView, PermissionRequiredMixin):
    model = Comment
    ordering = '-time_in'
    template_name = 'comments.html'
    context_object_name = 'comment'
    paginate_by = 10


@method_decorator(login_required(login_url = '/sign/login/'), name='dispatch')
class CommentDetail(DetailView, PermissionRequiredMixin):
    model = Comment
    template_name = 'comment.html'
    context_object_name = 'comment'
    queryset = Comment.objects.all()