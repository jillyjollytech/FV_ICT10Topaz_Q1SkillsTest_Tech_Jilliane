from pyscript import display, document

def create_order(e):
    document.getElementById("output").innerHTML = "" 
    prod1 = document.getElementById('item1')
    price1 = float(prod1.value) * prod1.checked
    
    prod2 = document.getElementById('item2')
    price2 = float(prod2.value) * prod2.checked

    prod3 = document.getElementById('item3')
    price3 = float(prod3.value) * prod3.checked

    prod4 = document.getElementById('item4')
    price4 = float(prod4.value) * prod4.checked

    prod5 = document.getElementById('item5')
    price5 = float(prod5.value) * prod5.checked


    subtotal = price1 + price2 + price3 + price4 + price5
    tax = subtotal * 0.12
    total = tax + subtotal

    
    a = f"Subtotal: ₱{subtotal:.2f}<br>Tax: ₱{tax:.2f}<br><b>Total:<b> ₱{total:.2f}"

    document.getElementById("output").innerHTML = a
