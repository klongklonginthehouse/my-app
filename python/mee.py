import streamlit as st
from datetime import datetime
st.set_page_config(page_title="My Website", page_icon="🚀", layout="wide")

def home():
    st.title("My Home Page")
    st.write("Hello Blog welcome to my Life!")
    st.write("Hi👋 I'm Jave Gajelloma, a BSICT Student From SNSU Main Campus")
    
    st.image("https://scontent.fcgy2-1.fna.fbcdn.net/v/t39.30808-6/458980880_1049790273601649_7547396865509863730_n.jpg?_nc_cat=107&ccb=1-7&_nc_sid=6ee11a&_nc_eui2=AeEDy0Y5XKTab04M7kklw5vgqKWFpow9wUaopYWmjD3BRroVX2nZzvqP3Mqj6GymGx5T35RSpiP4n7V4hB93C5S6&_nc_ohc=CMBu__Evl4kQ7kNvgF5kBN6&_nc_ht=scontent.fcgy2-1.fna&_nc_gid=AvAg7JJDD1kwNmK6nQriSJP&oh=00_AYAbySnst8BxHby2KIRpeDRu6bs36sYIcGQ8Zkw0ca5ayA&oe=66F950BF", caption="Hello World", use_column_width=True)
    
def about_me():
    st.title("About Me Page")
    st.subheader("Likes:")
    st.write("singing 🎤🎶👩‍🎤")
    st.write("dancing 🕺😏💃🍹")
    st.write("Reading Books 📖👀 ")
    st.write("Playing Games 🎮🎮")
    st.write("Watching Movies 👧🧑")
    st.write("Practicing Coding 💻")
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
