# Ex.04 Design a Website for Server Side Processing
## Date:27.2.2026

## AIM:
To create a web page to calculate total bill amount with GST from price and GST percentage using server-side scripts.

## FORMULA:
Bill = P + (P * GST / 100)
<br> P --> Price (in Rupees)
<br> GST --> GST (in Percentage)
<br> Bill --> Total Bill Amount (in Rupees)

## DESIGN STEPS:

### Step 1:
Clone the repository from GitHub.

### Step 2:
Create Django Admin project.

### Step 3:
Create a New App under the Django Admin project.

### Step 4:
Create a HTML file to implement form based input and output.

### Step 5:
Create python programs for views and urls to perform server side processing.

### Step 6:
Receive input values from the form using request.POST.get().

### Step 7:
Calculate the total bill amount (including GST).

### Step 8:
Display the calculated result in the server console.

### Step 9:
Render the result to the HTML template.

### Step 10:
Publish the website in Localhost.

## PROGRAM:
~~~
math.html

<html>
    <head>
        <title>Total</title>
        <style>
            body {
    margin: 0;
    background-color: rgb(16, 11, 16);
}

.container {
    background-color: rgb(41, 213, 202);
    width: 300px;
    padding: 30px;
    border: 5px dashed rgb(226, 35, 95);

    margin: 100px auto;  
    text-align: center;
}
.container h1{
    color:blue;
}
.container h4{
    color:green;
}
        </style>
    </head>
    <body>

        <div class="container">
            <h1>TOTAL</h1>
            <h4>SATHYA PRIYAN G(25018768)</h4>
            <form method="POST">
            {% csrf_token %}
            <label>Price</label>
            <input type="text" name="Price" value="{{price}}">
            <br>
            <br>
            <label>GST</label>
            <input type="text" name="GST" value="{{gst}}">
            <br>
            <br>
            <button>Calculate</button>
            <br>
            <br>
            <label>Total price</label>
            <input type="text" name="Total" value="{{total}}">
            </form>
        </div>
    </body>
</html>

views.py

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
~~~

## OUTPUT - SERVER SIDE:

![alt text](<Screenshot (31)-1.png>)

## OUTPUT - WEBPAGE:

![alt text](<Screenshot (30).png>)

## RESULT:
The a web page to calculate total bill amount with GST from price and GST percentage using server-side scripts is created successfully.
