from django.shortcuts import render
import razorpay
from django.views.decorators.csrf import csrf_exempt

from . models import Pet
def home(request):
    if request.method=='POST':
        name = request.POST.get('name')
        breed = request.POST.get('breed')
        amount = int(request.POST.get('amount'))*100
    
        client=razorpay.Client(auth=('rzp_test_Cr9gHQCbATBCWX','4uAPJQoExnqJYqn1NaPkNUAP'))
        payment = client.order.create ({'amount':amount,'currency':'INR','payment_capture':'1'})
        print(payment)
        pet=Pet(name=name,amount=amount,payment_id=payment['id'],breed=breed)
        pet.save()
        return render(request,'home.html',{'payment':payment})

    return render(request,'home.html')
@csrf_exempt
def success(request):
    if request.method=='POST':
        a=request.POST
        order_id=''
        for key, value in a.items():
            if key =='razorpay_order_id':
                order_id=value
                break
        user = Pet.objects.filter(payment_id=order_id).first()
        user.paid=True
        user.save()
    return render (request,'success.html')