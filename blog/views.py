
from django.views.generic import ListView , DetailView
from home.models import BlogPost


class BlogListView(ListView):
    model = BlogPost
    template_name = 'blog/blog.html'
    context_object_name = 'blogs'
    paginate_by = 5


class BlogDetailView(DetailView):
    model = BlogPost
    template_name = 'blog/blog(single).html'
    context_object_name = 'blog'

    def get_object(self, queryset=None):
        slug = self.kwargs.get('slug')
        return BlogPost.objects.get(slug=slug)



