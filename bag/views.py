from django.shortcuts import render, redirect


def view_bag(request):
    """ A view that renders the bag contents page """

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """

    # Get the quantity from the form and convert to integer
    quantity = int(request.POST.get('quantity'))
    # Get the redirect from the form
    redirect_url = request.POST.get('redirect_url')
    # Check to see if there is a bag variable in the sesssion
    # If not create one
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        bag[item_id] += quantity
    else:
        bag[item_id] = quantity

    request.session['bag'] = bag
    print(request.session['bag'])
    return redirect(redirect_url)