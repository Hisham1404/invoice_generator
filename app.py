from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_invoice', methods=['POST'])
def generate_invoice():
    invoice_number = request.form['invoice_number']
    customer_name = request.form['customer_name']
    invoice_date = request.form['invoice_date']
    product_name = request.form['product_name']
    quantity = int(request.form['quantity'])
    price = float(request.form['price'])

    total_amount = quantity * price

    return render_template(
        'invoice.html',
        invoice_number=invoice_number,
        customer_name=customer_name,
        invoice_date=invoice_date,
        product_name=product_name,
        quantity=quantity,
        price=price,
        total_amount=total_amount
    )

if __name__ == '__main__':
    app.run(debug=True)
