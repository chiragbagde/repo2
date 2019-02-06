from django.shortcuts import render

# Create your views here.
def index(request):
    context_dict ={'text':"Time required to learn django",'time':'one month','motivate':'You can do it'}
    return render(request,"template_learning/index.html",context_dict)

def other(request):
    return render(request,"template_learning/other.html")

def relative(request):
    return render(request,"template_learning/relativeurl_template.html")
