from django.shortcuts import render
from .models import Blog
from .form import BlogForm



# Create your views here.
def blog(request):
	return render(request, 'blog/blog.html')


def blogsingle(request):
	return render(request, 'blog/blog-single.html')

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

	# if request.method == 'POST':
	# 	blog=Blog()
	# 	blog.name = request.POST.get('name')
	# 	blog.institute = request.POST.get('institute')
	# 	blog.title= request.POST.get('title')
	# 	blog.content= request.POST.get('content')
	# 	if request.POST.get('image'):
	# 		blog.image = request.FILES('image')
	# 	blog.status = False
	# 	blog.save()
	# 	return render(request, 'blog/blog.html')  

	