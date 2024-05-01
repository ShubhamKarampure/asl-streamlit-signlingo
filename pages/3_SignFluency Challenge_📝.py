import streamlit as st
import random
import time
import streamlit_book as stb

if "page" not in st.session_state:
    st.session_state["page"] = "test"

st.session_state["page"] = "test"

st.header("Test your understand 📝")


# Hide Streamlit style
hide_streamlit_style = """
<style>
    .st-emotion-cache-gh2jqd {
        width: 100%;
        padding: 5rem 1rem 10rem;
        max-width: 46rem;
    }
    img {
        border-radius: 1rem;
    }
    div[data-testid="stToolbar"],
    div[data-testid="stDecoration"],
    div[data-testid="stStatusWidget"],
    #MainMenu,
    header,
    footer,
    [data-testid="ScrollToBottomContainer"] {
        visibility: hidden;
        height: 0%;
        position: fixed;
    }
    .video-wrapper {
        background-color: white;
        display: inline-block;
        width: 300px;
        height: 300px;
        overflow: hidden;
        position: relative;
        border-radius: 1rem; /* Add border radius to match the image */
        align-content: center;
    }
    .st-emotion-cache-sh2krr p {
    word-break: break-word;
    margin-bottom: 0px;
    font-size: 20px;
}

    .st-bd {
        font-family: 'Arial', sans-serif; /* Change to your preferred font */
        font-size: 18px; /* Adjust the font size as needed */
        color: #333; /* Adjust the text color */
        margin-bottom: 10px; /* Adjust the bottom margin */
    }

</style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# Define video URLs
video_urls = {
    "A": "https://videos-asl.lingvano.com/9099-480p.mp4",
    "B": "https://videos-asl.lingvano.com/9101-480p.mp4",
    "C": "https://videos-asl.lingvano.com/9102-480p.mp4",
    "D": "https://videos-asl.lingvano.com/9133-480p.mp4",
    "E": "https://videos-asl.lingvano.com/9103-480p.mp4",
    "F": "https://videos-asl.lingvano.com/9131-480p.mp4",
    "G": "https://videos-asl.lingvano.com/9126-480p.mp4",
    "H": "https://videos-asl.lingvano.com/9132-480p.mp4",
    "I": "https://videos-asl.lingvano.com/9115-480p.mp4",
    "J": "https://videos-asl.lingvano.com/9127-480p.mp4",
    "K": "https://videos-asl.lingvano.com/9111-480p.mp4",
    "L": "https://videos-asl.lingvano.com/9134-480p.mp4",
    "M": "https://videos-asl.lingvano.com/9113-480p.mp4",
    "N": "https://videos-asl.lingvano.com/9108-480p.mp4",
    "O": "https://videos-asl.lingvano.com/9109-480p.mp4",
    "P": "https://videos-asl.lingvano.com/9112-480p.mp4",
    "Q": "https://videos-asl.lingvano.com/9124-480p.mp4",
    "R": "https://videos-asl.lingvano.com/9122-480p.mp4",
    "S": "https://videos-asl.lingvano.com/9125-480p.mp4",
    "T": "https://videos-asl.lingvano.com/9120-480p.mp4",
    "U": "https://videos-asl.lingvano.com/9118-480p.mp4",
    "V": "https://videos-asl.lingvano.com/9130-480p.mp4",
    "W": "https://videos-asl.lingvano.com/9116-480p.mp4",
    "X": "https://videos-asl.lingvano.com/9119-480p.mp4",
    "Y": "https://videos-asl.lingvano.com/9128-480p.mp4",
    "Z": "https://videos-asl.lingvano.com/9129-480p.mp4",
}


def question():
    col1, col2 = st.columns([0.5,0.5], gap="medium")
    # Function to update video display
    def update_video(charachter):
        return f"""
        <div class="video-wrapper">
        <video width="350" height="290" autoplay controlsList="nodownload" loop style="transform: scaleX(-1);">
            <source src="{video_urls[charachter]}" type="video/mp4">
            Your browser does not support the video tag.
        </video>
        </div>  
        """

    with col1:
        video_placeholder = st.empty()

    # Initialize session state
    if "correct_option" not in st.session_state:
        st.session_state["correct_option"] = None

    if "options" not in st.session_state:

        st.session_state["options"] = None
    if st.session_state["correct_option"] is not None:
        video_placeholder.markdown(
            update_video(st.session_state["correct_option"]), unsafe_allow_html=True
        )

    # Check if the correct option is initialized
    if st.session_state["correct_option"] is None:

        st.session_state["correct_option"] = random.choice(list(video_urls.keys()))

        video_placeholder.markdown(
            update_video(st.session_state["correct_option"]), unsafe_allow_html=True
        )

        correct_option = st.session_state["correct_option"]
        remaining_chars = [char for char in video_urls.keys() if char != correct_option]
        incorrect_options = random.sample(remaining_chars, 3)
        if st.session_state["options"] is None:
            options = [correct_option] + incorrect_options
            random.shuffle(options)
            st.session_state["options"] = options 

    with col2:
        checked_answer, correct_answer = stb.single_choice(
            "Select the right option",
            st.session_state["options"],
            st.session_state["options"].index(st.session_state["correct_option"]),
            success = f"Perfect! It's letter {st.session_state['correct_option']}!",
            error="Sadly, that's not true",
            button="Click to check",
        )
       

    # Check the answer
    if checked_answer:
        if correct_answer:
            st.balloons()
            st.session_state["correct_option"] = None
            st.session_state["options"] = None
            video_placeholder.empty()
            time.sleep(2)
            st.experimental_rerun()


question()
