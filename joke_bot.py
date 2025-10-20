from langgraph.graph.state import CompiledStateGraph
from prompt_builder import build_prompt_from_config
from utils import load_yaml_config, load_llm
from langgraph.graph import StateGraph, END
from pydantic import BaseModel
from config.config import LLM

# --- Define State ---

class Joke(BaseModel):
    text: str
    category: str
    language: str

class AgenticJokeState(BaseModel):
    """State for the writer-critic loop."""
    latest_joke: str = ""
    approved: bool = False
    retry_count: int = 0
    category: str = 'general'
    language: str = 'english'


# --- Prompt Config ---

prompt_cfg = load_yaml_config()


# --- Writer-Critic Node Factories ---

# Node: Writer
def make_writer_node(writer_llm):
    def writer_node(state: AgenticJokeState) -> dict:
        config = prompt_cfg['joke_writer_config']
        prompt = build_prompt_from_config(config, input_data="")
        prompt += f"\n\nGenerate a Joke of category {state.category} & in language {state.language}."

        response = writer_llm.invoke(prompt)

        return {'latest_joke': response.content}
    
    return writer_node


# Node: Critic
def make_critic_node(critic_llm):
    def critic_node(state: AgenticJokeState) -> dict:
        config = prompt_cfg['joke_critic_config']
        prompt = build_prompt_from_config(config, input_data=state.latest_joke)

        decision = critic_llm.invoke(prompt).content.strip().lower()
        approved = 'yes' in decision

        return {'approved': approved, 'retry_count': state.retry_count + 1}
    
    return critic_node


# --- Routing ---

# writer-critic router
def writer_critic_router(state: AgenticJokeState) -> str:
    if state.approved or state.retry_count>=5:
        return "show_final_joke"
    
    return "writer"


# --- Graph Assembly ---

def build_joke_graph(
        writer_model: str = LLM,
        critic_model: str = LLM,
        writer_temp: float = 0.8,
        critic_temp: float = 0.1,
        api_key: str = None
) -> CompiledStateGraph:
    """
    Build a simplified graph for Streamlit that just runs the writer-critic loop
    and returns a single joke without any user interaction.
    """
    
    writer_llm = load_llm(writer_model, writer_temp, api_key)
    critic_llm = load_llm(critic_model, critic_temp, api_key)

    builder = StateGraph(AgenticJokeState)

    # Register nodes - only writer and critic needed
    builder.add_node("writer", make_writer_node(writer_llm))
    builder.add_node("critic", make_critic_node(critic_llm))

    # Set the entry point to writer
    builder.set_entry_point("writer")

    # Define transitions: writer -> critic
    builder.add_edge("writer", "critic")
    
    # Conditional routing from critic
    builder.add_conditional_edges(
        "critic",
        writer_critic_router,
        {
            "writer": "writer",
            "show_final_joke": END
        }
    )

    return builder.compile()


def generate_joke_with_critic(
    category: str = "general",
    language: str = "english",
    writer_temp: float = 0.8,
    critic_temp: float = 0.1,
    writer_model: str = LLM,
    critic_model: str = LLM,
    api_key: str = None
) -> Joke:
    """
    Generate a single joke using the writer-critic loop.
    This is the main function that Streamlit will call.
    
    Args:
        category: The joke category
        language: The language code for the joke
        writer_temp: Temperature for the writer LLM
        critic_temp: Temperature for the critic LLM
        writer_model: Model name for the writer
        critic_model: Model name for the critic
        
    Returns:
        A Joke object containing the approved joke
    """
    graph = build_joke_graph(
        writer_model=writer_model,
        critic_model=critic_model,
        writer_temp=writer_temp,
        critic_temp=critic_temp,
        api_key=api_key
    )
    
    # Run the graph with initial state
    final_state = graph.invoke(
        AgenticJokeState(
            category=category,
            language=language
        ),
        config={'recursion_limit': 50}
    )
    
    # Create and return the joke
    joke = Joke(
        text=final_state['latest_joke'],
        category=category,
        language=language
    )
    
    return joke
