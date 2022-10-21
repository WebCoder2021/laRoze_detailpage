from audioop import add
from itertools import product
from multiprocessing import context
from django.shortcuts import render
from shop.servis import set_info
from shop.telegram_send import send_order
from .models import PaymentType, Product, Orders

def index(request):
    context={}
    context['products'] = Product.objects.all()
    return render(request,'index.html', context)



# Create your views here.
def detail(request,slug):
    context={}
    product = Product.objects.filter(slug=slug).first()
    context['product']=product
    context['payment_type']=PaymentType.objects.all()
    if request.method=='POST':
        print('POST')
        fio = request.POST.get('fio',False)
        phone_number = request.POST.get('phone_number',False)
        address = request.POST.get('address',False)
        payment = request.POST.get('payment',False)
        color = request.POST.get('color',False)
        size = request.POST.get('size',False)
        if fio and phone_number and address and payment and color and size:
            order = Orders.objects.create(product=product,color_id=color,size_id=size,payment_type_id=payment,full_name=fio,phone_number=phone_number,address=address)
            order.save()
            text = set_info(order.id)
            context['text'] = text
            print(text)
            send_order(text)
            context['yes'] = True
            return render(request, 'index.html',context)
        else:
            context['err'] = "Iltimos ma'lumotlarni to'liq kiritng"
            return render(request, 'index.html',context)




    return render(request, 'detail.html',context)