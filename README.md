# MCP AI Assistant using LangChain

A powerful AI assistant that leverages Model Context Protocol (MCP) and LangChain to provide intelligent conversational capabilities with access to various tools and services.

## 🚀 Features

- **MCP Integration**: Connects to MCP servers for extended functionality
- **LangChain Powered**: Built on LangChain framework for robust AI interactions
- **Conversational Memory**: Maintains context across conversation sessions
- **Groq LLM**: Uses Groq's high-performance language models
- **Interactive Chat**: Real-time conversation interface
- **Error Handling**: Robust error handling and recovery mechanisms

## 📋 Prerequisites

- Python 3.8 or higher
- pip or uv package manager
- Access to Groq API
- MCP servers running (if using MCP functionality)

## 🛠️ Installation

### 1. Clone the Repository
```bash
git clone <your-repository-url>
cd 1-mcp-ai-assistant-using-langchain
```

### 2. Install Dependencies

#### Using uv (Recommended)
```bash
uv sync
```

#### Using pip
```bash
pip install -r requirements.txt
```

### 3. Environment Setup
Create a `.env` file in the project root:
```bash
# Groq API Configuration
GROQ_API_KEY=your_groq_api_key_here

# MCP Configuration (if applicable)
MCP_SERVER_URL=your_mcp_server_url
MCP_API_KEY=your_mcp_api_key
```

### 4. MCP Configuration
Ensure your `mcp_config.json` file is properly configured:
```json
{
  "mcpServers": {
    "server_name": {
      "command": "path_to_server_executable",
      "args": ["arg1", "arg2"],
      "env": {
        "ENV_VAR": "value"
      }
    }
  }
}
```

## 🔧 Configuration

### Groq API Setup
1. Visit [Groq Console](https://console.groq.com/)
2. Create an account and generate an API key
3. Add the API key to your `.env` file

### MCP Server Setup
1. Install and configure your MCP servers
2. Update `mcp_config.json` with server details
3. Ensure servers are running before starting the application

## 🚀 Usage

### Basic Usage
```bash
python app.py
```

### Advanced Usage
```python
from app import run_chat
import asyncio

# Run the chat programmatically
asyncio.run(run_chat())
```

### Interactive Commands
- Type your questions or requests normally
- Use `exit`, `quit`, or `bye` to end the session
- Press `Ctrl+C` to interrupt the chat

## 📁 Project Structure

```
1-mcp-ai-assistant-using-langchain/
├── app.py                 # Main application file
├── mcp_config.json       # MCP server configuration
├── pyproject.toml        # Project dependencies and metadata
├── uv.lock              # Lock file for reproducible builds
├── .env                 # Environment variables (create this)
├── requirements.txt     # Python dependencies
└── README.md           # This file
```

## 🔌 Dependencies

### Core Dependencies
- `langchain-groq`: Groq integration for LangChain
- `python-dotenv`: Environment variable management
- `mcp-use`: MCP client and agent utilities

### Development Dependencies
- `uv`: Modern Python package manager
- `pytest`: Testing framework (if applicable)

## ⚙️ Configuration Options

### LLM Configuration
```python
llm = ChatGroq(
    model="llama3-8b-8192",    # Model name
    api_key=groq_api_key,      # API key
    temperature=0.7            # Creativity level (0.0-1.0)
)
```

### Agent Configuration
```python
agent = MCPAgent(
    llm=llm,                   # Language model
    client=client,             # MCP client
    verbose=True,              # Enable verbose output
    memory_enabled=True,       # Enable conversation memory
    max_steps=15,             # Maximum reasoning steps
)
```

## 🐛 Troubleshooting

### Common Issues

#### 1. GROQ_API_KEY not found
```bash
Error: GROQ_API_KEY not found in environment variables
```
**Solution**: Ensure your `.env` file exists and contains the correct API key.

#### 2. MCP Connection Failed
```bash
Error: Failed to connect to MCP servers
```
**Solution**: 
- Check if MCP servers are running
- Verify `mcp_config.json` configuration
- Ensure network connectivity

#### 3. Import Errors
```bash
ModuleNotFoundError: No module named 'langchain_groq'
```
**Solution**: Install dependencies using `uv sync` or `pip install -r requirements.txt`

### Debug Mode
Enable verbose logging by setting `verbose=True` in the agent configuration.

## 🔒 Security Considerations

- Never commit your `.env` file to version control
- Keep your API keys secure and rotate them regularly
- Use environment variables for sensitive configuration
- Validate MCP server connections before production use

## 📝 API Reference

### Main Functions

#### `run_chat()`
Main function that initializes and runs the interactive chat session.

**Returns**: None

**Raises**: 
- `Exception`: If initialization fails
- `KeyboardInterrupt`: If user interrupts the session

### Classes Used

#### `MCPClient`
Handles communication with MCP servers.

#### `MCPAgent`
AI agent that processes user input and generates responses.

#### `ChatGroq`
Language model interface for Groq API.

## 🧪 Testing

### Running Tests
```bash
# If using pytest
pytest

# If using unittest
python -m unittest discover
```

### Test Coverage
Ensure your tests cover:
- Environment variable loading
- MCP client initialization
- Agent response generation
- Error handling scenarios

## 📊 Performance

### Optimization Tips
- Use appropriate model sizes for your use case
- Adjust `max_steps` based on complexity requirements
- Monitor API usage and costs
- Implement caching for repeated queries

### Resource Requirements
- **Memory**: Minimum 2GB RAM
- **Storage**: 100MB for dependencies
- **Network**: Stable internet connection for API calls

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Development Setup
```bash
# Clone your fork
git clone <your-fork-url>

# Install development dependencies
uv sync --dev

# Run tests
pytest

# Format code
black .
```

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [LangChain](https://langchain.com/) for the AI framework
- [Groq](https://groq.com/) for the language models
- [MCP](https://modelcontextprotocol.io/) for the protocol specification
- [uv](https://github.com/astral-sh/uv) for modern Python packaging

## 📞 Support

### Getting Help
- Check the [Issues](https://github.com/your-repo/issues) page
- Review the troubleshooting section above
- Search existing discussions

### Reporting Issues
When reporting issues, please include:
- Python version
- Operating system
- Error messages
- Steps to reproduce
- Configuration files (without sensitive data)

## 🔄 Changelog

### Version 1.0.0
- Initial release
- Basic MCP integration
- Groq LLM support
- Interactive chat interface

## 📈 Roadmap

- [ ] Enhanced error recovery
- [ ] Multiple LLM provider support
- [ ] Web interface
- [ ] Plugin system
- [ ] Advanced memory management
- [ ] Performance monitoring

---

**Note**: This is a development version. For production use, ensure proper testing and security measures are in place.
