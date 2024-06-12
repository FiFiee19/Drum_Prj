from django.shortcuts import redirect, render
from myapp.models import Product
from django.contrib import messages
# Create your views here.
def index(req):
    all_product = Product.objects.all()
    return render(req, 'products.html',{"all_product":all_product})

def management(req):
    product_manage = Product.objects.all()
    return render(req, 'management.html',{"product_manage":product_manage})

def forms(req):
    if req.method == 'POST':
        name = req.POST['name']
        price = req.POST['price']
        images = req.FILES['images']
        product = Product.objects.create(
            name = name,
            price = price,
            images = images
        )
        product.save()
        messages.success(req,"บันทึกข้อมูลเรียบร้อย")
        return redirect('management')
    else:
        return render(req, 'forms.html')    
    
def edit(req,product_id):
    if req.method == 'POST':
        product = Product.objects.get(id=product_id)
        product.name = req.POST['name']
        product.price = req.POST['price']
        if 'images' in req.FILES:
            product.images = req.FILES['images']
        product.save()
        messages.success(req,"อัปเดตข้อมูลเรียบร้อย")
        return redirect('management')
    else:    
        product = Product.objects.get(id=product_id) 
        return render(req, 'edit.html',{"product":product})

def delete(req,product_id):
    product = Product.objects.get(id=product_id)
    product.delete()
    messages.success(req,"ลบข้อมูลเรียบร้อย")
    return redirect('management')