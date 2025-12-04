from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from src.config.config import GROQ_API_KEY

llm = ChatGroq(
    groq_api_key=GROQ_API_KEY,
    model_name="llama-3.3-70b-versatile",
    temperature=0.3
)

# Updated Prompt for Multi-Day Itinerary
itinerary_prompt = ChatPromptTemplate([
    ("system",
     "You are a professional travel planner. Create a well-structured itinerary for a {days}-day trip "
     "to the city: {city}. The itinerary must:\n"
     "• Be structured clearly as Day 1, Day 2, ..., Day N\n"
     "• Each day should include: morning, afternoon and evening plans\n"
     "• Include top attractions with 1 line descriptions\n"
     "• Suggest local vegetarian foods for morning, afternoon and evening\n"
     "• Provide approx travel time between places\n"
     "• Add useful travel tips for each day\n"
     "• Keep it clean, concise, and beginner-friendly"),
    ("human", "Create the itinerary.")
])


def generate_itinerary(city: str, days: int) -> str:
    response = llm.invoke(
        itinerary_prompt.format_messages(city=city, days=days)
    )
    return response.content
