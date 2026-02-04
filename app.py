import streamlit as st
from engine import process_meeting
import os

st.set_page_config(page_title="AI MoM Generator", layout="wide")

st.title("🎙️ AI Meeting Minutes Generator")
st.write("Upload meeting audio and get professional MoM in seconds.")

uploaded_file = st.file_uploader("Upload Audio (mp3, wav, m4a)", type=["mp3", "wav", "m4a"])

if uploaded_file is not None:
    # Save file temporarily
    with open("temp_audio.mp3", "wb") as f:
        f.write(uploaded_file.getbuffer())
    
    if st.button("Generate MoM"):
        with st.spinner("Processing... Isme thoda time lag sakta hai."):
            transcript, _ = process_meeting("temp_audio.mp3")
            st.session_state.transcript = transcript
    
    # Show transcript for editing
    if "transcript" in st.session_state:
        st.subheader("Edit Transcript")
        edited_transcript = st.text_area("Raw Text", st.session_state.transcript, height=300, key="transcript_editor")
        
        if st.button("Generate MoM from Edited Transcript"):
            with st.spinner("Generating MoM..."):
                from engine import generate_mom_from_text
                mom = generate_mom_from_text(edited_transcript)
                
                col1, col2 = st.columns(2)
                with col1:
                    st.subheader("Edited Transcript")
                    st.text_area("Final Text", edited_transcript, height=300, disabled=True)
                
                with col2:
                    st.subheader("Minutes of Meeting")
                    st.markdown(mom)
                    st.download_button("Download MoM", mom, file_name="MoM.md")