# ProdigyInfoTech-CyberSecurity-Internship-Task-03
 Task 03: Password Complexity Checker
# Prodigy InfoTech – Cyber Security Internship  
## Task 03: Password Complexity Checker

This project is developed as part of the **Prodigy InfoTech Cyber Security Internship**.  
The objective of this task is to build a **professional password complexity checking tool**
that evaluates the strength of a password based on multiple security criteria and provides
clear feedback to the user.

---

## 📌 Task Objective
To assess the strength of a password using standard security rules such as:
- Password length
- Uppercase letters
- Lowercase letters
- Numbers
- Special characters  

The tool categorizes passwords as **Weak, Medium, or Strong** and provides actionable
suggestions for improvement.

---

## 🧠 Security Criteria Used
The password is evaluated based on the following conditions:

- Minimum length of **8 characters**
- At least **one uppercase letter (A–Z)**
- At least **one lowercase letter (a–z)**
- At least **one numeric digit (0–9)**
- At least **one special character (!@#$%^&*)**

Each condition contributes to the overall password strength score.

---

## 🛠️ Technologies Used
- Python 3
- Regular Expressions (re module)

---

## ⚙️ Features
- Score-based password strength evaluation  
- Strength levels: **WEAK / MEDIUM / STRONG**  
- Clear security feedback and improvement suggestions  
- Modular and reusable code structure  
- Command-line interface  

---

## ▶️ How to Run the Program

1. Ensure Python is installed on your system  
2. Open terminal / PowerShell in the project directory  
3. Run the program using:

```bash
python password_checker.py
Enter a password when prompted

🧪 Example
Input:
Rohit@123097gfj
Output:
Password Strength: STRONG

✔ Password meets all security standards
Weak Password Example:
rohit
Output:
Password Strength: WEAK

Security Suggestions:
- Use at least 8 characters
- Add at least one uppercase letter
- Add at least one number
- Add at least one special character
