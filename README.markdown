# ✨ Agentic Unfiltered Storytelling AI: Build Worlds, Characters & Infinite Narratives

Unfiltered Story Generator is an **agentic AI-powered storytelling platform** that empowers users to create unrestricted stories, novels, or sequels step by step — starting from a simple story idea. Built using **Mistral LLM (via Ollama)** and **Streamlit**, it generates imaginative worlds, characters, and plotlines, then allows story continuation through a built-in chat interface. 

Unlike conventional AI tools with heavy safety filters, this project offers **true creative freedom** for writers, game designers, or narrative researchers — while remaining modular and lightweight for local development.

---

## 🔍 Features

- **🧠 Unrestricted Story Generation** using open-source LLMs like Mistral and TinyLLaMA.
- **👁️ Step-by-Step Pipeline**: Story Idea → World Creation → Characters → Full Story.
- **💬 Sequel Chat Interface**: Continue the story as an evolving dialogue.
- **📦 Local-first, Open Design**: No cloud APIs or censorship filters.
- **📸 Screenshots Output** for each stage of the generation process.

---

## ⚙️ Tech Stack

| Layer              | Tool / Library                     |
|--------------------|------------------------------------|
| 💡 LLM Backend      | [Ollama](https://ollama.com/) with `mistral:instruct` or `tinyllama` |
| 🧠 Prompt Chaining  | [LangChain](https://www.langchain.com/) |
| 🌐 Frontend         | [Streamlit](https://streamlit.io/) |
| 💾 Local Runtime    | Python 3.10+ with virtual environment |
| 🧰 Dev Environment  | Visual Studio Code (recommended)  |

---

## 📷 Output Screenshots

| Description           | Preview |
|-----------------------|---------|
| 🌍 World Description  | ![](screenshots/world_description.png) |
| 👤 Character Design   | ![](screenshots/character_description.png) |
| 📖 Generated Story    | ![](screenshots/generated_story.png) |
| ➕ Sequel Generator   | ![](screenshots/sequel_generator.png) |
| 🧾 Full Tracker View  | ![](screenshots/full_story_tracker.png) |
| 🏠 Home Page          | ![](screenshots/home_page.png) |

---

## 🛠️ Installation & Setup

### 1. Clone the repository
```bash
git clone https://github.com/your-username/unfiltered_story_gen.git
cd unfiltered_story_gen
```

### 2. Set up a virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Pull a model with Ollama
Choose based on your PC specs:

**💪 For better output (requires ~6–8GB RAM):**
```bash
ollama pull mistral:instruct
```

**🖥️ For low-end machines (works on 4GB RAM):**
```bash
ollama pull tinyllama
```

Update your backend file accordingly:

```python
# backend/llm_engine.py
llm = Ollama(model="tinyllama")  # or "mistral:instruct"
```

### 5. Run the app
```bash
streamlit run app.py
```

---

## 🚀 Use Cases
- ✍️ Writers looking for AI-enhanced creativity
- 🎮 Game developers needing lore & character backstories
- 📚 Novelists experimenting with AI-first storytelling
- 🧪 AI researchers studying unfiltered agentic generation

---

## 🧠 Why Is This Unique?
- **No Censorship Filters**: Unlike OpenAI or Gemini, this app uses open-source LLMs without built-in restrictions.
- **Agentic Control**: The system routes through prompt chaining steps with conditional logic.
- **Modular & Extendable**: Each part (world, characters, continuation) is a separate chain for easy control.
- **Runs Offline**: With Ollama, no external APIs or internet are needed after setup.
- **Lightweight Mode**: TinyLLaMA support makes it suitable for older or low-RAM systems.

---

## 📌 Folder Structure
```
unfiltered_story_gen/
│
├── app.py                    # Streamlit UI
├── requirements.txt
├── backend/
│   ├── llm_engine.py         # Model connector (Ollama)
│   └── chains.py             # Prompt chaining logic
└── screenshots/              # Generated screenshots
```

---

## ❤️ Credits
- Mistral for their open-weight LLMs
- Ollama for easy local LLM integration
- Streamlit for the web UI
- LangChain for building chainable logic

---

## 📄 License
This project is open-source and licensed under the MIT License.

---

## 🚧 Future Improvements
- Add user login & story history saving
- Enable voice-based story prompting
- Add image generation (Stable Diffusion) for characters & scenes