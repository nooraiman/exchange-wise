from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    amount = request.args.get('amount', default=1, type=float)
    currency = request.args.get('currency', default='USDMYR', type=str)  
    return render_template('index.html', amount=amount, currency=currency)

if __name__ == '__main__':
    app.run(debug=True)