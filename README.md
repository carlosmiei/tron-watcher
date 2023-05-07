# USDT TRON Watcher (through gmail)

This simple script allows you to get an email notification every time your account gets a deposit or makes an withdrawal. I decided to create it because the notify functionality from Tron Explorer does not work properly. In order to get the email notification you need a gmail account and create a `gmail app password`, the account's password does not work anymore. See how to create one [here] (https://www.getmailbird.com/gmail-app-password/).

### How to use
- Opem `main.py` and fill in `SENDER_EMAIL` `SENDER_PASSWORD`, `RECIPIENTS` and `ACCOUNT`
- Install dependencies
- run `python main.py`

### Sample email
- After configuring everything correctly, you will receive updates like this one:
![sampleBotEmail](https://user-images.githubusercontent.com/43336371/236694054-769378a3-c70e-4e3f-977b-d336cf2432fb.png)