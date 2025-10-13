<h1 align="center">🧠 Simple Self-Learning Chatbot</h1>
<p align="center">
  <em>A minimal Python chatbot that remembers your answers and improves over time.</em>
</p>

---

## 📘 Overview
This project is a lightweight, text-based **self-learning chatbot** written in Python.  
It doesn’t use any AI API or external libraries — instead, it learns directly from your input.  
Whenever it encounters a question it doesn’t know, it asks you for the correct answer and stores it locally, building its own knowledge base.

---

## 🚀 Features
- 🧩 **Learns automatically** from user input  
- 💾 **Stores data** in `text.json` for persistent memory  
- 🤔 **Understands similar questions** (e.g., `who r u` ≈ `who are you`)  
- 🔤 **Case-insensitive** text matching  
- ⚡ **No internet required** — works completely offline  

---

## 🧰 Requirements
- Python **3.8+**
- No additional libraries needed  
  *(only built-in `json` and `difflib`)*

---

## ▶️ How to Run
1. **Clone or download** this repository:
   ```bash
   git clone https://github.com/your-username/self-learning-chatbot.git
   cd self-learning-chatbot
