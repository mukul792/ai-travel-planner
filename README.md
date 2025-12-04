# 🧳 AI Travel Itinerary Planner — Groq-Powered Multi-Day Trip Planner

A Streamlit application that generates fully personalized **multi-day travel itineraries** using Groq’s ultra-fast **Llama-3.3 70B** model.  
Just enter your **city** and **number of days**, and the app builds a complete, structured travel plan with attractions, food recommendations, and useful travel tips.

This project integrates **Groq LLM**, **LangChain**, and **Streamlit** to deliver a smooth, fast, and highly detailed itinerary planning experience.

---

![Alt text]("ai travel planner/travel.png")

---

## 🚀 Features

- Enter any city to generate a custom itinerary  
- Choose number of days (1 to 30)  
- AI-generated **day-wise travel plan**  
- Morning / Afternoon / Evening breakdown  
- Must-visit attractions with short descriptions  
- Local food & restaurant suggestions  
- Travel tips for each day  
- Clean and modern Streamlit user interface  
- Fast generation powered by Groq’s low-latency Llama model  

---

## 🛠️ Tech Stack Overview

- **LLM:** Groq — Llama-3.3 70B Versatile  
- **Framework:** LangChain  
- **UI:** Streamlit  
- **Environment Management:** python-dotenv  
- **Backend Logic:** Custom TravelPlanner class  
- **Prompting:** ChatPromptTemplate with structured multi-day format  

---

## 📦 Project Setup

1. Install all required Python dependencies  
2. Create a `.env` file and add your **GROQ_API_KEY**  
3. Run the Streamlit application  
4. Enter the city name and number of days  
5. Get a fully formatted multi-day itinerary instantly  

---

## 📂 Folder Structure

- **app.py** — Main Streamlit application  
- **src/core/planner.py** — TravelPlanner class  
- **src/chains/itinerary_chain.py** — LLM prompt + Groq invocation  
- **src/utils/logger.py** — Logging utility  
- **src/utils/custom_exception.py** — Custom exception handler  
- **src/config/config.py** — API key loading  
- **.env** — Groq API key  
- **requirements.txt** — Project dependencies  

---

## 🧠 How the App Works

- User provides **city** + **number of days**  
- The LLM prompt constructs a structured request for a multi-day itinerary  
- LangChain sends the formatted prompt to Groq’s Llama-3.3 model  
- The AI generates a detailed plan including:  
  - Morning / Afternoon / Evening activities  
  - Must-visit places  
  - Food recommendations  
  - Travel estimates  
  - Daily tips  
- The final itinerary is displayed clearly in the Streamlit UI  

---

## 📸 Use Cases

- Quick vacation planning  
- Multi-day trip research  
- Discovering attractions in a new city  
- Helping students, families, couples plan personalized trips  
- Travel agencies generating fast draft itineraries  

---

## 🔮 Future Enhancements

- Add hotel recommendations  
- Add estimated budget for each day  
- Add attractive images for each attraction  
- Export itinerary to PDF  
- Save past itineraries  
- Add map integration (Google Maps API)  
- Add chat-based AI travel assistant  

---

## ⭐ Support This Project

If you like this project, consider starring the repository or sharing it with others!

