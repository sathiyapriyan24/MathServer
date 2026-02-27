from django.shortcuts import render
def Total_price(request):
    price = int(request.POST.get("Price", 0))
    gst = int(request.POST.get("GST", 0))

    total = price + (price * gst / 100) if request.method == "POST" else 0

    print("Price=", price)
    print("GST=", gst)
    print("Total=", total)

    return render(request, 'myapp/math.html', {
        'Price': price,
        'GST': gst,
        'Total': total
    })