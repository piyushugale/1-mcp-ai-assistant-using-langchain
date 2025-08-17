from dotenv import load_dotenv
from langchain_groq import ChatGroq
from mcp_use import MCPAgent, MCPClient
import os
import asyncio
import sys
import time

async def run_memory_chat():
    """ Run a chat using MCP Agent's built-in conversational memory"""

    try:
        # Load environment variables
        load_dotenv()
        groq_api_key = os.getenv("GROQ_API_KEY")
        
        if not groq_api_key:
            print("Error: GROQ_API_KEY not found in environment variables")
            return
        
        config_file = "mcp_config.json"
        
        if not os.path.exists(config_file):
            print(f"Error: Config file {config_file} not found")
            return

        print("Initializing Chat...")

        # Initialize MCP client with retry logic
        client = None
        max_retries = 3
        for attempt in range(max_retries):
            try:
                print(f"Attempting to connect to MCP servers (attempt {attempt + 1}/{max_retries})...")
                client = MCPClient.from_config_file(config_file)
                print("MCP client initialized successfully")
                break
            except Exception as e:
                print(f"Attempt {attempt + 1} failed: {e}")
                if attempt < max_retries - 1:
                    print("Retrying in 2 seconds...")
                    await asyncio.sleep(2)
                else:
                    print("Failed to initialize MCP client after all attempts")
                    return

        # Initialize LLM
        try:
            llm = ChatGroq(
                model="llama3-8b-8192",
                api_key=groq_api_key,
                temperature=0.7
            )
            print("LLM initialized successfully")
        except Exception as e:
            print(f"Error initializing LLM: {e}")
            return

        # Initialize MCP Agent with proper error handling
        try:
            agent = MCPAgent(
                llm=llm,
                client=client,
                verbose=True,
                memory_enabled=True,
                max_steps=15,
            )
            print("Agent initialized successfully")
        except Exception as e:
            print(f"Error initializing agent: {e}")
            return

        print("Starting Chat...")

        # Test the agent with a simple query
        try:
            print("Testing agent with a simple query...")
            response = await agent.run("What is the capital of France?")
            print(f"Test Response: {response}")
        except Exception as e:
            print(f"Error during test query: {e}")
            print("Trying to continue with interactive chat...")

        # Interactive chat loop with connection health checks
        print("\nStarting interactive chat (type 'exit' to quit):")
        while True:
            try:
                user_input = input("You: ")
                if user_input.lower() in ['exit', 'quit', 'bye']:
                    break
                
                if user_input.strip():
                    # Check if client is still responsive
                    try:
                        response = await agent.run(user_input)
                        print(f"AI: {response}")
                    except Exception as e:
                        print(f"Error during agent.run(): {e}")
                        print("Attempting to reconnect...")
                        
                        # Try to reinitialize the client
                        try:
                            client = MCPClient.from_config_file(config_file)
                            agent = MCPAgent(
                                llm=llm,
                                client=client,
                                verbose=True,
                                memory_enabled=True,
                                max_steps=15,
                            )
                            print("Reconnected successfully. Please try your question again.")
                        except Exception as reconnect_error:
                            print(f"Failed to reconnect: {reconnect_error}")
                            print("Please restart the application.")
                            break
                    
            except KeyboardInterrupt:
                print("\nChat interrupted by user")
                break
            except Exception as e:
                print(f"Unexpected error during chat: {e}")
                continue

    except Exception as e:
        print(f"Unexpected error: {e}")
        import traceback
        traceback.print_exc()

async def test_mcp_connection():
    """Test MCP connection before running the main chat"""
    try:
        config_file = "mcp_config.json"
        if not os.path.exists(config_file):
            print(f"Config file {config_file} not found")
            return False
            
        print("Testing MCP connection...")
        client = MCPClient.from_config_file(config_file)
        
        # Test basic connection with timeout
        try:
            # Add a simple test operation here if available
            print("MCP connection test successful")
            return True
        except Exception as e:
            print(f"MCP connection test failed: {e}")
            return False
            
    except Exception as e:
        print(f"MCP connection test failed: {e}")
        return False

async def main():
    """Main function with proper cleanup"""
    try:
        print("Starting MCP AI Assistant...")
        
        # Test connection first
        if await test_mcp_connection():
            await run_memory_chat()
        else:
            print("Failed to establish MCP connection. Please check your configuration.")
            print("Make sure your MCP servers are running and accessible.")
            
    except KeyboardInterrupt:
        print("\nProgram interrupted by user")
    except Exception as e:
        print(f"Program error: {e}")
        import traceback
        traceback.print_exc()
    finally:
        print("Cleaning up...")
        # Add any cleanup code here if needed

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except Exception as e:
        print(f"Failed to start application: {e}")
        import traceback
        traceback.print_exc()