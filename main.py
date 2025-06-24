from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from groq_agent import get_answer

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "VM Chatbot API is running"}

@app.post("/chat")
def chat(question: str = Query(..., description="Ask your VM-related question")):
    answer = get_answer(question)
    return {"response": answer}



# 🔍 General Enquiry Questions
# How many enquiries were received today / this week / this month?

# Which regions have received the most enquiries recently?

# Can you show me all enquiries from a specific region like Bangalore or East Delhi?

# How many unique venues were enquired about last month?

# 📅 Date/Time-Based
# What was the busiest day or time for enquiries?

# Can I see the trend of enquiries over the last 30 days?

# Show enquiries made on weekends vs weekdays.

# 💼 Business Insights
# How many enquiries resulted in bookings?

# What is the total revenue generated this month?

# Which venue type generates the highest revenue?

# Who are the top 5 customers based on revenue?

# 🤖 Agent Allocation & Efficiency
# How many leads were agent-allocated vs not?

# Do bookings happen more often when an agent is allocated?

# Which agent-handled region had the best performance?

# 🧼 Data Quality Checks
# How many entries have missing phone numbers or email addresses?

# List entries where the venue type is missing.

# Are there any duplicate enquiries based on phone number?

# 🕵️‍♂️ Specific Queries
# Show me all enquiries for a ‘Wedding’ occasion.

# List enquiries where the revenue is above ₹50,000.

# Filter enquiries that did not convert into bookings.

