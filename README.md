# ADK agentic patterns (Memory + MCP)

Hands-on Google ADK tutorial covering multi-agent workflows for trip planning.

## What I learned

| Pattern | Folder | Example prompt |
|---------|--------|----------------|
| **Sequential** | `b1_sequential_agent` | Find the best sushi restaurant in Bangalore, then directions from MG Road. |
| **Parallel** | `b2_parallel_agent` | Suggest a museum, a concert, and a restaurant for a weekend in Bangalore. |
| **Loop** | `b3_loop_agent` | Plan one activity + one restaurant in SF with travel time under 45 minutes. |
| **Custom** | `c_custom_agent` | I have a $100 budget—build a day plan in Sunnyvale. |
| **Routing** | `d_routing_agent` | I'm hungry for Italian near Indiranagar. |
| **Agent as tool** | `e_agent_as_tool` | Plan a museum + dinner in Sunnyvale and validate logistics. |
| Single agent | `a_single_agent` | Weekend date plan in Bangalore, foodie + outdoors, July 19–20. |
| Memory | `f_agent_with_memory` | Remember I like Italian food, then plan something in Sunnyvale. |
| MCP tools | `g_agents_mcp` | Find top-rated museums in Tokyo under $20. |

## Local setup (short)

**Prereqs:** Python 3.12+, [Ollama](https://ollama.com) with `llama3.2`

```bash
git clone https://github.com/Nithya113/adk-agentic-pattern-memory-mcp.git
cd adk-agentic-pattern-memory-mcp

# Prefer Homebrew Python on Mac (avoids Anaconda openssl issues)
/opt/homebrew/bin/python3.12 -m venv .adk_env
source .adk_env/bin/activate
pip install -U pip
pip install -r requirements.txt
pip install litellm

# Optional: Gemini API (not needed if using Ollama)
# cat > .env <<'EOF'
# GOOGLE_GENAI_USE_VERTEXAI=FALSE
# GOOGLE_API_KEY=your_key
# EOF

# Ollama (OpenAI-compatible)
cat >> .env <<'EOF'
OLLAMA_API_BASE=http://localhost:11434
OPENAI_API_BASE=http://localhost:11434/v1
OPENAI_API_KEY=ollama
EOF

ollama pull llama3.2
adk web   # http://127.0.0.1:8000
```

### MCP trip agent (optional)

```bash
python setup_trip_database.py

# Terminal 1 — download toolbox for your OS from genai-toolbox, then:
cd mcp_tool_box
chmod +x toolbox
./toolbox --tools-file trip_tools.yaml --port 7001

# Terminal 2
cd g_agents_mcp && python main.py
# or use g_agents_mcp in ADK web while toolbox is running
```

Original course: [goo.gle/advancedadk](https://goo.gle/advancedadk)
