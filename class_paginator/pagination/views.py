from django.http.response import Http404
from django.shortcuts import render
from .models import Post
from django.views.generic import ListView


# Create your views here.
class PostListView(ListView):
    model = Post
    template_name = 'pagination/home.html'
    ordering = ['id']
    paginate_by = 2
    paginate_orphans = 1



# To handle pagination with non integer or page not exist

    # def get_context_data(self, *args, **kwargs):
    #     try:
    #         return super(PostListView, self).get_context_data(*args, **kwargs)
    #     except Http404:
    #         self.kwargs['page'] = 1
    #         return super(PostListView, self).get_context_data(*args, **kwargs)

#Or  Can use this Method also

    def paginate_queryset(self, queryset, page_size) :
        try:
            return super(PostListView, self).paginate_queryset(queryset, page_size)
        except Http404:
            self.kwargs['page'] = 1
            return super(PostListView, self).paginate_queryset(queryset, page_size)


