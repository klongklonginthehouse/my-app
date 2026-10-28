import streamlit as st
from datetime import datetime
st.set_page_config(page_title="My Website", page_icon="🚀", layout="wide")

def home():
    st.title("Home Page")
    st.write("Welcome to the home page!")
    st.write("Hi👋 Im Jave Gajelloma, a Computer Engineering student")
    
    st.image("https://scontent.fdvo2-2.fna.fbcdn.net/v/t39.30808-6/407316958_873382151242463_1150520590098207901_n.jpg?_nc_cat=107&ccb=1-7&_nc_sid=efb6e6&_nc_eui2=AeH8vlH__h-msRZ3fs_VXIdSWzi4og05C7lbOLiiDTkLuVTKOqf_e19NNHuTnZ68nWgmXZh7K5snbOwYTb0R3lhv&_nc_ohc=B8yCt84wjXQAX-aM7CI&_nc_ht=scontent.fdvo2-2.fna&oh=00_AfAlsReEoS0Ry3LYsuFLQHatPpWCIcoq1ubeEEjHI1XX3g&oe=6570F18F", caption="Hello World", use_column_width=True)
    

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


def contact():
    st.title("Contact Page")
    st.subheader("My social media accounts")
    st.write("You can contact me via Email at javegajelloma@gmail.com.")
    st.write("Or via facebook https://www.facebook.com/profile.php?id=100057120588260")
    st.write("Please click me https://boulderbugle.com/magnitude-61-na-lindol-5qyed30w")


def main():
 
    current_datetime = datetime.now()
    formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
    st.write(f"Current Date and Time: {formatted_datetime}")

   
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Select a page", ["Home", "About Me", "Contact"])

  
    if page == "Home":
        home()
    elif page == "About Me":
        about_me()
    elif page == "Contact":
        contact()


if __name__ == "__main__":
    main()
