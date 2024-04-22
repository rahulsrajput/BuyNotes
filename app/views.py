from django.http import HttpResponseRedirect
from django.shortcuts import render
from usermanage.forms import UpdateForm
from payment.models import Orders
from .models import Customer

# Create your views here.
def error_404_view(request, exception):
    return render(request, 'app/error404.html')


def home(request):
    return render(request, 'app/home.html')


def contact(request):
    return render(request, 'app/contact.html')


def dashboard(request):
    if request.user.is_authenticated:
        form = UpdateForm(instance=request.user)

        if request.method == 'POST':
            form = UpdateForm(request.POST, instance=request.user)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/dashboard')
                    

        user = request.user
        customer_obj = Customer.objects.get(user=user)
        order_objs = Orders.objects.filter(complete=True,customer=customer_obj)


        context = {
            'form':form,
            'order_objs':order_objs
        }
        return render(request, 'app/dashboard.html', context)
    
    else:
        return HttpResponseRedirect('/login')