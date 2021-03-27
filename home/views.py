from django.shortcuts import render
from meals.models import Meal , Category
from blog.models import Post
from aboutus.models import WhyChooseUs


def home(request):

    meals = Meal.objects.all()
    meal_list = Meal.objects.all()
    categories = Category.objects.all()
    posts = Post.objects.all()
    latest_post = Post.objects.last()
    why_choose_us = WhyChooseUs.objects.all()



    context = {
        'meals' : meals ,
        'meal_list' : meal_list ,
        'categories' : categories ,
        'posts' : posts ,
        'latest_post' : latest_post ,
        'why_choose_us' : why_choose_us ,
    }

    return render(request , 'index.html' , context)
