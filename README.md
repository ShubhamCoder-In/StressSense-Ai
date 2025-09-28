# StressSense AI

**Hackathon:** Samadhan 2.0  
**Team:** [Your Team Name]  
**Project:** StressSense AI – Powered Mental Wellness Platform  

---

## **Project Overview**

StressSense AI is an **AI-powered mental wellness platform** aimed at **detecting student stress levels** and providing **personalized suggestions** to improve academic performance and emotional well-being. The system is designed to analyze student responses, monitor stress patterns, and offer actionable insights using AI-powered APIs like **Gemini**.

This project was developed for the **Samadhan 2.0 Hackathon** with a focus on leveraging **technology for student mental health**.

---

## **Problem Statement**

Students often experience stress, anxiety, and lack of motivation due to heavy workloads and academic pressure. There is a need for a **smart platform** that can:

- Detect stress levels in real-time
- Provide personalized recommendations
- Track improvements over time
- Help students adopt healthier study routines  

---

## **Our Approach**

1. **Data Collection**
   - Students fill in **survey-based assessments** about difficulty, motivation, stress, and coping.
   - Responses are stored in **MongoDB Atlas**.

2. **Analysis**
   - Student responses are sent to a **Flask backend**.
   - AI APIs (Gemini) analyze the responses for **stress, emotions, and engagement**.

3. **Personalized Suggestions**
   - Based on AI analysis, the system provides **structured suggestions**.
   - Suggestions are displayed in **dashboard with charts and trends**.

4. **Frontend**
   - Built using **HTML, CSS, Bootstrap, and JavaScript**.
   - Interactive dashboard with **charts**, **cards**, and **quick links**.
   - Users can see their stress trends, tasks, notifications, and recommendations.

5. **Backend**
   - Flask server with **REST APIs** to handle assignments, surveys, and suggestions.
   - **MongoDB** database stores student data and predictions.
   - **Gemini API** integration provides AI-generated insights.

---

## **Features**

- Student Dashboard with **stress trends** and **recommendations**
- Personalized suggestions powered by AI
- Survey management system
- Historical performance tracking
- Interactive frontend with charts and statistics
- Role-based access (Admin / Expert / Student)

---

## **Tech Stack**

- **Frontend:** HTML, CSS, Bootstrap, JavaScript
- **Backend:** Python, Flask
- **Database:** MongoDB Atlas
- **AI Integration:** Gemini API (Google)
- **Charts & Visualization:** Chart.js / Canvas API

---

## **Installation**

1. Clone the repository:

```bash
git clone https://github.com/yourusername/stresssense-ai.git
cd stresssense-ai
Create a virtual environment:

bash
Copy code
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
Install dependencies:

bash
Copy code
pip install -r requirements.txt
Add environment variables:

ini
Copy code
MONGO_URI=<your_mongodb_uri>
GEMINI_API_KEY=<your_gemini_api_key>
SECRET_KEY=<your_flask_secret>
Run the Flask server:

bash
Copy code
python app.py
