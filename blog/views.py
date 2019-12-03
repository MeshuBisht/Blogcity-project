from django.views import generic, View
from django.shortcuts import render 
from django.db.models import Count
from .models import Post

# Create your views here.
#def index(request):
#	return  render(request,"index.html" , {})
# class PostList(generic.ListView):
# 	model=Post
# 	#queryset = Post.objects.filter(status=1).order_by('-created_on')
# 	#queryset=Post.objects.order_by('?').values('title').first()
# 	template_name = "index.html"


def contact(request):
	return render(request,"contact.html",{})
def single(request):
	return  render(request,"single.html" , {})
#def technology(request):
#	return  render(request,"technology.html" , {})



	
# def nature_single(request):
# 	return  render(request,"nature_single.html" , {})	


# class foodList(generic.ListView):
# 	queryset = Post.objects.filter(category='food').order_by('-created_on')
# 	#queryset=Post.objects.order_by('?').values('title').first()
# 	template_name = "food.html"
# def food_single(request):
# 	return  render(request,"food_single.html" , {})	


# class LifeList(generic.ListView):
# 	#model=Post
# 	queryset = Post.objects.filter(category='lifestyle').order_by('-created_on')
# 	#queryset=Post.objects.order_by('?').values('title').first()
# 	template_name = "lifestyle.html"
# #def lifestyle(request):
# #	return  render(request,"lifestyle.html" , {})	    
# def life_single(request):
# 	return render(request,"life_single.html" , {})
	

# class healthList(generic.ListView):
# 	#model=Post
# 	queryset = Post.objects.filter(category='health').order_by('-created_on')
# 	#queryset=Post.objects.order_by('?').values('title').first()
# 	template_name = "health.html"		

class travelList(View):
	#model=Post
	def get(self,request):
		sset = Post.objects.filter(category='travel').order_by('-created_on')
		posts=Post.objects.all()[0:3]
		freqs=Post.objects.values('category').order_by().annotate(Count('category'))
		return render(request,'travel.html',{'sset':sset,'freqs':freqs,'posts':posts,})	

class blogpost(View):
	def get(self,request,pk):
		#img = Post.objects.filter(file_type='image')
		record = Post.objects.get(pk=pk)
		posts=Post.objects.all()[0:3]
		populars=Post.objects.order_by().values('category').distinct()
		freqs=Post.objects.values('category').order_by().annotate(Count('category'))
		return render(request,'travel_single.html',{'record': record,'posts':posts,'populars':populars,'freqs':freqs,})
class TechList(View):
	def get(self,request):
		sset = Post.objects.filter(category='technology').order_by('-created_on')
		posts=Post.objects.all()[0:3]
		freqs=Post.objects.values('category').order_by().annotate(Count('category'))
		return render(request,'technology.html',{'sset':sset,'freqs':freqs,'posts':posts,})
class sportsList(View):
	def get(self,request):
		sset = Post.objects.filter(category='sports').order_by('-created_on')
		posts=Post.objects.all()[0:3]
		freqs=Post.objects.values('category').order_by().annotate(Count('category'))
		return render(request,'sports.html',{'sset':sset,'freqs':freqs,'posts':posts,})
				                                        

class natureList(View):
	def get(self,request):
		sset = Post.objects.filter(category='nature').order_by('-created_on')
		posts=Post.objects.all()[0:3]
		freqs=Post.objects.values('category').order_by().annotate(Count('category'))
		return render(request,'nature.html',{'sset':sset,'freqs':freqs,'posts':posts,})



class worldList(View):
	def get(self,request):
		sset = Post.objects.filter(category='world').order_by('-created_on')
		posts=Post.objects.all()[0:3]
		freqs=Post.objects.values('category').order_by().annotate(Count('category'))
		return render(request,'world.html',{'sset':sset,'freqs':freqs,'posts':posts,})		


class author(View):
	def get(self,request):
		posts=Post.objects.all()[0:3]
		freqs=Post.objects.values('category').order_by().annotate(Count('category'))
		return render(request,'author.html',{'freqs':freqs,'posts':posts,})

class PostList(View):
	def get(self,request):
		nature = Post.objects.filter(category='nature')[0:4]
		world = Post.objects.filter(category='world')[0:2]
		left=Post.objects.filter(category='world')[0:1]
		right=Post.objects.filter(category='sports')[0:1]
		travel=Post.objects.filter(category='travel')[0:4]
		sports=Post.objects.filter(category='sports')[0:3]
		technology=Post.objects.filter(category='technology')[0:3]
		posts=Post.objects.all()[0:3]
		freqs=Post.objects.values('category').order_by().annotate(Count('category'))
		return render(request,'index.html',{'sports':sports,'freqs':freqs,'posts':posts,'world':world,
			                            'right':right,'travel':travel,'technology':technology,'nature':nature,'left':left})		






