from langchain.llms import Ollama

# Load local Mistral model via Ollama
llm = Ollama(model="mistral:instruct")

def generate_text(prompt: str) -> str:
    """
    Send a prompt to the Mistral model and get back the generated text.
    """
    try:
        response = llm.invoke(prompt)
        return response
    except Exception as e:
        return f"Error generating response: {e}"
