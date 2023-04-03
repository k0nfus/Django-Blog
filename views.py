from django.views.generic import ListView, DetailView, FormView
from django.views.generic import CreateView, UpdateView, TemplateView
from django.views.generic.detail import SingleObjectMixin
from django.urls import reverse_lazy, reverse
from django.core.paginator import Paginator

from .models import Post
from .forms import CommentForm

class BlogListView(ListView):
    model = Post
    template_name = "home.html"
    paginate_by = 5

class CommentGet(DetailView):
    model = Post
    template_name = "post_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = CommentForm()
        return context

class CommentPost(SingleObjectMixin, FormView):
    model = Post
    form_class = CommentForm
    template_name = "post_detail.html"
    
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)
    
    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.article = self.object
        comment.save()
        return super().form_valid(form)

    def get_success_url(self):
        Post = self.get_object()
        return reverse("post_detail", kwargs={"slug": Post.slug})

class BlogDetailView(DetailView):
    model = Post
    template_name = "post_detail.html"
   
    def get(self, request, *args, **kwargs):
        view = CommentGet.as_view()
        return view(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        view = CommentPost.as_view()
        return view(request, *args, **kwargs)

class BlogCreateView(CreateView):
    model = Post
    template_name = "post_new.html"
    fields = ["title", "author", "body"]

class BlogUpdateView(UpdateView):
    model = Post
    template_name = "post_edit.html"
    fields = ["title", "body"]

class AboutPageView(TemplateView):
    template_name = "about.html"

class ProjektePageView(TemplateView):
    template_name = "projekte.html"