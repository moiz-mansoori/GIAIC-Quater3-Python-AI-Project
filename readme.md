# GIAIC Quarter-3 Projects

## Growth Mindset Journey Tracker, Unit Converter, Password Strength Meter, Library manager & Secure Data Encryption System

This repository contains **Five projects** built with **Streamlit** as part of the **GIAIC Quarter-3 curriculum**. These projects focus on practical applications of Python in web development, data handling, and user interaction. Under the guidance of **Sir Zia Khan**, these projects aim to enhance problem-solving skills and proficiency in **Streamlit**, a powerful Python framework for building interactive web applications.

### 📌 Projects Overview:

1. **Growth Mindset Journey Tracker** - A web application to help users track and develop their growth mindset through daily reflections, progress visualization, and educational resources.

2. **Unit Converter** - A **Streamlit-based Unit Converter** that allows users to easily convert values between different measurement units. The app supports multiple categories such as **length, mass, area, speed, temperature, and more**.

3. **Password Strength Meter** - A secure and interactive web app that analyzes password strength, provides feedback, and generates strong passwords.

4. **Library Manager** - A command-line personal library manager that allows users to manage their book collection, track reading progress, and view library statistics.

5. **SecureVault – Secure Data Encryption System** -The application enables users to securely encrypt, store, and retrieve sensitive information using custom passkeys, all through an intuitive and user-friendly web interface.


---

# Growth Mindset Journey Tracker

A web application built with **Streamlit** to help users track and develop their growth mindset through daily reflections, progress visualization, and educational resources.

## 🔥 About the Project

