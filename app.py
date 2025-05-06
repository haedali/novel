import streamlit as st
from backend.chains import generate_world, generate_characters, generate_full_story, continue_story

st.set_page_config(page_title="📝 Unfiltered Story AI", layout="wide")

# --- Session State Setup ---
for key in ["step", "story_idea", "world", "characters", "story", "chat_history"]:
    if key not in st.session_state:
        st.session_state[key] = 1 if key == "step" else ""

# --- App Title ---
st.title("✨ Unfiltered Story Creator with Mistral")

# --- Step 1: Story Idea ---
if st.session_state.step == 1:
    st.subheader("Step 1: Your Story Idea")
    idea = st.text_input("Describe your story idea:", value="", key="idea_input")
    if st.button("Generate World 🌍"):
        if idea.strip():
            with st.spinner("Generating world..."):
                st.session_state.story_idea = idea
                st.session_state.world = generate_world(idea)
                st.session_state.step = 2
        else:
            st.warning("Please enter a story idea.")

# --- Step 2: World Generation ---
elif st.session_state.step == 2:
    st.subheader("Step 2: Generated World 🌍")
    st.text_area("World Description", value=st.session_state.world, height=150)
    if st.button("Generate Characters 👥"):
        with st.spinner("Generating characters..."):
            st.session_state.characters = generate_characters(st.session_state.world)
            st.session_state.step = 3

# --- Step 3: Character Generation ---
elif st.session_state.step == 3:
    st.subheader("Step 3: Characters 👤")
    st.text_area("Characters", value=st.session_state.characters, height=200)
    if st.button("Generate Story 📖"):
        with st.spinner("Generating story..."):
            story = generate_full_story(st.session_state.world, st.session_state.characters)
            st.session_state.story = story
            st.session_state.chat_history = [story]
            st.session_state.step = 4

# --- Step 4: Story and Chat ---
elif st.session_state.step == 4:
    st.subheader("Step 4: Your Story 📖")
    st.text_area("Generated Story", value=st.session_state.story, height=300)

    st.markdown("---")
    st.subheader("🧠 Ask to Continue the Story (Sequel Chat)")
    user_input = st.text_input("What happens next?", key="chat_input")
    if st.button("Continue Story ➡️"):
        if user_input.strip():
            with st.spinner("Continuing story..."):
                new_story = continue_story("\n".join(st.session_state.chat_history), user_input)
                st.session_state.chat_history.append(new_story)
                st.session_state.story += "\n\n" + new_story
                st.experimental_rerun()
        else:
            st.warning("Enter something to continue.")

    st.markdown("### 📝 Full Story So Far")
    st.write(st.session_state.story)
