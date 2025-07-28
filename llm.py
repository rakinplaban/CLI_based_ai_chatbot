from transformers import pipeline, AutoTokenizer, AutoModelForCausalLM
from persona import YUNA_SYSTEM_PROMPT
from dotenv import load_dotenv
import os
import requests

load_dotenv()

print("Loading Yuna's brain... 🧠")

MODEL_NAME = "TinyLlama/TinyLlama-1.1B-Chat-v1.0"
HF_TOKEN = os.getenv("HF_TOKEN")

# API_URL = "https://api-inference.huggingface.co/models/google/flan-t5-small"
# API_URL = "https://api-inference.huggingface.co/models/facebook/blenderbot-1B-distill"

headers = {"Authorization": f"Bearer {HF_TOKEN}"} 

tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForCausalLM.from_pretrained(MODEL_NAME)

chatbot = pipeline(
    "text-generation",
    model=model,
    tokenizer=tokenizer,
    max_new_tokens=200,
    do_sample=True,
    temperature=0.7,
    top_k=50,
    top_p=0.95
)

def ask_yuna(user_input):
    # payload = {
    #     "inputs": f"{YUNA_SYSTEM_PROMPT}\nUser: {user_input}\nYuna:",
    #     "parameters": {"max_new_tokens": 100}
    # }

#     response = requests.post(API_URL, headers=headers, json=payload)
#     output = response.json()

#     try:
#         print("RAW RESPONSE:", response.text)
#         return output[0]["generated_text"]
#     except:
#         return "Oops! Yuna-chan ran into an error 💦"


    prompt = f"{YUNA_SYSTEM_PROMPT}\nUser: {user_input}\nYuna:"
    output = chatbot(prompt)[0]["generated_text"]
    reply = output.split("Yuna:")[-1].strip()
    return reply


# def ask_yuna(user_input):
#     prompt = f"{YUNA_SYSTEM_PROMPT}\nUser: {user_input}\nYuna:"
#     payload = {
#         "inputs": prompt,
#         "parameters": {"max_new_tokens": 100}
#     }

#     response = requests.post(API_URL, headers=headers, json=payload)

#     if response.status_code != 200:
#         print("🔴 Response:", response.status_code, response.text)
#         return "Yuna: Hmm... I can't speak right now 💭 (model might be loading or busy)"

#     try:
#         output = response.json()
#         return "Yuna: " + output[0]["generated_text"]
#     except Exception as e:
#         print("❌ JSON decode error:", e)
#         print("🔵 Raw Response:", response.text)
#        return "Yuna: Whoopsie~ Something went wrong while decoding 💦"
