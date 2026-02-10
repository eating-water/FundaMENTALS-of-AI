import streamlit as st

# =================================
# MCP-STYLE TOOLS (Separated Layer)
# ================================
def currency_tool(country):
    data = {
        "Japan": {"currency": "Japanese Yen (JPY)", "base": "JPY"},
        "India": {"currency": "Indian Rupee (INR)", "base": "INR"},
        "US": {"currency": "US Dollar (USD)", "base": "USD"},
        "UK": {"currency": "Pound Sterling (GBP)", "base": "GBP"},
        "China": {"currency": "Chinese Yuan (CNY)", "base": "CNY"},
        "South Korea": {"currency": "South Korean Won (KRW)", "base": "KRW"}
    }
    return data.get(country)

def exchange_rate_tool(base):
    # Mocked but realistic values
    rates = {
        "JPY": {"USD": 0.0067, "INR": 0.56, "GBP": 0.0053, "EUR": 0.0062},
        "INR": {"USD": 0.012, "GBP": 0.0096, "EUR": 0.011, "INR": 1},
        "USD": {"USD": 1, "INR": 83, "GBP": 0.79, "EUR": 0.92},
        "GBP": {"USD": 1.26, "INR": 104, "GBP": 1, "EUR": 1.16},
        "CNY": {"USD": 0.14, "INR": 11.5, "GBP": 0.11, "EUR": 0.13},
        "KRW": {"USD": 0.00075, "INR": 0.062, "GBP": 0.00059, "EUR": 0.00069}
    }
    return rates.get(base)

def stock_market_tool(country):
    markets = {
        "Japan": {
            "exchange": "Tokyo Stock Exchange",
            "index": "Nikkei 225",
            "value": "38,500",
            "map": "https://www.google.com/maps?q=Tokyo+Stock+Exchange"
        },
        "India": {
            "exchange": "Bombay Stock Exchange",
            "index": "SENSEX",
            "value": "72,300",
            "map": "https://www.google.com/maps?q=Bombay+Stock+Exchange"
        },
        "US": {
            "exchange": "NYSE",
            "index": "S&P 500",
            "value": "4,950",
            "map": "https://www.google.com/maps?q=New+York+Stock+Exchange"
        },
        "UK": {
            "exchange": "London Stock Exchange",
            "index": "FTSE 100",
            "value": "7,650",
            "map": "https://www.google.com/maps?q=London+Stock+Exchange"
        },
        "China": {
            "exchange": "Shanghai Stock Exchange",
            "index": "SSE Composite",
            "value": "3,050",
            "map": "https://www.google.com/maps?q=Shanghai+Stock+Exchange"
        },
        "South Korea": {
            "exchange": "Korea Exchange",
            "index": "KOSPI",
            "value": "2,620",
            "map": "https://www.google.com/maps?q=Korea+Exchange"
        }
    }
    return markets.get(country)

# =================================
# AGENT (LLM Reasoning Layer)
# =================================

def finance_agent(query):
    countries = ["Japan", "India", "US", "UK", "China", "South Korea"]
    country = next((c for c in countries if c.lower() in query.lower()), None)

    if not country:
        return "❌ Country not supported."

    currency = currency_tool(country)
    rates = exchange_rate_tool(currency["base"])
    market = stock_market_tool(country)

    response = f"""
## 🌍 Country: {country}

### 💱 Official Currency
**{currency['currency']}**

---

### 🔄 Exchange Rates (1 {currency['base']})
- USD: {rates.get("USD")}
- INR: {rates.get("INR")}
- GBP: {rates.get("GBP")}
- EUR: {rates.get("EUR")}

---

### 📈 Stock Market Details
- **Stock Exchange:** {market['exchange']}
- **Major Index:** {market['index']}
- **Current Index Value:** {market['value']}

---

### 📍 Stock Exchange HQ Location
[View on Google Maps]({market['map']})
"""
    return response

# =================================
# STREAMLIT UI
# =================================

st.set_page_config(page_title="Currency & Stock Market Agent", layout="wide")

st.title("💹 AI Currency & Stock Market Agent")
st.write("LLM Agent using MCP-style tool orchestration")

user_query = st.text_input(
    "Enter your query",
    placeholder="Give me currency and stock market details for Japan"
)

if st.button("Get Details"):
    if user_query.strip():
        with st.spinner("Fetching financial data..."):
            output = finance_agent(user_query)
        st.markdown(output)
    else:
        st.warning("Please enter a valid query.")
