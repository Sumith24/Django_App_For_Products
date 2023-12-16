from django.shortcuts import render
from .models import Products
from django.http import HttpResponseRedirect, HttpResponse

# Home

def home(request):
    all_product = Products.objects.all().order_by('-created_at')
    return render(request, 'home.html', {"products": all_product})


# Add Product
def add_product(request):
    if request.method == 'POST':
        if request.POST.get('product')\
            and request.POST.get('purchase')\
            and request.POST.get('sale')\
            and request.POST.get('qty')\
            and request.POST.get('gender')\
            or request.POST.get('note'):
            product = Products()
            product.product = request.POST.get('product')
            product.purchase = request.POST.get('purchase')
            product.sale = request.POST.get('sale')
            product.qty = request.POST.get('qty')
            product.gender = request.POST.get('gender')
            product.note = request.POST.get('note')

            product.save()

            return HttpResponseRedirect('/')
    else:
        return render(request, 'add.html')

# view the product individually
def view_product(request, product_id):
    product = Products.objects.get(id=product_id)
    if product != None:
        return render(request, 'edit.html', {"product":product})


# Edit product
def edit_product(request, product_id):
    if request.method == 'POST':
        product = Products.objects.get(id = request.POST.get('id'))
        if product != None:
            product.product = request.POST.get('product')
            product.purchase = request.POST.get('purchase')
            product.sale = request.POST.get('sale')
            product.qty = request.POST.get('qty')
            product.gender = request.POST.get('gender')
            product.note = request.POST.get('note')
            product.save()
            return HttpResponseRedirect('/')
    else:
        product = Products.objects.get(id = product_id)
        return render(request, 'edit.html', {'product':product})

# Delete product
def delete_product(request, product_id):
    product = Products.objects.get(id=product_id)
    product.delete()
    return HttpResponseRedirect('/')


