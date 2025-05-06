from backend.llm_engine import generate_text

def generate_world(story_idea: str) -> str:
    prompt = (
        f"Create a fictional world setting (3-4 sentences) for this story idea: '{story_idea}'. "
        "Keep it creative and concise."
    )
    return generate_text(prompt)

def generate_characters(world_description: str) -> str:
    prompt = (
        f"Based on this world: '{world_description}', create 2-3 main characters with names, roles, and one key trait each."
    )
    return generate_text(prompt)

def generate_full_story(world: str, characters: str) -> str:
    prompt = (
        f"Write an engaging 2-paragraph story based on the world below and these characters:\n\n"
        f"World: {world}\n\nCharacters: {characters}\n\n"
        "Start the story naturally with vivid language."
    )
    return generate_text(prompt)

def continue_story(previous_story: str, user_prompt: str) -> str:
    prompt = (
        f"Here is the current story:\n\n{previous_story}\n\n"
        f"Now continue it based on this user input: '{user_prompt}'. Keep the tone and characters consistent."
    )
    return generate_text(prompt)
