'''from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)

POST 

method 

save()

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Post
from .forms import PostForm  # Import the new form
from django.contrib.auth.decorators import login_required


class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-published_date']


class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm  # Use the new form
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    form_class = PostForm  # Use the new form
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('home')

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author


from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Post
from .forms import PostForm


class PostListView(ListView):
    """
    Displays a list of all blog posts. Accessible to all users.
    """
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-published_date']


class PostDetailView(DetailView):
    """
    Displays a single blog post. Accessible to all users.
    """
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    """
    Allows a logged-in user to create a new blog post.
    """
    model = Post
    form_class = PostForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        """
        Sets the author of the post to the current user before saving.
        """
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """
    Allows the author to edit their own blog post.
    """
    model = Post
    form_class = PostForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        """
        Ensures the author field remains the same upon saving.
        """
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        """
        Tests if the logged-in user is the author of the post.
        """
        post = self.get_object()
        return self.request.user == post.author


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """
    Allows the author to delete their own blog post.
    """
    model = Post
    success_url = reverse_lazy('home')

    def test_func(self):
        """
        Tests if the logged-in user is the author of the post.
        """
        post = self.get_object()
        return self.request.user == post.author


from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Post, Comment
from .forms import PostForm, CommentForm


class PostListView(ListView):
    """
    Displays a list of all blog posts. Accessible to all users.
    """
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-published_date']


class PostDetailView(DetailView):
    """
    Displays a single blog post and its comments.
    """
    model = Post

    def get_context_data(self, **kwargs):
        """
        Adds comments and the comment form to the context.
        """
        context = super().get_context_data(**kwargs)
        post = self.get_object()
        context['comments'] = post.comments.all()
        context['comment_form'] = CommentForm()
        return context


class PostCreateView(LoginRequiredMixin, CreateView):
    """
    Allows a logged-in user to create a new blog post.
    """
    model = Post
    form_class = PostForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        """
        Sets the author of the post to the current user before saving.
        """
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """
    Allows the author to edit their own blog post.
    """
    model = Post
    form_class = PostForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        """
        Ensures the author field remains the same upon saving.
        """
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        """
        Tests if the logged-in user is the author of the post.
        """
        post = self.get_object()
        return self.request.user == post.author


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """
    Allows the author to delete their own blog post.
    """
    model = Post
    success_url = reverse_lazy('home')

    def test_func(self):
        """
        Tests if the logged-in user is the author of the post.
        """
        post = self.get_object()
        return self.request.user == post.author


class CommentCreateView(LoginRequiredMixin, CreateView):
    """
    Allows a logged-in user to create a new comment.
    """
    model = Comment
    form_class = CommentForm
    
    def form_valid(self, form):
        """
        Sets the comment's author and post before saving.
        """
        post = get_object_or_404(Post, pk=self.kwargs['pk'])
        form.instance.author = self.request.user
        form.instance.post = post
        return super().form_valid(form)
    
    def get_success_url(self):
        """
        Redirects the user back to the post's detail page after a successful comment.
        """
        return reverse_lazy('post-detail', kwargs={'pk': self.kwargs['pk']})


class CommentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """
    Allows a comment's author to edit their comment.
    """
    model = Comment
    form_class = CommentForm
    
    def test_func(self):
        """
        Tests if the logged-in user is the author of the comment.
        """
        comment = self.get_object()
        return self.request.user == comment.author

    def get_success_url(self):
        """
        Redirects the user back to the post's detail page after a successful edit.
        """
        comment = self.get_object()
        return reverse_lazy('post-detail', kwargs={'pk': comment.post.pk})


class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """
    Allows a comment's author to delete their comment.
    """
    model = Comment
    
    def test_func(self):
        """
        Tests if the logged-in user is the author of the comment.
        """
        comment = self.get_object()
        return self.request.user == comment.author

    def get_success_url(self):
        """
        Redirects the user back to the post's detail page after a successful deletion.
        """
        comment = self.get_object()
        return reverse_lazy('post-detail', kwargs={'pk': comment.post.pk})
'''

from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models import Q # Import Q object for complex queries
from .models import Post, Comment
from .forms import PostForm, CommentForm


class PostListView(ListView):
    """
    Displays a list of all blog posts. Accessible to all users.
    """
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-published_date']


class PostDetailView(DetailView):
    """
    Displays a single blog post and its comments.
    """
    model = Post

    def get_context_data(self, **kwargs):
        """
        Adds comments and the comment form to the context.
        """
        context = super().get_context_data(**kwargs)
        post = self.get_object()
        context['comments'] = post.comments.all()
        context['comment_form'] = CommentForm()
        return context


class PostCreateView(LoginRequiredMixin, CreateView):
    """
    Allows a logged-in user to create a new blog post.
    """
    model = Post
    form_class = PostForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        """
        Sets the author of the post to the current user before saving.
        """
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """
    Allows the author to edit their own blog post.
    """
    model = Post
    form_class = PostForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        """
        Ensures the author field remains the same upon saving.
        """
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        """
        Tests if the logged-in user is the author of the post.
        """
        post = self.get_object()
        return self.request.user == post.author


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """
    Allows the author to delete their own blog post.
    """
    model = Post
    success_url = reverse_lazy('home')

    def test_func(self):
        """
        Tests if the logged-in user is the author of the post.
        """
        post = self.get_object()
        return self.request.user == post.author


class CommentCreateView(LoginRequiredMixin, CreateView):
    """
    Allows a logged-in user to create a new comment.
    """
    model = Comment
    form_class = CommentForm
    
    def form_valid(self, form):
        """
        Sets the comment's author and post before saving.
        """
        post = get_object_or_404(Post, pk=self.kwargs['pk'])
        form.instance.author = self.request.user
        form.instance.post = post
        return super().form_valid(form)
    
    def get_success_url(self):
        """
        Redirects the user back to the post's detail page after a successful comment.
        """
        return reverse_lazy('post-detail', kwargs={'pk': self.kwargs['pk']})


class CommentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """
    Allows a comment's author to edit their comment.
    """
    model = Comment
    form_class = CommentForm
    
    def test_func(self):
        """
        Tests if the logged-in user is the author of the comment.
        """
        comment = self.get_object()
        return self.request.user == comment.author

    def get_success_url(self):
        """
        Redirects the user back to the post's detail page after a successful edit.
        """
        comment = self.get_object()
        return reverse_lazy('post-detail', kwargs={'pk': comment.post.pk})


class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """
    Allows a comment's author to delete their comment.
    """
    model = Comment
    
    def test_func(self):
        """
        Tests if the logged-in user is the author of the comment.
        """
        comment = self.get_object()
        return self.request.user == comment.author

    def get_success_url(self):
        """
        Redirects the user back to the post's detail page after a successful deletion.
        """
        comment = self.get_object()
        return reverse_lazy('post-detail', kwargs={'pk': comment.post.pk})


class PostSearchView(ListView):
    """
    Handles searching for posts based on title, content, or tags.
    """
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'

    def get_queryset(self):
        """
        Returns a filtered list of posts based on the search query.
        """
        query = self.request.GET.get('q')
        if query:
            return Post.objects.filter(
                Q(title__icontains=query) |
                Q(content__icontains=query) |
                Q(tags__name__icontains=query)
            ).distinct()
        return Post.objects.all()

    def get_context_data(self, **kwargs):
        """
        Adds the search query to the context.
        """
        context = super().get_context_data(**kwargs)
        context['query'] = self.request.GET.get('q')
        return context