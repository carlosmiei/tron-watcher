import time
import requests
import smtplib
from email.message import EmailMessage
from email_template import get_html_body

### EMAIL CONFIG ###
SENDER_EMAIL = 'YOUR EMAIL'
SENDER_PASSWORD = 'YOUR GMAIL APP PASSWORD' # gmail app password
RECIPIENTS = ['RECIPIENT EMAIL']

### CONTRACT CONFIG ###
CONTRACT = "TR7NHqjeKQxGTCi8q8ZY4pL8otSzgjLj6t" # USDT CONTRACT ADDRESS

### ACCOUNT TO WATCH ###
ACCOUNT = 'YOUR TRON ACCOUNT' # ACCOUNT TO WATCH

### POLLING CONFIG ###
POLL_INTERVAL = 5 # 5 minutes

TRANSACTIONS_URL = f'https://api.trongrid.io/v1/accounts/{ACCOUNT}/transactions/trc20?limit=20&contract_address={CONTRACT}'
ACCOUNT_URL = f'https://apilist.tronscan.org/api/account?address={ACCOUNT}&includeToken=true'

seen_transactions = set()

def send_email(subject, body):
    msg = EmailMessage()
    msg.set_content(body, subtype='html')
    msg['Subject'] = subject
    msg['From'] = SENDER_EMAIL
    msg['To'] = ', '.join(RECIPIENTS)
    smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    smtp_server.login(SENDER_EMAIL, SENDER_PASSWORD)
    smtp_server.sendmail(SENDER_EMAIL, RECIPIENTS, msg.as_string())
    smtp_server.quit()

def get_usdt_transactions():
    response = requests.get(TRANSACTIONS_URL)
    return response.json()


def get_usdt_balance():
    response = requests.get(ACCOUNT_URL)
    data = response.json()
    for token in data['trc20token_balances']:
        if token['tokenName'] == 'Tether USD':
            usdt_balance = round(float(token['balance'])*pow(10,-token['tokenDecimal']),6)
            return usdt_balance

def create_send_email(tx):
    timestamp = tx['block_timestamp']
    id = tx['transaction_id']
    datetime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(timestamp/1000))
    is_deposit = tx['to'] == ACCOUNT
    amount = round(float(tx['value'])*pow(10,-tx['token_info']['decimals']),6)
    action = 'Deposit' if is_deposit else 'Withdrawal'
    subject = f'[{action}] confirmation of USDT on [{ACCOUNT}]'
    link = f'https://tronscan.org/#/transaction/{id}'
    other_key = 'From' if is_deposit else 'To'
    other_account = tx['from'] if is_deposit else tx['to']
    body = get_html_body(ACCOUNT, id, action, amount, datetime, link, other_key, other_account)
    send_email(subject, body)

def handle_usdt_transactions():
    while True:
        transactions = get_usdt_transactions()['data']
        current_time = time.time() * 1000
        for tx in transactions:
            timestamp = tx['block_timestamp']
            id = tx['transaction_id']
            if True or id not in seen_transactions:
                seen_transactions.add(id)
                diff = current_time - timestamp
                if True or diff < POLL_INTERVAL * 60 * 1000:
                    print('this is a new transaction, will send an email', timestamp, 'id', id)
                    create_send_email(tx)
        print('Will sleep for:', POLL_INTERVAL, 'minutes')
        time.sleep(POLL_INTERVAL * 60)

def main():
    handle_usdt_transactions()

main()