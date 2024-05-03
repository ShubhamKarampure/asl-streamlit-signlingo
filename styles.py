def page_setup():
    return """
    <style>

         /* Hide side toolbar buttons*/
        div[data-testid="stToolbar"] {
        visibility: hidden;
        height: 0%;
        position: fixed;
        }

        /* deccrease upper padding */
        .st-emotion-cache-gh2jqd {
            width: 100%;
            padding: 0rem 1rem 10rem;
            max-width: 46rem;
        }

        /* hide header */
        header {
        visibility: hidden;
        height: 0%;
        }

        /* add logo in navbar */
        [data-testid="stSidebar"] {
            background-image: url(https://i.imgur.com/eelyBU4.png);
            background-repeat: no-repeat;
            padding-top: 50px;
            background-position: 50px 50px;
            background-size: 200px 70px; /* or specify the size you want */
        }

        /* placing log out button */
        .st-emotion-cache-hc3laj {
        position: fixed;
        top: 10px;
        right: 32.5px;
        }

        .st-emotion-cache-1u2dcfn {
        display:none;
        }

        [data-testid="stSidebarNavSeparator"]{
        display: none;
        }

       [data-testid="stSidebarNavItems"] {
            max-height: none;
        }
    </style>
    """

def hide_navbar():
    return """
    <style>
        .st-emotion-cache-j7qwjs {
            display:none;
        }
        </style>
    """

def unhide_nav_bar() :
    return """
    <style>
        .st-emotion-cache-j7qwjs {
            display:block;
        }
        </style>
    """
def page_with_webcam_video() :
    return """
        <style>

        img {
        border-radius: 1rem;
        }


        .st-as {
            height:2rem;
            border-radius: 2rem;
        }

         .video-wrapper {
        background-color: white;
        display: inline-block;
        width: 336px;
        height: 336px;
        overflow: hidden;
        position: relative;
        border-radius: 1rem; /* Add border radius to match the image */
        align-content : center
        }

        .letterToFind {
            font-size: 200px;
            color: #ffe090;
            max-height: 20rem;
            text-align : center;
        }

        .progress-text {
            margin-top: 10px;
            text-align: center;
        }

        .progress-container {
            width: 100%;
            height: 2rem; 
            background-color: #683aff;
            border-radius: 5rem;
            position: relative;
        }

            .progress-bar {
        background-color: #ffe090; 
        height: 100%;
        border-radius: 5rem;
        width: 0;
        transition: width 0.3s ease-in-out;
        text-align: center;
        color: #683aff;
        font-size: 20px;
        font-weight: bold;
        line-height: 2rem;
        box-shadow: 10px 0 5px rgba(0, 0, 0, 0.2); /* Adjust values as needed */
    }


    
        </style>
    """
