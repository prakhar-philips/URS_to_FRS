import streamlit as st
import requests

st.title("URS to FRS Generator")

st.write("Upload your URS PDF and enter a project description to generate a Functional Requirements Specification (FRS) PDF.")

urs_file = st.file_uploader("Upload URS PDF", type=["pdf"])
user_prompt = st.text_area("Project Description / Prompt")

if st.button("Generate FRS"):
    if urs_file and user_prompt:
        with st.spinner("Generating FRS PDF..."):
            files = {"urs_file": (urs_file.name, urs_file, "application/pdf")}
            data = {"user_prompt": user_prompt}
            try:
                response = requests.post(
                    "http://localhost:8000/api/frs/generate",
                    files=files,
                    data=data
                )
                if response.status_code == 200:
                    st.success("FRS PDF generated!")
                    st.download_button(
                        label="Download FRS PDF",
                        data=response.content,
                        file_name="Generated_FRS.pdf",
                        mime="application/pdf"
                    )
                else:
                    st.error(f"Error: {response.status_code} - {response.text}")
            except Exception as e:
                st.error(f"Request failed: {e}")
    else:
        st.warning("Please upload a URS PDF and enter a project description.") 