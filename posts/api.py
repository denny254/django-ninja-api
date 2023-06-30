from ninja import NinjaAPI
from django.http import HttpRequest
from . models import Post
from . schemas import PostInputSchema, PostOutputSchema
from django.shortcuts import get_object_or_404
from typing import List 


api = NinjaAPI()

@api.get("/posts", response=List[PostOutputSchema])
def get_all_posts(request):
    all_posts = Post.objects.all()
    return all_posts
 

@api.post('/posts', response={201:PostOutputSchema})
def create_a_post(request, payload:PostInputSchema):
    new_post = Post.objects.create(**payload.dict())
    
    return  201, new_post 

@api.get('/post/{post_id}', response={200:PostOutputSchema})
def get_one_post(request, post_id:int):
    post = get_object_or_404(Post, pk=post_id)
    
    return 200, post


@api.put('/post/update/{post_id}', response={200:PostOutputSchema})
def update_post(request, post_id:int, payload:PostInputSchema):
    post_to_update = get_object_or_404(Post, pk=post_id)
    
    post_to_update.title = payload.title 
    post_to_update.content = payload.content 
    
    post_to_update.save()
    
    return 200, post_to_update 
    
    

@api.delete('/post/delete/{post_id}', response={204:None})
def delete_post(request, post_id:int):
    
      post_to_delete = get_object_or_404(Post, pk=post_id)     
      post_to_delete.delete()
      
      
      return 204, None 
   
