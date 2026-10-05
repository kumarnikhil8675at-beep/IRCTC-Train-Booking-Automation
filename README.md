# 🚆 IRCTC Train Booking Automation — Selenium with Python

<p align="center">
  <img src="./images/logo.png" alt="IRCTC Logo" width="180">
</p>

<p align="center">
  <b>Python + Selenium based automation project for learning browser automation</b>
</p>

---

## 📌 About This Project

This project is created **for learning purposes** to understand how browser automation works using **Python and Selenium**.

The program automates several steps of the IRCTC train-search and booking flow, such as:

- 🔐 Logging into an IRCTC account
- 🚆 Searching for a specific train
- 📍 Selecting the From and To stations
- 📅 Selecting the journey date
- 🛏️ Selecting the Sleeper class
- 👥 Selecting passengers from the IRCTC Master List
- ⚡ Reducing repetitive manual steps

The program stops before the final payment step. The user must manually select the payment method and complete the transaction.

> ⚠️ **Educational Purpose:** This project is intended to practice Selenium, XPath, CSS selectors, explicit waits, browser automation, and web-element handling. Always use automation only in ways permitted by the website's current terms, policies, and applicable rules.

---

## 🎯 Purpose

The main purpose of this project is to learn how Selenium can be used to automate repetitive actions in a real website.

It helped me practice:

```text
Python
   ↓
Selenium
   ↓
WebDriver
   ↓
HTML Elements
   ↓
XPath / CSS Selectors
   ↓
Web Automation
```

The project is **not intended to bypass CAPTCHA, security systems, payment verification, or other protections.**

---

## 🛠️ Technologies Used

| Technology | Purpose |
|------------|---------|
| 🐍 Python | Main programming language |
| 🤖 Selenium | Browser automation |
| 🌐 Google Chrome | Browser |
| 🔎 XPath | Finding web elements |
| 🎯 CSS Selectors | Finding web elements |
| ⏳ WebDriverWait | Waiting for elements |
| ⌨️ Keys | Sending keyboard actions |

---

## 📂 Project Structure

```text
IRCTC-Automation/
│
├── main.py
└── README.md
```

---

# ⚙️ How It Works

## 1. Start Chrome with Remote Debugging

Before running the Python program, Chrome needs to be started with remote debugging enabled.

Open **Win + R** and run:

```text
"C:\Program Files\Google\Chrome\Application\chrome.exe" --remote-debugging-port=9222
```

This allows Selenium to connect to the already-open Chrome session.

---

## 2. Connect Selenium to Chrome

The program uses:

```python
chrome_option = webdriver.ChromeOptions()

chrome_option.add_experimental_option(
    "debuggerAddress",
    "127.0.0.1:9222"
)

driver = webdriver.Chrome(options=chrome_option)
```

Instead of creating a completely new browser session, Selenium connects to the Chrome instance running on port `9222`.

---

# 🔑 Login

The program opens the IRCTC website and enters the username and password.

```python
username.send_keys(Username)
password.send_keys(Password)

password.send_keys(Keys.ENTER)
```

For security, real login credentials should **never be uploaded to GitHub**.

Use placeholders such as:

```python
Username = "your_username"
Password = "your_password"
```

or preferably environment variables.

---

# 🚉 Train Search

The important details are stored at the beginning of the program:

```python
Train_name = 'S KRANTI SUP EX (12393)'
From = 'PATNA JN. - PNBE'
To = 'NEW DELHI - NDLS (NEW DELHI)'
Date = '03/12/2026'

Member = 6
```

This makes it easy to change the journey details without changing the main automation logic.

---

# 📍 Selecting Stations

The program finds the From station:

```python
from_location = WebDriverWait(driver, 1).until(
    EC.presence_of_element_located(
        (By.XPATH, "...")
    )
)

from_location.send_keys(From)
```

Then it enters the destination:

```python
to_location.send_keys(To)
```

`send_keys()` is used to type the station name into the input field.

---

# 📅 Selecting Journey Date

The date field is selected and its existing value is cleared:

```python
date_journey.click()

date_journey.send_keys(Keys.CONTROL, 'a')
date_journey.send_keys(Keys.BACKSPACE)

date_journey.send_keys(Date)
date_journey.send_keys(Keys.ENTER)
```

---

