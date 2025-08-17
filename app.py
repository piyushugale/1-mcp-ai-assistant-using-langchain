from dotenv import load_dotenv
from langchain_groq import ChatGroq
from mcp_use import MCPAgent, MCPClient
import os
import asyncio

async def run_chat():
    """Run a chat using MCP Agent with conversational memory"""
    try:
        # Load environment variables
        load_dotenv()
        groq_api_key = os.getenv("GROQ_API_KEY")
        
        if not groq_api_key:
            print("Error: GROQ_API_KEY not found in environment variables")
            return
        
        # Initialize MCP client
        client = MCPClient.from_config_file("mcp_config.json")
        
        # Initialize LLM
        llm = ChatGroq(
            model="llama3-8b-8192",
            api_key=groq_api_key,
            temperature=0.7
        )
        
        # Initialize MCP Agent
        agent = MCPAgent(
            llm=llm,
            client=client,
            verbose=True,
            memory_enabled=True,
            max_steps=15,
        )
        
        print("Chat initialized successfully. Type 'exit' to quit.")
        
        # Interactive chat loop
        while True:
            try:
                user_input = input("You: ")
                if user_input.lower() in ['exit', 'quit', 'bye']:
                    break
                
                if user_input.strip():
                    response = await agent.run(user_input)
                    print(f"AI: {response}")
                    
            except KeyboardInterrupt:
                print("\nChat interrupted by user")
                break
            except Exception as e:
                print(f"Error: {e}")
                continue
                
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    asyncio.run(run_chat())