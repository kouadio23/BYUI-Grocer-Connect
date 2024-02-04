# BYUI Grocer Connect

## 📖 Description

BYUI Grocer Connect is a web application designed to streamline the grocery shopping process for students at Brigham Young University-Idaho. It connects students needing groceries with those already planning to shop, facilitating a community-driven approach to grocery shopping.

## 🌟 Features

- **User Accounts:** Secure sign-up and login functionality.
- **Grocery List Submission:** Easy submission of grocery lists.
- **Shopper-Buyer Matching:** Automated matching for convenience.
- **In-App Chat:** Direct communication between users.
- **Payment Integration:** Simplified transactions.
- **Order Tracking:** Real-time updates on grocery orders.
- **Ratings & Reviews:** Trust-building through user feedback.

## 💻 Technologies Used

- **Backend:** Django
- **Frontend:** React
- **Database:** PostgreSQL
- **Data Format:** JSON

## 🚀 Getting Started

### Prerequisites

Ensure you have the following installed:
- Python 3.8+
- pip
- Node.js and npm
- PostgreSQL

### Setup

1. **Clone the Repository**

    ```bash
    git clone https://github.com/yourrepository/byui-grocer-connect.git
    cd byui-grocer-connect
    ```

2. **Backend Setup**

    Navigate to the backend directory and set up the Python environment:

    ```bash
    cd backend
    python -m venv venv
    venv\Scripts\activate  # On Windows
    source venv/bin/activate  # On Unix or MacOS
    pip install -r requirements.txt
    python manage.py migrate
    python manage.py runserver
    ```

3. **Frontend Setup**

    Set up the React environment:

    ```bash
    cd ../frontend
    npm install
    npm start
    ```

### Environment Variables

Create a `.env` file in the backend directory with necessary configurations for database connections and more.

## 📘 How to Use

Access the web application by navigating to `http://localhost:8000` in your browser, sign up for an account, and follow the on-screen prompts.

## 🤝 Contributing

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**. Check out our [Contribution Guidelines](CONTRIBUTING.md) for more information.

## ⚖️ License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## 💖 Acknowledgments

- BYU-I community for the inspiration.
- Contributors who dedicate time and effort to this project..

