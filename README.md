![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)
![LangChain](https://img.shields.io/badge/LangChain-1C3C3C?style=for-the-badge&logo=langchain&logoColor=white)
![HuggingFace](https://img.shields.io/badge/HuggingFace-F9AB00?style=for-the-badge&logo=huggingface&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

Welcome to the **Simple Mistral Chatbot Playground**! This repository features a minimalist, easy-to-understand conversational application built with **Streamlit** and powered by the cutting-edge **Mistral-7B-v0.1** model via **LangChain** and **Hugging Face Endpoints**.

This project is perfect for beginners looking to understand how to connect large language models to a web interface without the overhead of complex memory modules or agent routing.

---

## ✨ Features

- **Sleek Web Interface:** A lightweight and responsive chat UI built with Streamlit.
- **Mistral 7B Power:** Uses the open-weight `mistralai/Mistral-7B-v0.1` model for fast and intelligent inferences.
- **Customizable Parameters:** Easily tweak `temperature` and `max_new_tokens` directly in the code to change the AI's creativity and response length.
- **Notebook Prototyping:** A ready-to-use Jupyter Notebook (`simple-chatbot.ipynb`) for experimenting with the LLM API before deploying to the app.

---

## 📂 Project Structure

```text
📦 repository
 ┣ 📜 app.py                 # The Streamlit web application script
 ┣ 📜 simple-chatbot.ipynb   # Jupyter notebook for testing & API prototyping
 ┗ 📜 README.md              # You are here!


---

## 🚀 Step-by-Step Quickstart Guide

### 1. Prerequisites

Before diving in, make sure you have:

* **Python 3.8+** installed on your machine.
* A **Hugging Face Account** and a generated [Access Token](https://huggingface.co/settings/tokens).

### 2. Clone the Repository

```bash
git clone [https://github.com/your-username/your-repo-name.git](https://github.com/your-username/your-repo-name.git)
cd your-repo-name

```

### 3. Set Up a Virtual Environment (Highly Recommended)

Keep your dependencies clean and isolated to avoid package conflicts:

```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\\Scripts\\activate

```

### 4. Install Dependencies

Install the required Python packages using pip:

```bash
pip install streamlit langchain langchain-huggingface jupyter

```

### 5. Set Your Hugging Face API Token

The AI model needs your Hugging Face API token to generate responses.

Open `app.py` and replace the placeholder with your actual token:

```python
import os
os.environ['HUGGINGFACEHUB_API_TOKEN'] = 'hf_your_actual_token_here' 

```

*(⚠️ **Security Warning:** Never commit your actual API token to a public GitHub repository. For production apps, it is best practice to use Streamlit Secrets or a `.env` file instead of hardcoding it).*

### 6. Run the Application! 🎉

Fire up the Streamlit web interface by executing:

```bash
streamlit run app.py

```

Your browser will automatically open a new tab (usually at `http://localhost:8501`) where you can start asking the Mistral chatbot anything!

---

## 🧪 Testing in the Jupyter Notebook

If you want to test the raw API calls without running the Streamlit UI, open the provided notebook:

```bash
jupyter notebook simple-chatbot.ipynb

```

This environment is perfect for debugging, checking dependency installations, or experimenting with different LLMs available on the Hugging Face Hub (just change the `repo_id`).

## 🤝 Contributing

Got ideas to improve this project? Feel free to fork the repository, make your changes, and submit a Pull Request!
You can download the generated file using the link above and drop it directly into your GitHub repository!

```
