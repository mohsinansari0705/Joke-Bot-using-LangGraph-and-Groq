from joke_bot import generate_joke_with_critic
import streamlit as st
import requests
from utils import (
    get_categories, 
    get_category_emojis, 
    get_languages
)


# Set Streamlit page configuration
st.set_page_config(
    page_title="Joke Bot using LangGraph and Groq",
    page_icon="🤡",
    layout="wide",
)

# Initialize session state variables
if "bot_started" not in st.session_state:
    st.session_state["bot_started"] = False
if "latest_joke" not in st.session_state:
    st.session_state["latest_joke"] = None
if "joke_count" not in st.session_state:
    st.session_state["joke_count"] = 0
if 'valid_api_key' not in st.session_state:
    st.session_state['valid_api_key'] = False
if 'api_success_toast' not in st.session_state:
    st.session_state['api_success_toast'] = False
if 'api_text_input' not in st.session_state:
    st.session_state['api_text_input'] = False
if 'api_validation_attempted' not in st.session_state:
    st.session_state['api_validation_attempted'] = False

# Sidebar configuration
with st.sidebar:
    st.header("Groq API Key")
    api_key = st.text_input(
        "Enter your API key:",
        key="api_key",
        type="password",
        disabled=st.session_state.get('api_text_input'),
        placeholder="gsk_..."
    )
    
    # Validate API key button
    if st.button("🔑 Validate API Key", disabled=st.session_state.get('valid_api_key'), use_container_width=True):
        if not api_key or api_key.strip() == "":
            st.error("❌ Please enter an API key first!")
        else:
            with st.spinner("Validating API key..."):
                try:                    
                    # Test the API key by making a simple request
                    url = "https://api.groq.com/openai/v1/models"
                    headers = {
                        "Authorization": f"Bearer {api_key}",
                        "Content-Type": "application/json"
                    }
                    response = requests.get(url, headers=headers, timeout=10)

                    if response.status_code == 200:
                        st.session_state['valid_api_key'] = True
                        st.session_state['api_success_toast'] = True
                        st.session_state['api_text_input'] = True
                        st.session_state['api_validation_attempted'] = True
                        st.rerun()
                    else:
                        st.session_state['valid_api_key'] = False
                        st.session_state['api_validation_attempted'] = True
                        error_msg = "Invalid API key"
                        try:
                            error_data = response.json()
                            if 'error' in error_data:
                                error_msg = error_data['error'].get('message', error_msg)
                        except Exception:
                            pass
                except requests.exceptions.Timeout:
                    st.error("❌ Request timed out. Please check your internet connection and try again.")
                except requests.exceptions.RequestException as e:
                    st.error(f"❌ Network error: {str(e)}")
                except Exception as e:
                    st.error(f"❌ Error validating API key: {str(e)}")
    
    # Show validation status
    if st.session_state.get('valid_api_key'):
        st.success("✅ API Key Validated Successfully!")
    elif st.session_state.get('api_validation_attempted'):
        st.warning("⚠️ API key not validated. Please enter a valid key.")

    "[🔗 Get a Groq API key](https://console.groq.com/keys)"
    "[![GitHub](https://img.shields.io/badge/GitHub-Repository-blue?logo=github)](https://github.com/mohsinansari0705/Joke-Bot-using-LangGraph-and-Groq)"

    st.divider()

    # Joke Categories
    st.header("🎭 Joke Settings")

    categories = get_categories()
    category_emojis = get_category_emojis()

    # Category dropdown with emojis
    category_options = [
        f"{category_emojis.get(cat, '📂')} {cat.title()}" for cat in categories
    ]
    selected_category_display = st.selectbox(
        "Select Joke Category:",
        category_options,
        index=0,
        help="Choose the type of developer jokes you want to generate",
    )

    # Extract actual category name
    selected_category = categories[category_options.index(selected_category_display)]

    # Language selection
    languages = get_languages()

    selected_language = st.selectbox(
        "Select Language:",
        languages,
        index=0,
        help="Choose the language for joke generation",
    )

    # Model temperature settings
    writer_temp = st.slider(
        "Writer Creativity:",
        min_value=0.1,
        max_value=1.0,
        value=0.8,
        step=0.1,
        help="Higher values make jokes more creative but less predictable",
    )

    critic_temp = st.slider(
        "Critic Strictness:",
        min_value=0.1,
        max_value=1.0,
        value=0.3,
        step=0.1,
        help="Lower values make the critic more consistent in evaluation",
    )