# 🚆 Finding the Required Train

The program gets the list of available trains:

```python
list_of_train = driver.find_elements(
    By.CSS_SELECTOR,
    "div.form-group.no-pad.col-xs-12.bull-back.border-all"
)
```

Then it checks every train:

```python
for a in list_of_train:
    name = a.find_element(By.TAG_NAME, value='strong')

    if Train_name == name.text:
        print("Your train no is found : ", name.text)
```

So instead of selecting a train manually, the program searches the available train list for the name stored in:

```python
Train_name
```

---

# 🛏️ Sleeper Class

The current version of this project is designed for the **Sleeper class flow**.

After finding the required train, the program selects the sleeper option and continues to the booking step.

```python
sleeper_class.click()
```

Then it selects the available booking option:

```python
sleeper_class_show.click()
```

---

# 👥 Passenger Selection

The program uses passengers already saved in the **IRCTC Master List**.

The number of passengers is controlled by:

```python
Member = 6
```

The loop:

```python
for count_no in range(Member):
```

repeats the passenger-selection process.

If more passengers are required, the value can be changed:

```python
Member = 4
```

or:

```python
Member = 6
```

---

# 💳 Payment

The program **does not complete the payment automatically**.

After passenger selection, it displays:

```text
Everything is done.
Now you can select the payment method and complete your transaction to get your ticket.
```

The final payment and transaction are completed manually by the user.

---

# 🧠 Selenium Concepts Learned

This project helped me understand several important Selenium concepts.

### Finding one element

```python
driver.find_element()
```

### Finding multiple elements

```python
driver.find_elements()
```

### XPath

```python
(By.XPATH, "...")
```

### CSS Selector

```python
(By.CSS_SELECTOR, "...")
```

### Waiting for an element

```python
WebDriverWait(driver, 1).until(
    EC.presence_of_element_located(...)
)
```

### Typing into an input

```python
element.send_keys("text")
```

### Keyboard actions

```python
element.send_keys(Keys.ENTER)
```

### Clicking an element

```python
element.click()
```

### Searching through multiple elements

```python
for element in list_of_train:
    ...
```

---

# 🔐 Security Note

**Do not upload your actual IRCTC username or password to GitHub.**

For example, don't commit:

```python
Username = "actual_username"
Password = "actual_password"
```

Use:

```python
Username = "your_username"
Password = "your_password"
```

For a more advanced version, credentials can be stored using environment variables.

---

# ⚠️ Important Notice

This repository is an **educational Selenium automation project**.

It is created to learn:

- Browser automation
- Selenium WebDriver
- XPath
- CSS selectors
- Explicit waits
- Loops
- Web-element interaction
- Automation of repetitive browser tasks

It is **not designed to bypass CAPTCHA, security mechanisms, payment verification, or website protections**.

IRCTC's website has its own terms and conditions regarding the use of automated devices/software and website access. Users are responsible for checking and following the **latest applicable IRCTC terms and policies** before using automation.

---

# 🚀 Future Improvements

Some possible improvements for learning purposes:

- [ ] Add better error handling
- [ ] Replace long XPath expressions with shorter selectors
- [ ] Use environment variables for credentials
- [ ] Add logging
- [ ] Add configurable train/class selection
- [ ] Improve explicit waits
- [ ] Handle unavailable trains
- [ ] Add screenshots when an error occurs
- [ ] Create a simple configuration file
- [ ] Make the code more modular using functions/classes

---

# 📚 Learning Outcome

Through this project, I learned how a Python program can interact with a real web page.

The main learning flow was:

```text
Python
  ↓
Selenium WebDriver
  ↓
Open Browser
  ↓
Find HTML Elements
  ↓
XPath / CSS Selectors
  ↓
Click / Type / Select
  ↓
Automate Repetitive Tasks
```

This project was mainly created to get practical experience with **Selenium and browser automation** instead of only learning the concepts theoretically.

---

## ⭐ Disclaimer

This project is provided for **educational and learning purposes only**.

The author does not encourage misuse of automation or violation of any website's terms, policies, security mechanisms, or applicable laws.

Always use your own account and legitimate booking information, and check the current terms of the service before using automation.

---

<p align="center">
  🚆 <b>Built for Learning • Python • Selenium • Web Automation</b> 🐍
</p>
