import os

LLM = 'llama-3.1-8b-instant'

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

CONFIG_DIR = os.path.join(ROOT_DIR, "config")
PROMPT_CONFIG_FILE_DIR = os.path.join(CONFIG_DIR, "prompt_config.yaml")