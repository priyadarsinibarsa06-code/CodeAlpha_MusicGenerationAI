import streamlit as st
from music21 import stream, note
import random

st.set_page_config(page_title="Music Generation AI")

st.title("🎵 Music Generation with AI")

if st.button("Generate Music"):

    melody = stream.Stream()

    notes = ['C4', 'D4', 'E4', 'F4', 'G4', 'A4', 'B4']

    for i in range(20):
        random_note = random.choice(notes)
        melody.append(note.Note(random_note))

    melody.write('midi', fp='generated_music.mid')

    st.success("Music Generated Successfully!")

    with open("generated_music.mid", "rb") as file:
        st.download_button(
            label="Download Music File",
            data=file,
            file_name="generated_music.mid",
            mime="audio/midi"
        )