This project is the **first project of Quarter 3, Section A**, under the guidance of **Sir Zia Khan**. The original project details can be found [here](https://github.com/panaversity/learn-modern-ai-python/blob/main/Growth_Mindset_Challenge.md).

The goal of this application is to encourage self-improvement by providing users with tools to reflect on their learning experiences, track progress, and access valuable educational content on developing a **growth mindset**.

## 🌟 Features  

### 🔐 User Authentication  
- Secure login and signup system  
- Password hashing for enhanced security  
- Session management for user data preservation  

### ✍️ Daily Reflections  
- Log daily challenges and key learnings  
- Track mindset rating over time  
- Set personal improvement goals  
- View reflection history  

### 📊 Progress Tracking  
- Visual representation of mindset growth  
- Analyze historical data trends  
- User-specific progress insights  

### 📚 Educational Resources  
- Learn about **growth mindset principles**  
- Access recommended books, articles, and videos  
- Explore learning tips and strategies

## 🚀 Deployment

The Web App with Streamlit Deployed URL is live and accessible at:
[**Web App with Streamlit**](https://giaic-quater3-python-ai-project-zd9ubtdksipnpwbkzrbtje.streamlit.app/)

## 📝 Usage Guide  

### 1️⃣ Sign Up / Login  
- Register with your **email and password**  
- Log in securely  
- Logout when finished  

### 2️⃣ Daily Reflection  
- Navigate to the **Daily Reflection** tab  
- Log your **challenges, learnings, and mindset rating**  
- Set action steps for improvement  

### 3️⃣ Track Progress  
- Visit the **Progress Tracker** tab  
- View mindset rating trends over time  
- Review previous reflections  

### 4️⃣ Access Learning Resources  
- Explore the **Learning Resources** tab  
- Watch educational videos and read recommended materials  

## 🛠️ Technical Details  
- Built using **Streamlit**  
- Secure authentication with **SHA-256 password hashing**  
- Utilizes **session state** for temporary data management  
- Responsive design for different screen sizes  

## ⚠️ Important Notes  
- This is a **development version** using session state for temporary storage  
- **Data will be lost** when the server restarts  

For production use, consider implementing:  
- Persistent database storage  
- Password reset functionality  
- Email verification system  
- Enhanced session management  
- Rate limiting to prevent unauthorized login attempts  

---

# Unit Converter

A **lightweight and user-friendly** unit conversion web app built with **Streamlit**.

## 🚀 Features
- **Multiple Unit Categories**: Convert units across various domains like **length, mass, area, speed, digital storage, pressure, etc.**
- **Temperature Conversion Handling**: Converts **Celsius, Fahrenheit, and Kelvin** using proper formulas.
- **Fuel Economy Conversions**: Supports **miles per gallon, liters per 100 km**, and more.
- **Live Conversion**: Instant results based on input values.
- **User-Friendly Interface**: Simple dropdowns for unit selection and real-time calculations.
- **Common Conversions Table**: Displays frequently used conversions for reference.

## 🚀 Deployment
- The Unit Converter app is live and accessible at:
[**Unit Converter App**](https://8ajkilr2dnouaw62ndqbvq.streamlit.app/)

## 📌 Supported Categories
- **Length** (meters, kilometers, miles, inches, etc.)
- **Mass** (grams, kilograms, pounds, tons, etc.)
- **Area** (square meters, acres, hectares, etc.)
- **Speed** (m/s, km/h, mph, knots, etc.)
- **Temperature** (Celsius, Fahrenheit, Kelvin)
- **Time** (seconds, minutes, hours, days, etc.)
- **Volume** (liters, gallons, cubic meters, etc.)
- **Pressure** (Pascal, bar, PSI, atm, etc.)
- **Digital Storage** (bytes, kilobytes, megabytes, terabytes, etc.)
- **Energy** (joules, calories, watt-hours, etc.)
- **Plane Angle** (degrees, radians, etc.)
- **Data Transfer Rate** (bps, kbps, Mbps, Gbps, etc.)

## 🛠️ How It Works
1. **Select a Category** from the sidebar dropdown.
2. **Choose "From" and "To" Units** from the dropdown lists.
3. **Enter the Value** in the input field.
4. The converted result appears **instantly**.
5. **See the conversion formula** used in calculations.
6. **Check Common Conversions** for quick reference.

## 🔢 Conversion Formulas
### Temperature
- **Celsius to Fahrenheit**: \( °F = (°C × 9/5) + 32 \)
- **Fahrenheit to Celsius**: \( °C = (°F - 32) × 5/9 \)
- **Celsius to Kelvin**: \( K = °C + 273.15 \)
- **Kelvin to Celsius**: \( °C = K - 273.15 \)
- **Fahrenheit to Kelvin**: \( K = (°F - 32) × 5/9 + 273.15 \)
- **Kelvin to Fahrenheit**: \( °F = (K - 273.15) × 9/5 + 32 \)

### Fuel Economy
- **Liters per 100 km to MPG (US)**: \( MPG = 235.215 / (L/100km) \)

Other categories follow **direct unit-to-unit conversion ratios**.

---

# Password Strength Meter

A **Streamlit-based** web app that evaluates password strength and provides feedback on improving security.

## 🚀 Features
- **Real-time Password Analysis**: Checks password strength as users type.
- **Feedback & Suggestions**: Provides recommendations for stronger passwords.
- **Password Generation**: Generates secure, random passwords.
- **Color-Coded Strength Indicator**: Shows weak, medium, or strong passwords.
- **Secure Handling**: Ensures password security without storing user input.

## 🚀 Deployment
- The Password Strength Meter app is live and accessible at:
[**Password Strength Meter App**](https://gba5sbnxegugrhevgrw4uc.streamlit.app/)

## 📝 Usage Guide
1. **Enter a password**: The app will analyze its strength.
2. **View feedback**: Suggestions for improving password security.
3. **Generate a strong password**: Use the password generator for enhanced security.

✅ **A simple yet powerful tool for ensuring strong password security!**

---

# Library Manager

A **command-line personal library manager** that allows users to manage their book collection, track reading progress, and view library statistics. 

## 📌 Features

📚 **Add & Remove Books**: Easily add books with details like title, author, year, genre, and read status.

🔍 **Search Books**: Find books by title or author.

📖 **View Library**: Display all stored books with reading status.

📊 **Track Reading Progress**: See the percentage of books read.

💾 **Save & Load Data**: Books are saved in `library.txt` for persistence.

---

# 🔐 SecureVault – Secure Data Encryption System

**SecureVault** is a secure data encryption system allows users to **encrypt, store, and retrieve sensitive information** using custom passkeys, all through a user-friendly web interface built with **Streamlit**.

## ✅ Features

- 🔐 **Encrypt & Store** any sensitive data with a custom passkey
- 🔓 **Retrieve** data securely using the correct encrypted string and passkey
- ⛔ **Lockout Mechanism** after 3 failed decryption attempts
- 🔑 **Admin Panel** for vault statistics, unlocking, and reset
- 🧠 Easy-to-use interface with real-time feedback
- 🗝️ Automatic key generation using `Fernet` encryption


---


## 🎯 Requirements
To run the applications, ensure you have **Python 3.x** installed and the following dependencies:

```bash
pip install streamlit
```

## ▶️ Running the App
Run the following command in your terminal or command prompt:

```bash
python -m streamlit run (filename).py
```


## 👥 Author  

### GIAIC Student:
 
**Moiz Mansoori**  
**5691**  

## 📞 Support  

For any questions or issues, feel free to reach out:  
- 📧 Email: [mansoorimoiz03@gmail.com](mailto:mansoorimoiz03@gmail.com)  
- 🛠 Open an issue in the repository
