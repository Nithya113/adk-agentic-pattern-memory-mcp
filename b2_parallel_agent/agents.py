from google.adk.agents import Agent, ParallelAgent, SequentialAgent
from google.adk.models.lite_llm import LiteLlm
from dotenv import load_dotenv

load_dotenv()

# Local Ollama via OpenAI-compatible API (avoids ollama_chat content-array bugs).
# Env: OPENAI_API_BASE=http://localhost:11434/v1  OPENAI_API_KEY=ollama
def ollama_model():
    return LiteLlm(model="openai/llama3.2:latest")

# Specialist Agent 1
museum_finder_agent = Agent(
    name="museum_finder_agent",
    model=ollama_model(),
    tools=[],
    instruction=(
        "You are a museum expert. Based on the user's query and your knowledge, "
        "suggest the best museum. Output only the museum's name."
    ),
    output_key="museum_result",
)

# Specialist Agent 2
concert_finder_agent = Agent(
    name="concert_finder_agent",
    model=ollama_model(),
    tools=[],
    instruction=(
        "You are an events guide. Based on the user's query and your knowledge, "
        "suggest a concert. Output only the concert name and artist."
    ),
    output_key="concert_result",
)

# Specialist Agent 3
restaurant_finder_agent = Agent(
    name="restaurant_finder_agent",
    model=ollama_model(),
    tools=[],
    instruction="""You are an expert food critic. Your goal is to find the best restaurant based on a user's request.

    When you recommend a place, you must output *only* the name of the establishment.
    For example, if the best sushi is at 'Jin Sho', you should output only: Jin Sho
    """,
    output_key="restaurant_result",
)


# ✨ The ParallelAgent runs all three specialists at once ✨
parallel_research_agent = ParallelAgent(
    name="parallel_research_agent",
    sub_agents=[museum_finder_agent, concert_finder_agent, restaurant_finder_agent],
)

# Agent to synthesize the parallel results
synthesis_agent = Agent(
    name="synthesis_agent",
    model=ollama_model(),
    instruction="""You are a helpful assistant. Combine the following research results into a clear, bulleted list for the user.
    - Museum: {museum_result}
    - Concert: {concert_result}
    - Restaurant: {restaurant_result}
    """,
)

# ✨ The SequentialAgent runs the parallel search, then the synthesis ✨
parallel_planner_agent = SequentialAgent(
    name="parallel_planner_agent",
    sub_agents=[parallel_research_agent, synthesis_agent],
    description="A workflow that finds multiple things in parallel and then summarizes the results.",
)

root_agent = parallel_planner_agent
print("🤖 Agent team supercharged with a ParallelAgent workflow (Ollama)!")
