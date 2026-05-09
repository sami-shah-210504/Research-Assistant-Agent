import os
import requests
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain.prompts import ChatPromptTemplate


system_prompt = """
You are a professional research assistant. Your goal is to produce comprehensive, reliable, and well-structured research reports.

### Instructions:
1. **Depth & Accuracy**
   - Provide detailed explanations with context and background where needed.
   - Ensure information is factually correct and clearly distinguish between established knowledge and recent developments.

2. **Use of Sources**
   - Integrate recent news articles, academic papers, and credible web sources.
   - Always cite sources in markdown format with inline citations (e.g., [Source Name, Year](link)).
   - Prefer authoritative sources (peer-reviewed journals, reputable news outlets, government or institutional sites).

3. **Formatting**
   - Use clear markdown structure:
     - # Title
     - ## Introduction
     - ## Key Insights
     - ## Recent News & Developments
     - ## Challenges & Open Questions
     - ## Conclusion
     - ## References
   - Use bullet points and numbered lists for readability.

4. **Style**
   - Write in an objective, professional, and concise tone.
   - Avoid fluff or repetition.
   - When data is limited, explicitly state limitations instead of guessing.

5. **Output Goal**
   - Deliver a polished research report that:
     - Summarizes the topic comprehensively.
     - Highlights recent news/events.
     - Cites all references.
     - Is ready for inclusion in academic or professional reports.
"""
# Load API keys
load_dotenv()
groq_api_key = os.getenv("GROQ_API_KEY")
news_api_key = os.getenv("NEWS_API_KEY")

# Initialize Groq LLM
llm = ChatGroq(
    groq_api_key=groq_api_key,
    model="llama-3.3-70b-versatile",  # or "llama-3.1-8b-instant"
    temperature=0
)

# Function to fetch latest news
def fetch_news(query, api_key):
    url = f"https://newsapi.org/v2/everything?q={query}&sortBy=publishedAt&language=en&apiKey={api_key}"
    response = requests.get(url)
    data = response.json()
    if "articles" in data:
        articles = data["articles"][:5]  # Get top 5 latest
        return "\n".join([f"- {a['title']} ({a['source']['name']})" for a in articles])
    return "No news found."

# Define research prompt
prompt = ChatPromptTemplate.from_messages([
    ("system", system_prompt),
    ("human", "Research topic: {topic}\n\nRecent news:\n{news}")
])

# Ask user for topic
topic = input("Enter a research topic: ")

# Fetch live news
news_summary = fetch_news(topic, news_api_key)

# Generate response
chain = prompt | llm
response = chain.invoke({"topic": topic, "news": news_summary})

print("\n📌 Research Report has been generated\nCheck File Directory\n")

# Save report to markdown file in Research Assistant Agent folder
report_md = f"# Research Report\n\n## Topic: {topic}\n\n### Recent News\n{news_summary}\n\n### LLM Analysis\n{response.content}\n"
output_path = os.path.join(os.path.dirname(__file__), "research_report.md")
with open(output_path, "w", encoding="utf-8") as f:
    f.write(report_md)

print(f"\n✅ Research report saved to {output_path}")
