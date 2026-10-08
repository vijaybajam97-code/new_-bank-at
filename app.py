import streamlit as st

# -----------------------------
# SBI Banking System
# -----------------------------

st.set_page_config(
    page_title="SBI Banking System",
    page_icon="🏦"
)

# Create the account balance when the app starts
if "balance" not in st.session_state:
    st.session_state.balance = 50000.0

st.title("🏦 SBI Banking System")
st.write("Simple banking application built with Python and Streamlit.")

st.divider()

# Show current balance
st.subheader(f"Current Balance: ₹{st.session_state.balance:.2f}")

# Enter amount
amount = st.number_input(
    "Enter amount:",
    min_value=0.0,
    step=100.0,
    format="%.2f"
)

st.divider()

# Credit / Deposit
if st.button("💰 Credit / Deposit", use_container_width=True):
    if amount <= 0:
        st.error("Please enter a valid amount.")
    else:
        st.session_state.balance += amount
        st.success(f"₹{amount:.2f} deposited successfully!")
        st.info(f"Available balance: ₹{st.session_state.balance:.2f}")

# Debit / Withdraw
if st.button("💸 Debit / Withdraw", use_container_width=True):
    if amount <= 0:
        st.error("Please enter a valid amount.")
    elif amount > st.session_state.balance:
        st.error("Insufficient balance.")
    else:
        st.session_state.balance -= amount
        st.success(f"₹{amount:.2f} debited successfully!")
        st.info(f"Current balance: ₹{st.session_state.balance:.2f}")

# Check balance
if st.button("💳 Check Balance", use_container_width=True):
    st.info(f"Your current balance is ₹{st.session_state.balance:.2f}")

st.divider()

st.caption("Demo project only. It does not use a real bank account or database.")
