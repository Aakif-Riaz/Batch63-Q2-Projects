from langchain.llms.base import LLM
from google import genai
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
import os

os.environ["GEMINI_API_KEY"] = "AIzaSyB-5EvRtXo60jr8XXGa_5_iwvB6UGg0m_A"

