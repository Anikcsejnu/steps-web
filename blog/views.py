from django.shortcuts import render
from .models import Blog
from .form import BlogForm
from django.views.generic import DetailView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger



# Create your views here.
def blog(request):
	post_list = Blog.objects.filter(status=True).order_by('-time')
	page = request.GET.get('page', 1)
	paginator = Paginator(post_list, 1)
	try:
		posts = paginator.page(page)
	except PageNotAnInteger:
		posts = paginator.page(1)
	except EmptyPage:
		posts = paginator.page(paginator.num_pages)

	context = {
		'postlist': posts,
	}
	return render(request, 'blog/blog.html', context)


class BlogSingleDetailView(DetailView):
	model = Blog
	template_name = 'blog/blog-single.html'


def post_blog(request):
	MyBlogForm = BlogForm(request.POST, request.FILES)

	if MyBlogForm.is_valid():
         blog = Blog()
         blog.name = MyBlogForm.cleaned_data["name"]
         blog.institute = MyBlogForm.cleaned_data["institute"]
         blog.title = MyBlogForm.cleaned_data["title"]
         blog.content = MyBlogForm.cleaned_data["content"]
         blog.status = False
         blog.image = MyBlogForm.cleaned_data["image"]
         blog.save()
         return render(request, 'blog/blog.html')
	else:
		return render(request, 'blog/post_blog.html')


	