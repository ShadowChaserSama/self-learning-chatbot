<h1 align="center">🧠 Simple Self-Learning Chatbot</h1>
<p align="center">
  <em>A minimal Python chatbot that remembers your answers and improves over time.</em>
</p>

---

## 📌 Update 1.1
- add new sound engine and sound system.
- improve answer quality.
- fix some bugs.

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

---

## 💡 Example Usage
```bash
🗨️ Question: who are you?
❓ I don't know the answer to this question. Please teach me.
Enter the answer: I'm a simple chatbot.
✅ Learned successfully. Thank you!

🗨️ Question: who r u
🤔 Did you mean: 'who are you?'
💬 I'm a simple chatbot.
```

---

## 🧠 How It Works

When you ask a question, the bot checks its knowledge base (text.json).
If it knows the answer → it replies.
If not → it asks you to teach it, saves your response, and remembers it.
It can also recognize similar questions using Python’s SequenceMatcher.

---

## 📂 Project Structure
self-learning-chatbot/
│
├── main.py        # Main Python script
├── text.json      # Knowledge database (auto-created)
└── README.md      # Documentation

---

## 📜 License

This project is open source and available under the MIT License.
You can freely modify, share, and improve it.

---

## ✨ Author

**Əli Zülbalayev**
💻 Passionate about Python and AI automation.
📧 Contributions and improvements are welcome — feel free to fork and build your version!

<p align="center"> <img src="https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python&logoColor=white" alt="Python"> <img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge"> <img src="https://img.shields.io/badge/Status-Active-success?style=for-the-badge"> </p> <p align="center"><em>Made with ❤️ in Python</em></p> ```
