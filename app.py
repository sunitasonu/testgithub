from flask import Flask, render_template, request
import razorpay

app = Flask(__name__)

# Replace with your actual Razorpay credentials
razorpay_client = razorpay.Client(auth=("rzp_test_gFwKPq0IjKRlDC", "q7tzMliPP8HBpily2drUwEMq"))

@app.route('/')
def home():
    # Amount in paise (e.g., ₹500 = 50000)
    payment = razorpay_client.order.create({
        "amount": 50000,
        "currency": "INR",
        "payment_capture": 1
    })
    return render_template('index.html', payment=payment, key_id="rzp_test_gFwKPq0IjKRlDC")

@app.route('/payment/sunita', methods=['POST'])
def payment_success():
    data = request.form
    print("Payment successful:", data)
    return "Payment was successful!"

if __name__ == '__main__':
    app.run(debug=False)
