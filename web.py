
import streamlit as st

# App Title
st.title("My Biography App")

# Sidebar for user input
st.sidebar.header("Edit Your Information")
name = st.sidebar.text_input("Name", "Honey Jane D. Elegino")
age = st.sidebar.number_input("Age", min_value=0, max_value=120, value=18)
gender = st.sidebar.selectbox("Gender", ["Female", "Male", "Other"], index=0)
birthday = st.sidebar.text_input("Birthday", "March 1, 2006")
course = st.sidebar.text_input("Course", "BSCpE")
university = st.sidebar.text_input("University", "Surigao Del Norte State University")
country = st.sidebar.text_input("Country", "Philippines")
nationality = st.sidebar.text_input("Nationality", "Filipino")
profile_picture = st.sidebar.file_uploader("Upload Your Profile Picture", type=["jpg", "png", "jpeg"])

# Sidebar for additional sections
st.sidebar.header("Additional Information")
about_me = st.sidebar.text_area(
    "About Me", 
    """Hi! I am a first-year BSCpE student with a passion for learning and exploring technology. 
I chose computer engineering because I am fascinated by how technology can solve real-world problems.  
Although it wasn't entirely my choice, I'm excited to embrace new challenges and learn as much as I can."""
)
hobbies = st.sidebar.text_area("Hobbies", "Playing Mobile Legends, Watching Anime, Discovering Music")
favorite_quotes = st.sidebar.text_area(
    "Favorite Quotes", 
    """- "Success is not final, failure is not fatal: It is the courage to continue that counts."
- "You will face many defeats in life, but never let yourself be defeated."
- "When we are no longer able to change the situation, we are challenged to change ourselves."
"""
)
motto = st.sidebar.text_input("Motto", "Strive for progress, not perfection.")
future_plan = st.sidebar.text_area(
    "Future Plans", 
    """- Explore machine learning and artificial intelligence.
- Master programming languages like Python and C++.
- Become an engineer who contributes to open-source projects.
- Build innovative solutions that help others."""
)

# Main content display
st.write("Hi there, and welcome!")
st.markdown(f"### Basic Information")
st.markdown(f"Name: {name}")
st.markdown(f"Age: {age}")
st.markdown(f"Gender: {gender}")
st.markdown(f"Birthday: {birthday}")
st.markdown(f"Course: {course}")
st.markdown(f"University: {university}")
st.markdown(f"Country: {country}")
st.markdown(f"Nationality: {nationality}")

# Display profile picture
if profile_picture is not None:
    st.image(profile_picture, caption="Your Profile Picture", width=200)
else:
    st.markdown("(No profile picture uploaded yet.)")

st.markdown("### About Me")
st.write(about_me)

st.markdown("### Hobbies")
st.write(hobbies)

st.markdown("### My Favorite Quotes")
st.write(favorite_quotes)

st.markdown("### My Motto")
st.write(motto)

st.markdown("### My Future Plans")
st.write(future_plan)

st.markdown("---")
st.write("Thank you for visiting my biography app!")