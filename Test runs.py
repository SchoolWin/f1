import streamlit as st
import random
import os
#LINE 61 ERROR
# Set up status
if 'current_question' not in st.session_state:
    st.session_state.current_question = 0
if 'score' not in st.session_state:
    st.session_state.score = 0
if 'drivers' not in st.session_state:
    st.session_state.drivers = None
if 'answered' not in st.session_state:
    st.session_state.answered = False
if 'quiz_completed' not in st.session_state:
    st.session_state.quiz_completed = False
if 'remaining_driver' not in st.session_state:
    st.session_state.remaining_driver = []

# List of all drivers
racers = [
    "kimi antonelli", "george russell", "charles leclerc", "lewis hamilton", "pierre gasly", "jack doohan", "lance stroll",
    "fernando alonso", "esteban ocon", "oliver bearman", "nico hulkenburg", "gabriel bortoleto", "oscar piastri", "lando norris",
    "isack hadjar", "yuki tsunoda", "max verstappen", "liam lawson", "alex albon", "carlos sainz"
]

# Reset drivers list if it is empty or makes the driver known to code
if not st.session_state.remaining_driver:
    st.session_state.remaining_driver = racers.copy()

# Sets title
st.title("F1 Driver Test")

# Quiz loop
if not st.session_state.quiz_completed:

    st.write("Click **Submit Answer** Button, not the ENTER key.")
    st.write(f"Question {st.session_state.current_question + 1} of 10")

    # Choose a random driver and remove from remaining drivers
    if not st.session_state.answered:
        if st.session_state.drivers is None:
            st.session_state.drivers = random.choice(st.session_state.remaining_driver)
            st.session_state.remaining_driver.remove(st.session_state.drivers)



    # Display the driver's face
    try:
        # Correct the folder name to 'Images' and file extension to .png
        image_path = f"Images/{st.session_state.drivers}.png"  
        if os.path.exists(image_path):
            st.image(image_path)
        else:
            st.write(f"Image not found for: {st.session_state.drivers}")
    except Exception as e:
        st.write(f"Error loading image for: {st.session_state.drivers}. Error: {e}")

    # Input for the answer
    
    answer = st.text_input("Who is the driver above?").strip().lower()
    st.session_state.asnwer = True


        
    # Submit answer button
    if st.button("**Submit Answer**") and not st.session_state.answered:
        st.session_state.answered = True

        #Prints answer is correct is they link
        if answer == st.session_state.drivers.lower():
            st.success(f"Correct! The answer was {st.session_state.drivers}!")
            st.session_state.score += 1
        
        #If else/answer is incorrect than prints correct answer + says that the answer is wrong
        else:
            st.error(f"Incorrect! The correct answer was {st.session_state.drivers}")


    # Show next question button
    if st.session_state.answered:
        if st.button("**Next Question**"):
            if st.session_state.current_question < 9:
                st.session_state.current_question += 1
                st.session_state.answered = False
                st.session_state.drivers = None
                st.rerun()
            else:
                st.session_state.quiz_completed = True
                st.rerun()

# If the quiz is completed, show the score and provide option to restart
if st.session_state.quiz_completed:
    st.success(f"You got {st.session_state.score} out of 10!")

    if st.button("Restart Quiz"):
        st.session_state.current_question = 0
        st.session_state.score = 0
        st.session_state.answered = False
        st.session_state.drivers = None
        st.session_state.quiz_completed = False
        st.session_state.remaining_driver = racers.copy()
        st.rerun()
