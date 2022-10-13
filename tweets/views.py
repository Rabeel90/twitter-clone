from readline import write_history_file
from turtle import back
from django.shortcuts import render
from .models import Tweet
from .forms import Tweetform
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.

def index(request):
    if request.method == 'POST':
        form = Tweetform(request.POST,request.FILES)
        if form.is_valid():
            # save cuz it's valid
            form.save()
            # Redirect to Home
            return HttpResponseRedirect('/')
        
        else:
            return HttpResponseRedirect(form.errors.as_json())
         #json=javascipt object notation
    else:
        form = Tweetform()
    
    posts = Tweet.objects.all().order_by('-created_at')
    
    return render(request, 'tweet.html', {'message': posts})


def Edit(request,tweet_id):
    post = Tweet.objects.get(id=tweet_id)
    if request.method == 'POST':
        form = Tweetform(request.POST, request.FILES,instance=post)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
        else:
            return HttpResponseRedirect(form.error.as_json())
        
    form = Tweetform()
    return render(request, 'edit.html', {'edit_message':post, 'form':form})

def delete(request,tweet_id):
    
    post = Tweet.objects.get(id=tweet_id)
    post.delete()
    
    return HttpResponseRedirect('/')

def like(request,tweet_id):
    
    post = Tweet.objects.get(id=tweet_id)
    post.likes += 1
    post.save()
    return HttpResponseRedirect('/')


        
        

            
            
    


