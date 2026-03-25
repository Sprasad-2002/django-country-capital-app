# 🌍 Django Country-Capital App

This is a simple Django project that demonstrates how to fetch data from the backend and display it on the frontend using Django ORM and templates.

---

## 🚀 Features

* Store Country and Capital data using models
* Use ForeignKey relationships (One-to-Many)
* Fetch data from backend using Django ORM
* Display data dynamically in HTML templates
* Clean table UI for data visualization

---

## 🛠️ Tech Stack

* Python
* Django
* SQLite3
* HTML / CSS

---

## 📂 Project Structure

```
project17/
│
├── app/
│   ├── models.py
│   ├── views.py
│   ├── admin.py
│
├── templates/
│   ├── displaycapital.html
│   ├── displaycountry.html
│
├── db.sqlite3
├── manage.py
```

---

## 🧠 Models Used

### Country Model

* `conid` (Primary Key)
* `cname` (Unique)

### Capital Model

* `capid` (Primary Key)
* `capname` (Unique)
* `conid` (ForeignKey → Country)

---

## 🔄 Data Flow

1. Data is stored in the database using Django models
2. Backend fetches data using ORM:

   ```python
   Capital.objects.all()
   ```
3. Data is passed to template using context
4. Template displays data using `{% for %}` loop

---

## ▶️ How to Run

```bash
git clone https://github.com/your-username/django-country-capital-app.git
cd django-country-capital-app
python manage.py runserver
```

Open in browser:

```
http://127.0.0.1:8000/capital/
```

---

## 📸 Output

Displays a table with:

* Capital ID
* Country ID / Name
* Capital Name

---

## 🔥 Future Improvements

* Add CRUD operations (Create, Update, Delete)
* Add search & filter
* Improve UI using Bootstrap
* Add REST API

---

## ⭐ If you like this project

Give it a star ⭐ on GitHub
