from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///expenses.db'
db = SQLAlchemy(app)

class Expense(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    amount = db.Column(db.Float, nullable=False)
    category = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(200))

@app.route('/')
def index():
    expenses = Expense.query.order_by(Expense.date.desc()).all()
    return render_template('index.html', expenses=expenses)

@app.route('/add', methods=['GET', 'POST'])
def add_expense():
    if request.method == 'POST':
        new_expense = Expense(
            amount=float(request.form['amount']),
            category=request.form['category'],
            description=request.form['description']
        )
        db.session.add(new_expense)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('add_expense.html')

@app.route('/delete/<int:expense_id>', methods=['POST'])
def delete_expense(expense_id):
    expense = Expense.query.get_or_404(expense_id)
    db.session.delete(expense)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/api/expenses')
def get_expenses():
    expenses = Expense.query.order_by(Expense.date.desc()).all()
    return jsonify([
        {
            'id': expense.id,
            'date': expense.date.strftime('%Y-%m-%d'),
            'amount': expense.amount,
            'category': expense.category,
            'description': expense.description
        } for expense in expenses
    ])

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
