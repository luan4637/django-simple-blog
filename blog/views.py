from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormMixin
from django.core.paginator import Paginator
from django.db.models import Count
from django.urls import reverse

from .models import Post, Category
from .forms import CommentForm

# Create your views here.
class IndexView(ListView):
    model = Post
    paginate_by = 10
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        page_number = self.request.GET.get('page')

        context = super(IndexView, self).get_context_data(**kwargs)
        context['top_posts'] = Post.objects.all().filter(published=True, pin_top=True)[:3]
        context['latest_posts'] = Paginator(Post.objects.all().filter(published=True).order_by('-created_at'), self.paginate_by).get_page(page_number)
        context['recent_posts'] = Post.objects.all().filter(published=True).order_by('-created_at')[:3]
        context['nav_categories'] = Category.objects.all()
        context['popular_categories'] = Category.objects.annotate(total_posts=Count('posts'))

        return context

class CategoryView(ListView):
    model = Post
    paginate_by = 10
    template_name = 'category.html'

    def get_context_data(self, **kwargs):
        page_number = self.request.GET.get('page')
        category = Category.objects.get(slug=self.kwargs.get('category_slug'))
        context = super(CategoryView, self).get_context_data(**kwargs)
        context['category'] = category
        context['latest_posts'] = Paginator(Post.objects.all().filter(published=True, category__in=[category.id]).order_by('-created_at'), self.paginate_by).get_page(page_number)
        context['recent_posts'] = Post.objects.all().filter(published=True).order_by('-created_at')[:3]
        context['nav_categories'] = Category.objects.all()
        context['popular_categories'] = Category.objects.annotate(total_posts=Count('posts'))

        return context

class DetailsView(FormMixin, DetailView):
    model = Post
    form_class = CommentForm
    slug_url_kwarg = 'post_slug'
    template_name = 'details.html'

    def get_success_url(self):
        return reverse('blog:post_details', kwargs={'post_slug': self.object.slug}) + '#post_comments'

    def get_context_data(self, **kwargs):
        initialComment = {'post': self.object}
        if (self.request.POST):
            initialComment['name'] = self.request.POST['name']
            initialComment['email'] = self.request.POST['email']
            initialComment['comment'] = self.request.POST['comment']

        context = super(DetailsView, self).get_context_data(**kwargs)
        context['also_like_posts'] = Post.objects.all().filter(published=True).order_by('?')[:2]
        context['recent_posts'] = Post.objects.all().filter(published=True).order_by('-created_at')[:3]
        context['nav_categories'] = Category.objects.all()
        context['popular_categories'] = Category.objects.annotate(total_posts=Count('posts'))
        context['comments'] = self.object.comment_set.all().filter(actived=True).order_by('-created_at')
        context['comment_form'] = CommentForm(initial=initialComment)

        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        form.save()
        return super(DetailsView, self).form_valid(form)

    def form_invalid(self, form):
        return super(DetailsView, self).form_invalid(form)