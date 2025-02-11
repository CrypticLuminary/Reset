from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import PostWasteDetailsForm
from .models import PostWasteDetails


@login_required
def wastepost(request):
    if request.method == "POST":
        form = PostWasteDetailsForm(request.POST, request.FILES)
        if form.is_valid():
            waste_post = form.save(commit=False)
            waste_post.name = request.user
            waste_post.save()
            return redirect('post_list')  # Adjust redirect as needed
    else:
        form = PostWasteDetailsForm()
    
    return render(request, 'post.html', {'form': form})

def post_list(request):
    # Fetch up to 10 products
    posts = PostWasteDetails.objects.all()[:10]
    return render(request, 'product_list.html', {'posts': posts})