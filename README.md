
## 🚀 Razorpay API Integration in Django

This repository demonstrates how to integrate Razorpay payment gateway in a Django application.

### 📌 Features
- Generate Razorpay payment links
- Capture payments
- Verify payment signatures
- Handle webhooks for payment status updates

---

## 🛠️ Installation

### 1️⃣ Clone the repository
```sh
git clone https://github.com/yourusername/razorpay_api_integration_django.git
cd razorpay_api_integration_django
```

### 2️⃣ Create a virtual environment and activate it
```sh
python -m venv env
source env/bin/activate  # For macOS/Linux
env\Scripts\activate     # For Windows
```

### 3️⃣ Install dependencies
```sh
pip install -r requirements.txt
```


---

## 🚀 Usage

### 1️⃣ Run migrations
```sh
python manage.py migrate
```

### 2️⃣ Start the Django development server
```sh
python manage.py runserver
```

### 3️⃣ API Endpoints

| Method | Endpoint | Description |
|--------|---------|-------------|
| `POST` | `/create-order/` | Create a new Razorpay order |
| `POST` | `/verify-payment/` | Verify payment signature |
| `POST` | `/webhook/` | Handle webhook events |

---

## 🔧 Configuration

### ✅ Add Razorpay API keys in Django settings
```python
# settings.py
import os

RAZORPAY_KEY_ID = os.getenv("RAZORPAY_KEY_ID")
RAZORPAY_KEY_SECRET = os.getenv("RAZORPAY_KEY_SECRET")
```

### ✅ Install required libraries
```sh
pip install razorpay django-dotenv
```

### ✅ Create Razorpay client in Django views
```python
import razorpay
from django.conf import settings

client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))
```

---

## 📜 License
This project is licensed under the MIT License.

---

## 💡 Author
👤 **Your Name**  
📧 aakashpc123@gmail.com  
🔗 [LinkedIn](https://www.linkedin.com/in/aakash-s-2209a1257)  

---


