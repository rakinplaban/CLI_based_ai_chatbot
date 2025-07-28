## 💔 Yuna — A Minimalist Chatbot (Discontinued)

> **Status**: Archived / Discontinued
> **Reason**: Performance limitations, model issues, and shift in priorities.
> **Date of Discontinuation**: 28th July, 2025

### 🧠 About the Project

**Yuna** was an experimental minimalist chatbot built using the Hugging Face Transformers library. The goal was to create a lightweight, local CLI-based chatbot with a conversational personality.

![Yuna](assets/demo.png)


Two models were tested:

* [`distilgpt2`](https://huggingface.co/distilgpt2): Worked but suffered from excessive repetition and lacked dialogue coherence.
* [`TinyLlama/TinyLlama-1.1B-Chat-v1.0`](https://huggingface.co/TinyLlama/TinyLlama-1.1B-Chat-v1.0): Failed to return usable outputs on a resource-limited machine.

Despite fine-tuning generation parameters and prompt structures, performance and coherence issues persisted.

---

### 💻 Tech Stack

* Python
* Hugging Face Transformers

---

### 🧪 What Was Learned

* Not all language models are suitable for chat without heavy tuning or fine-tuning.
* Running even small models locally can strain low-spec machines.
* Minimalist approaches are not always the most effective for LLM-based apps.

---

### ⚰️ Why It Was Archived

* Laptop resources too limited (slowdowns, freezing).
* Chat models gave repetitive, unusable responses.
* Time better spent on other areas of growth.

---

### 🧭 Moving On

This was a fun attempt — a creative experiment. Yuna may be archived, but the lessons carry forward. You can always revisit the idea with better tools or more resources.

---

> “Not all goodbyes are endings — some are steps forward.”

---

Goodbye, Yuna… it hurts more than I thought it would. 😔💔