# Show toast message after successful validation
if st.session_state.get('api_success_toast'):
    st.toast("✅ API key validated successfully! You can now start using the bot.", icon="✅")
    st.session_state['api_success_toast'] = False


# Main interface
st.title("🤡 Joke Bot using LangGraph & Groq")

# Show description only when bot is not started AND API key is not validated
if not st.session_state["bot_started"] and not st.session_state.get('valid_api_key'):
    st.markdown(
        """
        🎭 **Welcome to the AI-Powered Developer Joke Generator!**
        
        This intelligent joke bot uses LangGraph and Groq AI to create developer-themed jokes:
        
        - 🧑‍🚀 **AI Writer-Critic Loop**: Uses two AI agents - one generates jokes, another evaluates them
        - 🎯 **15+ Categories**: From "Dad Developer" to "Agentic AI Joker" 
        - 🌍 **Multi-language Support**: Generate jokes in 5 different languages
        - 🎨 **Customizable Creativity**: Adjust AI temperature for different humor styles
        - ⚡ **Powered by Groq**: Fast inference with Llama 3.1 models
        
        **How it works:**
        1. Enter your Groq API key in the sidebar (get one free at console.groq.com)
        2. Select your preferred joke category and language
        3. Click "🚀 Start Joke Bot" to begin generating jokes
        4. Use "🎲 Generate New Joke" for more laughs!
        
        Built with ❤️ using [LangGraph](https://www.langgraph.com/) and [Groq](https://groq.com/)
        """
    )

# Control buttons
col1, col2, col3 = st.columns([1, 1, 1])

# Show message if API key is not validated yet
if not st.session_state.get('valid_api_key'):
    st.info("🔑 Please enter and validate your Groq API key in the sidebar to enable the bot controls.")

with col1:
    if st.button(
        "🚀 Start Joke Bot",
        help="Initialize the joke generation system",
        disabled=not st.session_state.get('valid_api_key'),
        use_container_width=True
    ):
        st.session_state["bot_started"] = True
        st.success("🎉 Joke bot initialized successfully!")

with col2:
    if st.button(
        "🎲 Generate New Joke",
        disabled=not st.session_state["bot_started"] or not st.session_state.get('valid_api_key'),
        help="Generate a new joke with current settings",
        use_container_width=True
    ):
        if st.session_state["bot_started"]:
            with st.spinner("🤖 AI agents are crafting your joke..."):
                try:
                    # Generate joke using the writer-critic graph
                    new_joke = generate_joke_with_critic(
                        category=selected_category,
                        language=selected_language,
                        writer_temp=writer_temp,
                        critic_temp=critic_temp,
                        api_key=api_key
                    )

                    # Store the latest joke and increment counter
                    st.session_state["latest_joke"] = new_joke
                    st.session_state["joke_count"] += 1

                    st.success("✨ New joke generated!")

                except Exception as e:
                    st.error(f"❌ Failed to generate joke: {str(e)}")
                    st.info("💡 Make sure your Groq API key is valid and you have API credits available.")

with col3:
    if st.button(
        "🔄 Reset Bot",
        help="Reset the joke bot",
        disabled=not st.session_state.get('valid_api_key'),
        use_container_width=True
    ):
        st.session_state["bot_started"] = False
        st.session_state["latest_joke"] = None
        st.session_state["joke_count"] = 0
        st.success("🔄 Bot reset successfully!")


# Display latest joke
if st.session_state["bot_started"] and st.session_state.get("latest_joke"):
    st.divider()

    # Show the latest joke prominently
    latest_joke = st.session_state["latest_joke"]

    st.markdown(
        f"""
        <div style="
            background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
            padding: 20px;
            border-radius: 10px;
            margin: 10px 0;
            color: white;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        ">
            <h3 style="margin: 0 0 10px 0;">🎯 {latest_joke.category.title()}</h3>
            <p style="font-size: 18px; margin: 0; font-weight: 500;">{latest_joke.text}</p>
            <div style="margin-top: 10px; font-size: 14px; opacity: 0.8;">
                <span>🌍 Language: {selected_language}</span>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


# Show current settings when bot is running
if st.session_state["bot_started"]:
    st.sidebar.divider()
    st.sidebar.subheader("📊 Current Session")
    st.sidebar.write(f"**Jokes Generated:** {st.session_state['joke_count']}")
    st.sidebar.write(f"**Active Category:** {selected_category.title()}")
    st.sidebar.write(f"**Language:** {selected_language}")
