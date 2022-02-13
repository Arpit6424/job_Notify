from django.shortcuts import render

from .models import Card_Model, Blog_Model
=======
from .models import Card_Model
from django.core.paginator import Paginator

  
# Create your views here.
def index(request):
   
    # render function takes argument  - request
    # and return HTML as response

    card = Card_Model.objects.all()
    return render(request, "index.html", {'card' : card})

def blog_page(request, slug):
    blog = Blog_Model.objects.get(slug = slug)
    card = Card_Model.objects.get(slug = slug)
    context = {
        "blog" : blog,
        "card": card,
    }
    return render(request, "blog.html", context=context)

    card = Card_Model.objects.all().order_by('-id')        # All Card Objects
    paginator = Paginator(card, 4, orphans=1)          # Per Page Card
    page_number = request.GET.get('page')           # Holds Current Page number Value
    page_obj = paginator.get_page(page_number)          # Renders that page whose value is passed
    return render(request, "index.html", {'card' : page_obj})
