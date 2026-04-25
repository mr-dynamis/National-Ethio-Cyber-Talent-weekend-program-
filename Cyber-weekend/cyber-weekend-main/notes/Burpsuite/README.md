# Burp Suite 
Burp Suite is one of the most widely used tools in web application security testing. Think of it as a man-in-the-middle (MITM) proxy + toolkit that lets you see, modify, and analyze everything happening between your browser and a web server.


---

## 1. Core Idea: How Burp Suite Works

At its heart, Burp works as an intercepting proxy:

👉 Your flow normally:

Browser → Website Server

👉 With Burp:

Browser → Burp Suite → Website Server

This allows Burp to:

Capture requests before they reach the server

Let you modify them

Capture responses coming back



---

## 2. Burp Suite Structure (Main Components)

Burp is modular. Each tool has a specific role:


---

### 1. Proxy (The Heart of Burp)

This is where everything starts.

What it does:

Intercepts HTTP/HTTPS traffic

Lets you pause, edit, forward, or drop requests


Key features:

Intercept ON/OFF

Request editing

Response viewing

History tab (all traffic recorded)


👉 Example: You log into a site → Burp captures the login request → you can modify:

username=admin&password=1234


---

### 2. Target (Site Mapping)

This builds a map of the website.

What it shows:

All discovered URLs

Directories and endpoints

Parameters


👉 Think of it as:

> “Google Maps for the web app you’re testing”




---

### 3. Repeater (Manual Testing Tool)

Used for sending the same request repeatedly with changes.

Why it’s powerful:

Test payloads manually

Modify parameters

Analyze responses instantly


👉 Example: Change:

id=1 → id=2 → id=999

To test for IDOR vulnerabilities


---

### 4. Intruder (Automation / Brute Force)

This is for automated attacks.

Uses:

Brute-force passwords

Fuzz parameters

Discover hidden values


Attack types:

Sniper (one position)

Battering ram (same payload everywhere)

Pitchfork (multiple payload sets)

Cluster bomb (all combinations)


👉 Example: Testing login:

username: admin
password: [wordlist]


---

### 5. Scanner (Pro Version)

Automatically finds vulnerabilities like:

SQL Injection

XSS

CSRF


⚠️ Not available in Community Edition (manual testing instead)


---

### 6. Decoder

Encodes/decodes data:

Base64

URL encoding

HTML encoding


👉 Useful for:

YWRtaW4= → admin


---

### 7. Comparer

Compares two responses:

Useful for spotting subtle differences



---

### 8. Sequencer

Analyzes randomness of tokens:

Session IDs

CSRF tokens



---

### 9. Extender

Allows plugins/extensions:

Add custom tools

Integrate scripts



---

## 3. How Burp Works Step-by-Step (Real Flow)

Step 1: Configure Browser

Set proxy to:


127.0.0.1:8080


---

Step 2: Turn Intercept ON

Open a website

Burp captures request



---

Step 3: Analyze Request

Example:

POST /login HTTP/1.1
Host: example.com

username=admin&password=1234


---

Step 4: Modify Request

Try:

username=admin' OR '1'='1


---

Step 5: Forward to Server

See response

Analyze behavior



---

Step 6: Send to Tools

Send to Repeater → manual testing

Send to Intruder → brute force



---

## 4. Key Concepts You MUST Understand


---

🔸 HTTP Requests & Responses

Request:

GET /index.php?id=1 HTTP/1.1
Host: site.com

Response:

HTTP/1.1 200 OK
<html>...</html>

👉 Burp lets you control both.


---

🔸 Headers vs Body

Headers = metadata

Body = actual data


Example:

Content-Type: application/x-www-form-urlencoded


---

🔸 Cookies & Sessions

Burp helps you:

View cookies

Modify session tokens

Test authentication flaws



---

🔸 HTTPS Interception

Burp installs a certificate so it can:

Decrypt HTTPS traffic

Inspect secure communication



---

## 5. What You Can Do With Burp

Find SQL Injection

Test XSS (Cross-Site Scripting)

Check authentication flaws

Perform brute-force attacks

Analyze APIs



---

## 6. Important Real-World Tips

### 1. Always use Repeater first

Don’t jump into Intruder blindly.


---

### 2. Learn to read requests

Most beginners fail here.


---

### 3. Understand parameters

Every vulnerability comes from: 👉 input → processing → output


---

### 4. Use Proxy History

It’s gold. You’ll find hidden endpoints.


---

### 5. Practice on labs

Best place:

OWASP Juice Shop

PortSwigger Web Security Academy


---

## 7.  Example Attack Flow (Simple)

1. Intercept login request


2. Send to Repeater


3. Test:

         admin'--


4. Observe response difference


5. Confirm SQL Injection




