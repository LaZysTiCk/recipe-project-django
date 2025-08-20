from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login

# Create your views here.

def add_recipe(request):
    if request.method == "POST":
        recipe_name = request.POST.get("recipe_name")
        recipe_desc = request.POST.get("recipe_desc")
        recipe_image = request.FILES.get("recipe_image")

        Recipe.objects.create(
            recipe_name=recipe_name,
            recipe_desc=recipe_desc,
            recipe_image=recipe_image
        )
        return redirect("view_recipe")  # after adding go to list page

    return render(request, "recipes.html")


# View for Viewing All Recipes
def view_recipes(request):
    search_query = request.GET.get('search', '')  # get search text
    if search_query:
        recipes = Recipe.objects.filter(recipe_name__icontains=search_query)  # case-insensitive search
    else:
        recipes = Recipe.objects.all()

    context = {
        'recipes': recipes,
    }
    return render(request, 'view_recipe.html', context)

def delete_recipe(request, id):
    # print(id)
    querySet = Recipe.objects.get(id = id)
    querySet.delete()
    return redirect("/recipes/")

def update_recipe(request, id):
    querySet = Recipe.objects.get(id = id)
    if request.method == "POST":
        data = request.POST
        
        recipe_image = request.FILES.get("recipe_image")
        recipe_name = data.get("recipe_name")
        recipe_desc = data.get("recipe_desc")
        
        querySet.recipe_name = recipe_name
        querySet.recipe_desc = recipe_desc
        
        if recipe_image:
            querySet.recipe_image = recipe_image
            
        querySet.save()
        return redirect('/recipes/')
            
    context = {"recipe" : querySet, 'page' : 'Update Recipe'}
    return render(request,"update_recipes.html",context)

def login_page(request):
    if request.method == "POST":
        data = request.POST
        username = data.get("username")
        password = data.get("password")
        
        if User.objects.filter(username = username).exists():
            messages.error("Invalid username !!!")
            return redirect("/login/")
        
        user = authenticate(username = username, password = password)
        
        if user is None:
            messages.error("Wrong Password !!!!")
            return redirect("/login/")
        
        else:
            login(user = user)
            return redirect("/recipes/")
            
    return render(request, 'login.html' , context = {'page' : 'Login Page'})

def register(request):
    if request.method == "POST":
        data = request.POST
        
        first_name = data.get("first_name")
        last_name = data.get("last_name")
        username = data.get("username")
        password = data.get("password")
        
        user = User.objects.filter(username = username)
        
        if user.exists():
            messages.info(request, "This username is being taken already !!!!")
            return redirect("/register/")
        
        user = User.objects.create(
            first_name = first_name,
            last_name = last_name,
            username = username,
            password = password
        )
        
        user.set_password(password)
        user.save()
        messages.info(request, "You've successfully registered to our app !!!!!")
        return redirect('/register/')
        
    return render(request, 'register.html', context = {'page' : 'Sign Up Page'})