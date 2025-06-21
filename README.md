# 🕸️ AI Webscraper Agent

An AI-powered webscraping agent that uses the Brightdata MCP server to extract and summarize content from the web. Built with a modular architecture combining LLM reasoning, robust scraping, and a simple web interface.

---

## 🔧 Tech Stack

- **Frontend**: [Streamlit](https://streamlit.io/)
- **Backend**: [FastAPI](https://fastapi.tiangolo.com/)
- **Language**: Python
- **Scraping**: [Brightdata MCP Server](https://brightdata.com/)
- **AI Model**: Anthropic LLM (Claude)

---

## 🚀 Features

- Natural language interface to extract data from websites
- Uses Brightdata MCP for reliable web scraping
- LLM-powered summarization and reasoning
- Streamlit-based interactive frontend
- Async FastAPI backend integration

---

## Environment Variables

Create a .env file and configure the following:

```dotenv
# .env
# Environment Variables for AI Webscraper Agent
# Replace 'your_key_here' with your actual API keys

BRIGHTDATA_API_KEY=your_key_here
ANTHROPIC_API_KEY=your_key_here
MCP_SERVER_URL=https://your-brightdata-mcp-server
```

## 📦 Installation

```bash
git clone https://github.com/yourusername/ai-webscraper-agent.git
cd ai-webscraper-agent

uv pip install -r requirements.txt
```

## RUN App

### Start the FastAPI backend server and Streamlit app'

### Start the backend FastAPI server

```bash
uv run backend.py
```

### Start frontend Streamlit app

```bash
streamlit run frontend.py
```

## Example Usage

## Ask:

```
Scrape the top 5 news headlines from https://bbc.com and summarize them.
```

## Get Response:

```
1. Headline A - Summary
2. Headline B - Summary
3. Headline C - Summary
...
```

## Agent Flow

[User Prompt] ➡ [Streamlit UI] ➡ [FastAPI Router] ➡ [LLM Agent]
➡ [Brightdata Tool via MCP] ➡ [LLM Summarization] ➡ [UI Response]
