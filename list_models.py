import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

print("Available Models:")
for model in genai.list_models():
    print(f"  - {model.name}")
    print(f"    Display name: {model.display_name}")
    print(f"    Supported methods: {model.supported_generation_methods}")
    print()
