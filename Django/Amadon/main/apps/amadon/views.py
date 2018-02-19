from django.shortcuts import render, redirect

def index(request):
    return render(request, 'amadon/index.html')

def buy(request):
    if ['item_total'] not in request.session:
        request.session['item_total'] = 0
    if ['items_cost'] not in request.session:
        request.session['items_cost'] = 0
    if ['total_cost'] not in request.session:
        request.session['total_cost'] = 0

    product id = request.POST['product_id']
    product_catalog ={
    '1920': {"item": Dojo Shirt
    "price": 19.99},

    '9234'{"item": Dojo Sweater
    "price": 29.99},

    '9323'{"item": Dojo Cup
    "price": 4.99},

    '5411'{"item": Algorithm Book
    "price": 49.99},
    }


    purchase = {
    'quantity' = request.POST['quantity']
    'item' = request.POST['product_id']['item']
    'price' = request.POST['product_id']['price']
    }

    request.session['item'] = request.POST['product_id']
    items_cost = int(purchase['quantity']) * purchase['price']
    request.session['item_total'] = 'item_total'
    request.session['total_cost'] += 'item_total'


    return redirect('/amadon/checkout')
    # return redirect('amandon/checkout')

def cart(request):
    return render(request, 'amadon/checkout.html')
