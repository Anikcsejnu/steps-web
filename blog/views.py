from django.shortcuts import render
from .models import Blog
from .form import BlogForm
from django.views.generic import DetailView



# Create your views here.
def blog(request):
	context = {
		'postlist':Blog.objects.filter(status=True).order_by('-time'),
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


	