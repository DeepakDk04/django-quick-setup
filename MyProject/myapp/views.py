from django.shortcuts import render


from .models import Product, Account, Category


from .forms import  AddProductForm
# Create your views here.

def home(request):
    context = {}
    return render(request, "home.html", context)

def viewProducts(request):
    allProducts = Product.objects.all()
    context = {"allProducts":allProducts}
    return render(request, "home.html", context)

def viewOneProduct(request, id):
    
    oneProduct = Product.objects.get(id=id)
    context = {"oneProduct":oneProduct}
    return render(request, "home.html", context)


def viewAccounts(request):
    allAccounts = Account.objects.all()
    context = {"allAccounts":allAccounts}
    return render(request, "home.html", context)
    
def viewCategory(request):
    allCategorys = Category.objects.all()
    context = {"allCategorys":allCategorys}
    return render(request, "home.html", context)


def addProduct(request):
    form = AddProductForm()

    if request.method == 'POST':
        form = AddProductForm(request.POST)
        if form.is_valid():
            form.save()

    context = {'form':form}
    return render(request, "home.html", context)

def updateProduct(request, id):
    product = Product.objects.get(id=id)
    form = AddProductForm(instance=product)

    if request.method == 'POST':
        form = AddProductForm(product,request.POST)
        if form.is_valid():
            form.save()

    context = {'form':form}
    return render(request, "home.html", context)