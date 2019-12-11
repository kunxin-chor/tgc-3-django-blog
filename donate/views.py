from django.shortcuts import render, HttpResponse
from django.conf import settings
import stripe
# Create your views here.

def ask_for_donate(request):
    return render(request, 'donate/ask.template.html')
    
    
def donate(request):
    if request.method == 'GET':  
       amount = request.GET['amount'] # same as request.forms.get('amount') or request.forms['amount'] in Flask
       stripe_publishable_key = settings.STRIPE_PUBLISHABLE_KEY
       return render(request, 'donate/donate.template.html', {
            'publishable_key':stripe_publishable_key,
            'amount_in_dollars':amount,
            'amount':int(amount)*100,
        })
    else:
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe_token = request.POST["stripeToken"]
        charge = stripe.Charge.create(amount=request.POST["amount"],
            currency='usd',
            source=stripe_token
        )
        return HttpResponse("Thank you for your donation")