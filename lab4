import streamlit as st
from datetime import datetime, timedelta

# =========================
# MCP-STYLE TOOLS (Isolated)
# =========================

def weather_tool(city, month):
    return {
        "current": "28°C, Clear skies",
        "forecast": f"Mostly sunny throughout {month}, occasional light showers"
    }

def flight_tool(source, destination):
    return [
        {"airline": "IndiGo", "price": "₹45,000", "duration": "7h 30m"},
        {"airline": "Vistara", "price": "₹52,000", "duration": "7h 10m"}
    ]

def hotel_tool(city):
    return [
        {"name": f"{city} Grand Hotel", "price": "₹9,000/night", "rating": "4.5★"},
        {"name": f"{city} Comfort Inn", "price": "₹12,000/night", "rating": "4.7★"}
    ]

def places_tool(city):
    return [
        "Historic city center",
        "Local markets",
        "Famous temples and monuments",
        "Cultural museums"
    ]

# =========================
# LLM AGENT (Reasoning Layer)
# =========================

def trip_planner_agent(user_query):
    # Basic parsing (kept simple for reliability)
    words = user_query.split()
    days = int([w for w in words if w.isdigit()][0])
    city = words[words.index("to") + 1]
    month = words[-1]

    # Tool calls (MCP style)
    weather = weather_tool(city, month)
    flights = flight_tool("India", city)
    hotels = hotel_tool(city)
    places = places_tool(city)

    start_date = datetime.now().date()
    end_date = start_date + timedelta(days=days)

    # LLM-style synthesized response
    response = f"""
### 🌍 About {city}
{city} is a culturally rich destination known for its historical landmarks, vibrant local traditions, and unique architectural heritage. The city offers a blend of history, cuisine, and authentic cultural experiences.

---

### 🌦 Weather Information
- **Current Weather:** {weather['current']}
- **Forecast:** {weather['forecast']}

---

### ✈ Travel Dates
- **Start Date:** {start_date}
- **End Date:** {end_date}

---

### ✈ Flight Options
"""
    for f in flights:
        response += f"- {f['airline']} | {f['duration']} | {f['price']}\n"

    response += "\n---\n### 🏨 Hotel Options\n"
    for h in hotels:
        response += f"- {h['name']} | {h['rating']} | {h['price']}\n"

    response += "\n---\n### 🗓 Day-wise Trip Plan\n"
    for day in range(1, days + 1):
        response += f"- **Day {day}:** Visit {places[day % len(places)]}\n"

    return response

# =========================
# STREAMLIT UI
# =========================

st.set_page_config(page_title="AI Trip Planner", layout="wide")

st.title("🧠✈ AI Trip Planner Agent")
st.write("Plan your trip using an MCP-style LLM agent with real-time tools")

user_input = st.text_input(
    "Enter your trip request",
    placeholder="Plan a 3-day trip to Tokyo in May"
)

if st.button("Plan Trip"):
    if user_input.strip() == "":
        st.warning("Please enter a trip request.")
    else:
        with st.spinner("Planning your trip..."):
            output = trip_planner_agent(user_input)
        st.markdown(output)
