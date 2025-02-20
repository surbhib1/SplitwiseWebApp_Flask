from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Dictionary to store groups, users, and their expenses
groups = {}
debts = {}

@app.route('/')
def home():
    """Home page with options"""
    return render_template('index.html', groups=groups, debts=debts)

@app.route('/add_group', methods=['GET', 'POST'])
def add_group():
    """Add a new group"""
    if request.method == 'POST':
        group_name = request.form['group_name']
        if group_name in groups:
            return "Group already exists!", 400
        groups[group_name] = {}
        return redirect(url_for('home'))
    return render_template('add_group.html')

@app.route('/add_user', methods=['GET', 'POST'])
def add_user():
    """Add users under a specific group"""
    if request.method == 'POST':
        group_name = request.form['group_name']
        username = request.form['username']

        if group_name not in groups:
            return "Group does not exist!", 400

        if username in groups[group_name]:
            return "User already exists in this group!", 400

        groups[group_name][username] = 0  # Default expense is 0
        return redirect(url_for('home'))

    return render_template('add_user.html', groups=groups)

@app.route('/add_expense', methods=['GET', 'POST'])
def add_expense():
    """Add and split expenses among selected users"""
    if request.method == 'POST':
        group_name = request.form['group_name']
        payer = request.form['payer']
        amount = float(request.form['amount'])
        selected_users = request.form.getlist('selected_users')

        if group_name not in groups or payer not in groups[group_name]:
            return "Group or payer does not exist!", 400

        if not selected_users:
            return "No users selected for splitting!", 400

        split_amount = amount / len(selected_users)

        # Update expenses
        for user in selected_users:
            groups[group_name][user] += split_amount
            if user != payer:
                debts.setdefault(user, {}).setdefault(payer, 0)
                debts[user][payer] += split_amount

        return redirect(url_for('home'))

    return render_template('add_expense.html', groups=groups)

@app.route('/display_debts')
def display_debts():
    """Display outstanding debts"""
    return render_template('debts.html', debts=debts)

if __name__ == '__main__':
    app.run(debug=True)

