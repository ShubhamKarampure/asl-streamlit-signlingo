import streamlit as st
from urls import video_urls


def progress_bar(prog):
    if(prog > 0):
        return f"""
            <div class="progress-container">
                <div class="progress-bar" style="width: {prog}%;">{prog}%</div>
            </div>
            """
    else:
        return f"""
            <div class="progress-container">
                <div class="progress-bar" style="width: {prog}%;"></div>
            </div>
            """


def update_video(charachter):
    if st.session_state["page"]=="learnpage":
        return f"""
        <div class="video-wrapper">
        <div class="text-overlay">
            {charachter}
        </div>
        <video width="350" height="290" autoplay controlsList="nodownload" loop style="transform: scale(1.75);">
            <source src="{video_urls[charachter]}" type="video/mp4">
            Your browser does not support the video tag.
        </video>
        </div> 
        """
    else:
        return f"""
        <div class="video-wrapper">
        <video width="350" height="290" autoplay controlsList="nodownload" loop style="transform: scale(1.75);">
            <source src="{video_urls[charachter]}" type="video/mp4">
            Your browser does not support the video tag.
        </video>
        </div>
        """


def detected_word(WORD, detected_index):
    markdown_str = f'<div style="font-weight: bold; text-align: center; font-size: 50px;">'
    # Loop through each letter in the word
    for i, letter in enumerate(WORD):
        # Check if the current letter index is less than or equal to the detected index
        if i <= detected_index:
            # If yes, add the letter in green color
            markdown_str += f'<span style="color:#ffe090;">{letter}</span>'
        else:
            # If no, add the letter in white color
            markdown_str += f'<span style="color:white;">{letter}</span>'
    markdown_str += "</div>"
    return markdown_str
