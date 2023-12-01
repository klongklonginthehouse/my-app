import streamlit as st

# Function to render the home page
def home():
    st.title("Home Page")
    st.write("Welcome to the home page!")
    st.write("I am Jave Gajelloma, a computer engineering student")
    
    st.image("https://scontent.fmnl8-3.fna.fbcdn.net/v/t39.30808-6/322363851_710963113799578_5807797078688369385_n.jpg?_nc_cat=104&ccb=1-7&_nc_sid=9c7eae&_nc_eui2=AeEJ0VL96Q-bRzWImGPK6bj5QDb0v_shY-dANvS_-yFj5xo84EMk6vtCzPwhQ-bWXk_FmOSSh4dTEDBad1-blDwf&_nc_ohc=HvwEXRWd--AAX9qrvTT&_nc_ht=scontent.fmnl8-3.fna&oh=00_AfAZczNYnVzac_f3pz34tCMlWsNsSMbE7zV_y4UNTjuOlA&oe=656F1B45", caption="Your Image Caption", use_column_width=True)
    st.audio("audio/never-gonna-give-you-up-made-with-Voicemod-technology.mp3", format="audio/mp3", start_time=0)

# Function to render the about me page
def about_me():
    st.title("About Me Page")
    st.write("This is the about me.")

# Function to render the contact page
def contact():
    st.title("Contact Page")
    st.write("You can contact me via Email at javegajelloma@gmail.com.")

# Main function to handle page navigation
def main():
    # Create a sidebar for page navigation
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Select a page", ["Home", "About Me", "Contact"])

    # Render the selected page
    if page == "Home":
        home()
    elif page == "About Me":
        about_me()
    elif page == "Contact":
        contact()

# Run the app
if __name__ == "__main__":
    main()