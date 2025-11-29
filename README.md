# Customer Service Chatbot

##  Project Overview
This Customer Service Chatbot is a web-based application designed to handle common customer inquiries for an e-commerce platform. Built as part of an assignment for Adxreel, this project demonstrates the implementation of a responsive, user-friendly chatbot interface using modern web technologies.

## Features
- **Interactive Chat Interface**: Clean and intuitive UI for seamless user interaction
- **Predefined Questions**: Quick-access buttons for common customer inquiries
- **Responsive Design**: Works on both desktop and mobile devices
- **Local Processing**: No external API dependencies required for core functionality
- **Real-time Responses**: Instant answers to customer questions

##  Tech Stack

### Frontend
- **Streamlit**: For building and deploying the web application
- **HTML/CSS**: For custom styling and layout
- **JavaScript**: For interactive elements and dynamic content

### Backend
- **Python**: Core programming language
- **Streamlit Components**: For building the chat interface
- **Session State Management**: For maintaining conversation history

##  Project Structure
```
chatbot_Adxreel/
├── app.py               # Main application file
├── requirements.txt     # Python dependencies
├── .env.example        # Example environment variables
└── README.md           # Project documentation
```

##  Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Setup Instructions
1. Clone the repository:
   ```bash
   git clone (https://github.com/VidhyashreeX/ChatbotADXREEL)
   cd chatbot_Adxreel
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: .\venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the application:
   ```bash
   streamlit run app.py
   ```

5. Open your browser and navigate to `http://localhost:8501`
