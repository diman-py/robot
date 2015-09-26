# coding: utf-8
from django.shortcuts import render_to_response

def main(request):
    prod_list = {'1':{ 'name':'Cobra', 'price':'4115', 'image':'Cobra.jpg','desc':'Описание товара' }, 
                 '2':{ 'name':'Snake', 'price':'1499', 'image':'Snake.jpg','desc':'Описание товара' },
                 '3':{ 'name':'Sonata Style', 'price':'4299', 'image':'dino.jpg','desc':'Описание товара' },
                  }
    
    
    
    return render_to_response('content.html', 
                       { 'prod_list':prod_list })
    
def about(request):
    return render_to_response('about.html')

def contact(request):
    return render_to_response('contact.html')

def prod(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    
    return render_to_response('prod.html', {'numb'})