# Research Assistant Agent

This project is an AI-powered research assistant that generates detailed research reports on any topic, enhanced with recent news and reliable sources. It leverages the Groq LLM (LLaMA 3) and NewsAPI to provide up-to-date, well-structured information in markdown format.

## Features

- **Live News Integration:** Fetches the latest news articles relevant to your research topic.
- **LLM-Powered Analysis:** Uses Groq LLM to generate comprehensive, reliable, and well-cited research reports.
- **Markdown Output:** Saves each report in markdown format with clear headings and bullet points.
- **Customizable Topics:** Allows users to research any topic interactively.

## How It Works

1. **User Input:** Enter a research topic when prompted.
2. **News Fetching:** The assistant retrieves recent news articles using NewsAPI.
3. **LLM Analysis:** The Groq LLM analyzes the topic and news, generating a detailed report.
4. **Markdown Report:** The report is saved as `research_report.md` in the project folder.

## Setup

1. **Clone the repository** and navigate to the project directory.
2. **Create a `.env` file** in the project root with your API keys:
    ```
    GROQ_API_KEY=your_groq_api_key
    NEWS_API_KEY=your_newsapi_key
    ```
3. **Install dependencies:**
    ```powershell
    pip install -r requirements.txt
    ```
4. **Run the assistant:**
    ```powershell
    python research_assistant.py
    ```

## Output Example

See [`research_report.md`](research_report.md) for a sample report on "Electric Cars".

## Dependencies

- Python 3.8+
- [langchain_groq](https://pypi.org/project/langchain-groq/)
- [python-dotenv](https://pypi.org/project/python-dotenv/)
- [requests](https://pypi.org/project/requests/)

## License

This project is for educational and research purposes.

---
*Created by Syed S.*
