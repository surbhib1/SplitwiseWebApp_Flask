# **📌 Expense Tracker - Flask Web App**  

A simple **Flask-based** Expense Tracker that allows you to **create groups, add users, split expenses, and track debts** dynamically through a web interface.

---

## **🚀 Features**
✅ Create and manage **groups**  
✅ Add **users** to groups  
✅ Record **expenses** and split them  
✅ View **who owes whom** dynamically  

---

## **📂 Project Structure**
```
/expense-tracker-flask
│── app.py              # Main Flask app
│── templates/          # HTML Templates (Jinja)
│   ├── index.html
│   ├── add_group.html
│   ├── add_user.html
│   ├── add_expense.html
│   ├── debts.html
│── static/             # (Optional) For CSS, JS, images
│── requirements.txt    # List of dependencies
│── README.md           # Project Guide
```

---

## **🛠 Prerequisites**
Ensure you have the following installed:
- **Python 3.x** (Check with `python --version` or `python3 --version`)
- **pip** (Python package manager, installed with Python)
- **Flask** (Will install below)
- **Git** (optional, for version control)

---

## **📥 Installation Steps**

### **1️⃣ Clone the Repository**
```bash
git clone https://github.com/your-username/expense-tracker-flask.git
cd expense-tracker-flask
```

### **2️⃣ Create a Virtual Environment (Recommended)**
This ensures dependencies don't interfere with your system Python.
```bash
python -m venv venv  # Windows
source venv/bin/activate  # Mac/Linux
```

### **3️⃣ Install Dependencies**
```bash
pip install -r requirements.txt
```
If `requirements.txt` does not exist, install Flask manually:
```bash
pip install flask
```

---

## **🚀 Running the Flask App**
Once dependencies are installed, run the application:
```bash
python app.py
```
Then, open your browser and visit:
```
http://127.0.0.1:5000/
```

---

## **🖥 Web App Pages**
| Page                 | URL Path            | Description |
|----------------------|--------------------|-------------|
| **Home**            | `/`                | Overview of groups and users |
| **Add Group**       | `/add_group`       | Create a new group |
| **Add User**        | `/add_user`        | Add users to a group |
| **Add Expense**     | `/add_expense`     | Split expenses among users |
| **View Debts**      | `/display_debts`   | See who owes whom |

---

## **📌 Notes**
- **Data Storage:** Currently, data is stored in **Python dictionaries** (in-memory). 

---

## **🎯 Future Enhancements**
  
✅ **Database Support**  

---

---

## **📜 License**
This project is **open-source** 
---

