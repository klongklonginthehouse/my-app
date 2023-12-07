import streamlit as st
from datetime import datetime
st.set_page_config(page_title="My Website", page_icon="🚀", layout="wide")

# Function to render the home page
def home():
    st.title("Home Page")
    st.write("Welcome to the home page!")
    st.write("Hi👋 Im Jave Gajelloma, a Computer Engineering student")
    st.image("https://scontent.fmnl8-1.fna.fbcdn.net/v/t39.30808-6/407316958_873382151242463_1150520590098207901_n.jpg?_nc_cat=107&ccb=1-7&_nc_sid=efb6e6&_nc_eui2=AeH8vlH__h-msRZ3fs_VXIdSWzi4og05C7lbOLiiDTkLuVTKOqf_e19NNHuTnZ68nWgmXZh7K5snbOwYTb0R3lhv&_nc_ohc=1FfivB1zafsAX8KQK5O&_nc_ht=scontent.fmnl8-1.fna&oh=00_AfCy-B_MLYxj80kYrPdZOEBMFC4lXCOePfAOZQWaUv2dgw&oe=6576E04F", caption="Hello World", use_column_width=True)
    st.audio("R5tOLaRkUuZH.128.mp3")
# Function to render the about me page
def about_me():
    st.title("About Me Page")
    st.subheader("Likes:")
    st.write("singing 🎤🎶👩‍🎤")
    st.write("dancing 🕺😏💃🍹")
    st.write("Reading Books 📖👀 ")
    st.write("Playing Games 🎮🎮")
    st.write("Watching Movies 👧🧑")
    st.write("Practicing Programming 💻")
    st.write("And Also I like Girls 😏🥴")

# Function to render the contact page
def contact():
    st.title("Contact Page")
    st.subheader("My social media accounts")
    st.write("You can contact me via Email at javegajelloma@gmail.com.")
    st.write("Or via facebook https://www.facebook.com/profile.php?id=100057120588260")
    st.write("Please click me https://boulderbugle.com/magnitude-61-na-lindol-5qyed30w")


def main():
    # Display the current date and time
    current_datetime = datetime.now()
    formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
    st.write(f"Current Date and Time: {formatted_datetime}")

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