from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
from langchain_mcp_adapters.tools import load_mcp_tools
from langgraph.prebuilt import create_react_agent
from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv
import asyncio
import os
from fastapi import FastAPI, HTTPException, File, Response
from fastapi.responses import FileResponse

from models import ScrapeRequest


app = FastAPI()
load_dotenv()

model = ChatAnthropic(
    model="claude-3-5-sonnet-20240620",
    temperature=0.7,
    max_tokens=1000,
)

server_params = StdioServerParameters(
    command="npx",
    env={
        "API_TOKEN": os.getenv("API_TOKEN"),
        # "BROWSER_AUTH": os.getenv("BROWSER_AUTH"),
        "WEB_UNLOCKER_ZONE": os.getenv("WEB_UNLOCKER_ZONE"),
    },
    # Make sure to update to the full absolute path to your math_server.py file
    args=["@brightdata/mcp"],
)


@app.get("/test")
async def test_endpoint():
    return {"message": "Hello, this is a test endpoint!"}


@app.get("/health")
async def health_check():
    return {"status": "ok"}


@app.post("/scrape-web")
async def chat_with_agent(request: ScrapeRequest) -> Response:
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()

            tools = await load_mcp_tools(session)
            agent = create_react_agent(
                model=model,
                tools=tools
            )

            # start conversation
            messages = [
                {
                    "role": "system",
                    "content": "You can use multiple tools in sequence to answer complex questions. Think step by step.",
                }
            ]

            user_input = request.topics.strip()

            # Add user message to history
            messages.append({"role": "user", "content": user_input})

            # Invoke the agent with the current messages
            # Call the agent with the full message history
            agent_response = await agent.ainvoke({"messages": messages})

            # Extract agent's reply and add to history
            ai_message = agent_response["messages"][-1].content
            print(f"Agent: {ai_message}")
            return Response(content=ai_message, media_type="text/plain")

if __name__ == "__main__":
    # asyncio.run(chat_with_agent())
    import uvicorn
    uvicorn.run(
        "backend:app",
        host="0.0.0.0",
        port=1234,
        reload=True
    )
