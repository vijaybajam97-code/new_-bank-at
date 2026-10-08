# 🏦 SBI Banking System

A simple banking system web application built using **Python and Streamlit**.

This project is designed as a beginner-friendly deployment project.

## Features

- 💰 Credit / Deposit money
- 💸 Debit / Withdraw money
- 💳 Check current balance
- Checks for invalid amounts
- Checks for insufficient balance
- Simple web interface
- No HTML required

## Project Structure

```text
banking-system/
│
├── app.py
├── requirements.txt
└── README.md
```

## Starting Balance

The application starts with:

```text
₹500
```

## Run on Your Computer

### 1. Install the requirements

```bash
pip install -r requirements.txt
```

### 2. Start the application

```bash
streamlit run app.py
```

### 3. Open the local URL

Streamlit will show a URL similar to:

```text
http://localhost:8501
```

Open it in your browser.

## How the Application Works

```text
User enters amount
        ↓
      Button
        ↓
   Python code
        ↓
 Check the amount
        ↓
 ┌──────┴──────┐
 ↓             ↓
Credit        Debit
 ↓             ↓
+ money       - money
        ↓
 Current Balance
```

## Important

This is a learning/demo project.

It does **not** connect to a real SBI account, bank server, payment system, or database.

The balance is stored only during the Streamlit session.

## Deployment

This project can be uploaded to GitHub and deployed using a Streamlit-compatible hosting service.

Main file:

```text
app.py
```

Requirements file:

```text
requirements.txt
```
