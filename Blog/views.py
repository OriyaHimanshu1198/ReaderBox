from django.shortcuts import render , redirect , HttpResponseRedirect
from django.views import generic
from .models import Post , Contact , Comment
from .forms import PostForm , CommentForm
from django.core.paginator import Paginator


# Create your views here.

def index(request):
    post_list = Post.objects.filter(status=1).order_by('-created_on')
    
    paginator = Paginator(post_list,6)
    page = request.GET.get('page')
    post_list = paginator.get_page(page)
        

    context = {'post_list': post_list,  }
    return render(request, 'index.html', context)


'''class blogView(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')

    
    template_name = 'blog.html' 
'''    

def blogView(request):
    post_list = Post.objects.filter(status=1).order_by('-created_on')
    
    paginator = Paginator(post_list,6)
    page = request.GET.get('page')
    post_list = paginator.get_page(page)

    context = {'post_list': post_list,  }
    return render(request, 'blog.html',context)

'''class blog_Single(generic.DetailView):
    model = Post
    template_name = 'blog-single.html' 
'''
def  blog_Single(request, slug):
    post = Post.objects.get(slug = slug)
    post.views  = post.views + 1 
    post.save()
    comments = Comment.objects.filter(post=post, reply=None).order_by('-id')

    if request.method == 'POST':
        comment_form = CommentForm(request.POST or None)

        if comment_form.is_valid():
            content = request.POST.get('content')
            name = request.POST.get('name')
            email = request.POST.get('email')
            reply_id = request.POST.get('comment_id')

            comment_qs = None

            if reply_id:
                comment_qs = Comment.objects.get(id=reply_id)
            comment = Comment.objects.create(post=post, name=name , email=email , content = content , reply = comment_qs)
            comment.save()
            return redirect('Blog')
    else:
        comment_form = CommentForm()


        context = { 
        'post':post,
        'comments' : comments,
        'comment_form' : comment_form,
        } 
        return render(request, 'blog-single.html', context )
    


def contect(request):
    if request.method == 'POST' :
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
       
        contact = Contact(name= name , email=email , subject=subject , message=message )
        contact.save() 
           
    context = {}
    
    return render(request, 'submitform.html', context)

def dashboard(request):
    post_list = Post.objects.all()
    
    count = post_list.count()
    
    paginator = Paginator(post_list,7)
    page = request.GET.get('page')
    post_list = paginator.get_page(page)
           
    context = {'post_list': post_list , 'count' : count }
    return render(request, 'dashboard.html', context)


'''def createPost(request):

    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard.html')
    context = {'form' : form}
    return render(request, 'form.html', context)         

def updatePost(request, slug):

    post = Post.objects.get(slug = slug)
    form = PostForm(instance= post)
    if request.method == 'POST':
        form = PostForm(request.POST, instance= post)
        if form.is_valid():
            form.save()
            return redirect('dash')
    context = {'form' : form}
    return render(request, 'form.html', context)         


def deletePost(request, slug):
    post = Post.objects.get(slug = slug)
    
    if request.method == 'POST':        
            post.delete()
            return redirect('dashboard')
    context = {'title' : post}
    return render(request, 'delete.html', context)          


class main(generic.ListView):
    queryset = Post.objects.all()
    model = Post
    template_name = 'dashboard.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = Postfilter(self.request.GET, queryset=self.get_queryset())
        return context 

def AdminView(request):
    post_list = Post.objects.all()
    myFilter = Postfilter()
    
    context = {'post_list': post_list, 'myFilter':myFilter}
    return render(request, 'dashboard.html', context) '''