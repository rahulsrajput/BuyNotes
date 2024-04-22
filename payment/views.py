from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponseRedirect

from products.models import Products
from .models import Orders, Payment
from app.models import Customer


from instamojo_wrapper import Instamojo
from products.templatetags.discount_tags import discountPrice


# Create your views here.

api = Instamojo(api_key=settings.API_KEY, 
                auth_token=settings.AUTH_TOKEN,
                endpoint='https://test.instamojo.com/api/1.1/'
                )


def payment(request):

    if request.user.is_authenticated:
        if request.method == 'POST':
            uuid = request.POST['uuid']
            product = Products.objects.get(uuid=uuid)

            user = request.user
            customer = Customer.objects.get(user=user)

            #after discount amount
            amount = discountPrice(product.price, product.discount)

            # print(customer)

            order_object, created = Orders.objects.get_or_create(
                customer = customer,
                complete = False
            )

            payment_object, created = Payment.objects.get_or_create(
                order = order_object,
                is_paid = False
            )

            response = api.payment_request_create(
                amount = amount,
                purpose = product.name,
                buyer_name=customer.user,
                email=customer.user.email,
                redirect_url='http://127.0.0.1:8000/payment-success',
            )
            # print(response)

            payment_object.instamojo_id = response['payment_request']['id']
            payment_object.amount = response['payment_request']['amount']
            payment_object.status = response['payment_request']['status']
            payment_object.save()

            
            order_object.product = product
            order_object.save()

            context = {
                'product':product,
                'longurl':response['payment_request']['longurl']
            }
            return render(request, 'payment/payment.html',context)
        

    else:
        uuid = request.POST['uuid']
        product = Products.objects.get(uuid=uuid)
        context = {
            'product':product,
        }
        return render(request, 'payment/payment.html',context)            

    return HttpResponseRedirect('/products')

   


    



def paymentSuccess(request):
    if request.user.is_authenticated:
        payment_id = request.GET.get('payment_id')
        payment_status = request.GET.get('payment_status')
        instamojo_id = request.GET.get('payment_request_id')

        payment_object = Payment.objects.get(instamojo_id=instamojo_id)

        user = request.user
        customer = Customer.objects.get(user=user)
        order_object = Orders.objects.get(
            customer=customer,
            complete=False
        )
        
        if payment_status == 'Credit':
            payment_object.is_paid = True
            payment_object.status = payment_status
            payment_object.payment_id = payment_id
            payment_object.save()

            order_object.complete = True
            order_object.save()
        
        else:
            payment_object.status = payment_status
            payment_object.payment_id = payment_id
            payment_object.save()
            return render(request, 'payment/paymentFailed.html')
    
    return render(request, 'payment/paymentSuccess.html')