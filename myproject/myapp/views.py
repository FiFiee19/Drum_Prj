from django.http import Http404
from django.shortcuts import redirect, render
from myapp.models import Product, ProductImage
from django.contrib import messages
from django.db.models import Q

def index(req):
    query = req.GET.get('search')
    if query:
        all_product = Product.objects.filter(Q(name__icontains=query))
    else:
        all_product = Product.objects.all()
    return render(req, 'products.html', {"all_product": all_product})

def management(req):
    product_manage = Product.objects.all()
    return render(req, 'management.html',{"product_manage":product_manage})

def forms(req):
    if req.method == 'POST':
        name = req.POST['name']
        price = req.POST['price']
        product = Product.objects.create(
            name=name,
            price=price
        )
        # ตรวจสอบและเพิ่มรูปภาพ
        if 'images' in req.FILES:
            for file in req.FILES.getlist('images'):
                ProductImage.objects.create(product=product, images=file)


        product.save()
        messages.success(req, "บันทึกข้อมูลเรียบร้อย")
        return redirect('management')
    else:
        return render(req, 'forms.html')

    
def edit(req, product_id):
    product = Product.objects.get(id=product_id)
    if req.method == 'POST':
        product.name = req.POST['name']
        product.price = req.POST['price']
        
        # ตรวจสอบว่ามีไฟล์รูปภาพถูกอัพโหลดมากับฟอร์มหรือไม่
        if 'images' in req.FILES:
            for file in req.FILES.getlist('images'):
                ProductImage.objects.create(product=product, images=file)
        
        product.save()
        messages.success(req, "อัปเดตข้อมูลเรียบร้อย")
        return redirect('management')
    else:    
        return render(req, 'edit.html', {"product": product})

def delete(req,product_id):
    product = Product.objects.get(id=product_id)
    product.delete()
    messages.success(req,"ลบข้อมูลเรียบร้อย")
    return redirect('management')

def detail_product(req, product_id):
    try:
        product = Product.objects.get(id=product_id)
    except Product.DoesNotExist:
        raise Http404("Product does not exist")
    return render(req, 'detail_product.html', {"product": product})