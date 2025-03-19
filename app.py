import os
import streamlit as st
from dotenv import load_dotenv
from phi.agent import Agent
from phi.tools.duckduckgo import DuckDuckGo
from phi.tools.yfinance import YFinanceTools
from phi.model.groq import Groq

# Load environment variables
load_dotenv()
os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")

# Define agents
web_agent = Agent(
    name="Web Agent",
    role="Search the web for information",
    model=Groq(id="llama-3.3-70b-versatile"),
    tools=[DuckDuckGo()],
    instructions=["Always include sources"],
    show_tool_calls=True,
    markdown=True,
)

finance_agent = Agent(
    name="Finance Agent",
    role="Get financial data",
    model=Groq(id="llama-3.3-70b-versatile"),
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, company_info=True)],
    instructions=["Use tables to display data"],
    show_tool_calls=True,
    markdown=True,
)

agent_team = Agent(
    model=Groq(id="llama-3.3-70b-versatile"),
    team=[web_agent, finance_agent],
    instructions=["Always include sources", "Use tables to display data"],
    show_tool_calls=True,
    markdown=True,
)

# Streamlit UI
st.set_page_config(page_title="Finance Assistant", page_icon="💰", layout="wide")
st.title("💰 Finance Assistant")
st.markdown("### Get real-time financial insights and web-based information")

# Sidebar for navigation
with st.sidebar:
    st.header("Navigation")
    page = st.radio("Select an option:", ["Ask a Question", "About"], index=0)
    st.markdown("---")
    st.markdown("**Built with Streamlit and AI-powered Agents**")

if page == "Ask a Question":
    st.write("Enter your financial or web-related query below:")
    user_query = st.text_input("Your question:", "")

    if user_query:
        with st.spinner("Fetching response..."):
            response = agent_team.run(user_query)
            clean_response = response.content if hasattr(response, "content") else str(response)
        
        st.markdown("### Response:")
        st.markdown(clean_response, unsafe_allow_html=True)

elif page == "About":
    st.subheader("About Finance Assistant")
    st.write("Finance Assistant is an AI-powered tool designed to provide real-time financial insights and web-based information. It utilizes cutting-edge AI models and finance APIs to bring you accurate and useful data.")




# Normal code to use in terminal
# import os
# from dotenv import load_dotenv
# from phi.agent import Agent
# from phi.tools.duckduckgo import DuckDuckGo
# from phi.tools.yfinance import YFinanceTools
# from phi.model.nvidia import Nvidia
# from phi.model.groq import Groq
# load_dotenv()

# os.environ["NVIDIA_API_KEY"]=os.getenv("NVIDIA_API_KEY")
# groq = os.getenv("GROQ_API_KEY")

# web_agent = Agent(
#     name="Web Agent",
#     role="Search the web for information",
#     model=Groq(id="llama-3.3-70b-versatile"),
#     # model=Nvidia(id="meta/llama-3.3-70b-instruct"),
#     tools=[DuckDuckGo()],
#     instructions=["Always include sources"],
#     show_tool_calls=True,
#     markdown=True,
# )

# finance_agent = Agent(
#     name="Finance Agent",
#     role="Get financial data",
#     model=Groq(id="llama-3.3-70b-versatile"),
#     # model=Nvidia(id="meta/llama-3.3-70b-instruct"),
#     tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, company_info=True)],
#     instructions=["Use tables to display data"],
#     show_tool_calls=True,
#     markdown=True,
# )

# agent_team = Agent(
#     model=Groq(id="llama-3.3-70b-versatile"),
#     # model=Nvidia(id="meta/llama-3.3-70b-instruct"),
#     team=[web_agent, finance_agent],
#     instructions=["Always include sources", "Use tables to display data"],
#     show_tool_calls=True,
#     markdown=True,
# )
# inpt = input("Ask anything about Finance here : ")
# agent_team.print_response(inpt, stream=True)
