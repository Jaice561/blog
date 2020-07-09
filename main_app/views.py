from django.shortcuts import render
from django.views.generic.edit import CreateView, DeleteView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Blog

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)

# Create your views here.
def home(request):
    return render(request, 'home.html')

@login_required
def blogs_index(request):
#   blogs = Blog.objects.all()
  blogs = Blog.objects.filter(user=request.user)
  return render(request, 'blogs/index.html', { 'blogs': blogs })

@login_required
def blogs_detail(request, blog_id):
  blog = Blog.objects.get(id=blog_id)
  return render(request, 'blogs/detail.html', { 'blog': blog })

class BlogCreate(LoginRequiredMixin, CreateView):
  model = Blog
  fields = '__all__'
  success_url = '/blogs/'
  def form_valid(self, form):
    form.instance.user = self.request.user  
    return super().form_valid(form)

class BlogDelete(LoginRequiredMixin, DeleteView):
  model = Blog
  success_url = '/blogs/'