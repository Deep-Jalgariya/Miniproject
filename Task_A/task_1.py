import gradio as gr
import pandas as pd
import random
import matplotlib.pyplot as plt
from datetime import datetime
from io import BytesIO

# storing account balance and history
accounts = {}
transactions = {}

def create_account(name):
    # create account
    acc_number = random.randint(100000, 999999)
    accounts[acc_number] = {"name": name, "balance": 0}
    transactions[acc_number] = []  # Initialize transaction history
    return f"Account created! Name: {name}, Account Number: {acc_number}"

def deposit(acc_number, amount):
    # deposite
    acc_number = int(acc_number)
    if acc_number in accounts:
        if amount <= 0:
            return "Deposit amount must be greater than zero!"
        accounts[acc_number]["balance"] += amount
        transactions[acc_number].append((datetime.now(), "Deposit", amount))
        return f"Deposit successful! New Balance: {accounts[acc_number]['balance']}"
    return "Account not found!"

def withdraw(acc_number, amount):
    # withdraw
    acc_number = int(acc_number)
    if acc_number in accounts:
        if amount <= 0:
            return "Withdrawal amount must be greater than zero!"
        if accounts[acc_number]["balance"] >= amount:
            accounts[acc_number]["balance"] -= amount
            transactions[acc_number].append((datetime.now(), "Withdrawal", -amount))
            return f"Withdrawal successful! New Balance: {accounts[acc_number]['balance']}"
        return "Insufficient balance!"
    return "Account not found!"

def check_balance(acc_number):
    # balance check
    acc_number = int(acc_number)
    if acc_number in accounts:
        return f"Account Balance: {accounts[acc_number]['balance']}"
    return "Account not found!"

def delete_account(acc_number):
    # for delete account
    acc_number = int(acc_number)
    if acc_number in accounts:
        del accounts[acc_number]
        del transactions[acc_number]
        return f"Account {acc_number} deleted successfully!"
    return "Account not found!"

def get_transaction_history(acc_number):
    # transaction history
    acc_number = int(acc_number)
    if acc_number in transactions:
        history = transactions[acc_number]
        if not history:
            return "📜 No transactions found for this account."
        return pd.DataFrame(history, columns=["Date", "Type", "Amount"])
    return "Account not found!"

def calculate_interest():
    # calculate intrest
    for acc_number in accounts:
        interest = accounts[acc_number]["balance"] * 0.05
        accounts[acc_number]["balance"] += interest
        transactions[acc_number].append((datetime.now(), "Interest", interest))
    return "5% interest applied to all accounts!"

def get_accounts_table():
    # account table
    if not accounts:
        return pd.DataFrame(columns=["Account Number", "Name", "Balance"])
    data = [[acc_number, details["name"], details["balance"]] for acc_number, details in accounts.items()]
    return pd.DataFrame(data, columns=["Account Number", "Name", "Balance"])


with gr.Blocks() as bank_ui:
    gr.Markdown("# 🏦 Advanced Bank Account Manager")
    
    with gr.Tab("Create Account"):
        name_input = gr.Textbox(label="Enter Your Name")
        create_btn = gr.Button("Create Account")
        acc_output = gr.Textbox(label="Account Info", interactive=False)
        create_btn.click(create_account, inputs=[name_input], outputs=[acc_output])

    with gr.Tab("Deposit Money"):
        acc_input_d = gr.Textbox(label="Enter Account Number")
        amount_input_d = gr.Number(label="Enter Amount")
        deposit_btn = gr.Button("Deposit")
        deposit_output = gr.Textbox(label="Transaction Status", interactive=False)
        deposit_btn.click(deposit, inputs=[acc_input_d, amount_input_d], outputs=[deposit_output])

    with gr.Tab("Withdraw Money"):
        acc_input_w = gr.Textbox(label="Enter Account Number")
        amount_input_w = gr.Number(label="Enter Amount")
        withdraw_btn = gr.Button("Withdraw")
        withdraw_output = gr.Textbox(label="Transaction Status", interactive=False)
        withdraw_btn.click(withdraw, inputs=[acc_input_w, amount_input_w], outputs=[withdraw_output])

    with gr.Tab("Check Balance"):
        acc_input_b = gr.Textbox(label="Enter Account Number")
        balance_btn = gr.Button("Check Balance")
        balance_output = gr.Textbox(label="Balance Info", interactive=False)
        balance_btn.click(check_balance, inputs=[acc_input_b], outputs=[balance_output])

    with gr.Tab("Delete Account"):
        acc_input_del = gr.Textbox(label="Enter Account Number")
        delete_btn = gr.Button("Delete Account")
        delete_output = gr.Textbox(label="Delete Status", interactive=False)
        delete_btn.click(delete_account, inputs=[acc_input_del], outputs=[delete_output])

    with gr.Tab("Transaction History"):
        acc_input_th = gr.Textbox(label="Enter Account Number")
        history_btn = gr.Button("View Transaction History")
        history_output = gr.Dataframe(label="Transaction History")
        
        history_btn.click(get_transaction_history, inputs=[acc_input_th], outputs=[history_output])
        

    with gr.Tab("View All Accounts"):
        refresh_btn = gr.Button("Refresh Table")
        accounts_table = gr.Dataframe(label="Accounts")
        refresh_btn.click(get_accounts_table, inputs=[], outputs=[accounts_table])

    with gr.Tab("Calculate Interest"):
        interest_btn = gr.Button("Apply 5% Interest to All Accounts")
        interest_output = gr.Textbox(label="Interest Status", interactive=False)
        interest_btn.click(calculate_interest, inputs=[], outputs=[interest_output])

bank_ui.launch()
