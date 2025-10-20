from langchain_core.language_models.chat_models import BaseChatModel
from config.config import PROMPT_CONFIG_FILE_DIR
from langchain_groq import ChatGroq
from typing import Dict, Any
import yaml


def load_llm(model_name: str, temperature: float, api_key: str) -> BaseChatModel:
    if model_name == "llama-3.1-8b-instant":
        return ChatGroq(model="llama-3.1-8b-instant", temperature=temperature, api_key=api_key)
    else:
        raise ValueError(f"Unknown model name: {model_name}")


def load_yaml_config(config_path: str = PROMPT_CONFIG_FILE_DIR) -> Dict[str, Any]:
    """Loads a YAML configuration file and returns its contents as a dictionary."""
    with open(config_path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def get_categories():
    """Get available joke categories with emojis."""
    categories = [
        "dad developer",
        "chuck norris developer",
        "ai philosopher",
        "bug whisperer",
        "old-school coder",
        "frontend philosopher",
        "backend barbarian",
        "cloud comedian",
        "data scientist monk",
        "cybersecurity cynic",
        "devops therapist",
        "agentic ai joker",
        "prompt poet",
        "math & logic nerd",
        "general",
    ]

    return categories


def get_category_emojis():
    """Get emoji mapping for categories."""
    emoji_map = {
        "dad developer": "👨‍💻",
        "chuck norris developer": "🥋",
        "ai philosopher": "🧠",
        "bug whisperer": "🐛",
        "old-school coder": "💾",
        "frontend philosopher": "🎨",
        "backend barbarian": "⚙️",
        "cloud comedian": "☁️",
        "data scientist monk": "📊",
        "cybersecurity cynic": "🔒",
        "devops therapist": "🧘‍♂️",
        "agentic ai joker": "🤖",
        "prompt poet": "🪶",
        "math & logic nerd": "🧮",
        "general": "🎯",
    }

    return emoji_map


def get_languages():
    """Get the supported languages."""
    languages = [
        "English",
        "Hindi",
        "Spanish",
        "French",
        "German",
    ]

    return languages
