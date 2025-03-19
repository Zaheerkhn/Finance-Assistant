# Finance Assistant

## Overview

The **Finance Assistant** is a web-based application built using **Streamlit** and powered by **Phi Agents** with **Groq LLM**. It provides users with financial data, stock market insights, and web-based information retrieval through AI-driven agents.

## Features

-  **Web Search**: Retrieve information from the web using DuckDuckGo.
-  Financial Data: Get stock prices, company details, and analyst recommendations.
-  **AI-Powered Responses**: Uses Groq's **LLaMA 3.3-70B Versatile** model for intelligent and structured responses.
-  **Multiple Agents**:
  - **Web Agent**: Searches the web and provides sources.
  - **Finance Agent**: Retrieves stock-related insights and financial data.
  - **Agent Team**: Coordinates both agents for comprehensive responses.
-  **Formatted Data**: Displays financial data in tables for better readability.

## Tech Stack

- **Programming Language**: Python 
- **Framework**: Streamlit 
- **AI Models**: Groq's LLaMA 3.3-70B Versatile 
- **APIs**:
  - DuckDuckGo for web search 
  - YFinance for financial data 
  - Phi Agents for AI-powered assistance 

## Installation & Setup

### Prerequisites

Ensure you have Python installed (preferably 3.8+).

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/Zaheerkhn/Finance-Assistant
cd finance-assistant
```

### 2️⃣ Create a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate  # On Windows
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Set Up Environment Variables

Create a `.env` file in the root directory and add your **GROQ API Key**:

```
GROQ_API_KEY=your_api_key_here
```

### 5️⃣ Run the Application

```bash
streamlit run app.py
```

## Usage

1. Open the application in your browser.
2. Enter a **financial** or **general** query in the input box.
3. The AI agents will process the request and display a response.
4. For financial queries, data will be structured in tables.

## Example Queries

- *"What is the current stock price of Tesla?"*
- *"Give me an overview of Apple's financials."*
- *"Who is the CEO of Microsoft?"*
- *"Find the latest tech trends."*

## License

This project is licensed under the **Apache License 2.0**.

## Contributors

Developed by **Zaheer Khan**. Contributions are welcome! Open an issue or submit a pull request to improve the application. 🚀

---

Feel free to modify the README based on your preferences! 🚀


