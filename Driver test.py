import streamlit as st
import random
import os

# to start venv = .\.venv\bin\Activate.ps1

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
def clear_text(): 
  st.session_state["text"] = ''  

# List of all drivers
racers = [
 
    "Kimi Antonelli", "George Russell", "Charles Leclerc", "Lewis Hamilton", "Pierre Gasly", "Jack Doohan", "Lance Stroll",
    "Fernando Alonso", "Esteban Ocon", "Oliver Bearman", "Nico Hulkenberg", "Gabriel Bortoleto", "Oscar Piastri", "Lando Norris",
    "Isack Hadjar", "Yuki Tsunoda", "Max Verstappen", "Liam Lawson", "Alexander Albon", "Carlos Sainz"
]

# Reset drivers list if it is empty or makes the driver known to code
if not st.session_state.remaining_driver:
    st.session_state.remaining_driver = racers.copy()

# Sets title
st.title("F1 Driver Test")


# Quiz loop
if not st.session_state.quiz_completed:

    #Gives Slight Instructions
    st.write("Click **Submit Answer** Button, not the ENTER key.")
    st.write("Clicking the **Submit Answer** Button for a second time, the answer will not change, but will get rid of the correct or incorrect message.")
    
    #Shows question number
    st.write(f"Question {st.session_state.current_question + 1} of 10")

    # Choose a random driver and remove from remaining drivers
    if not st.session_state.answered:
        if st.session_state.drivers is None:
            st.session_state.drivers = random.choice(st.session_state.remaining_driver)
            st.session_state.remaining_driver.remove(st.session_state.drivers)

    # Display the driver's face
    try:
        image_path = f"images/{st.session_state.drivers}.png"
        if os.path.exists(image_path):
            st.image(image_path)
        else:
            st.write(f"Image not found for: {st.session_state.drivers}")
    except Exception as e:
        st.write(f"Error loading image for: {st.session_state.drivers}. Error: {e}")

    
    # Input for the answer
    answer = st.text_input("Who is the driver above? (Same name as the F1 Website)", key="text").strip().lower()
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


    # Show next question button and after click goes to next question and clears it
    if st.session_state.answered:
        if st.button("**Next Question**", on_click=clear_text):
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

    #Restart button for quiz to reset and resets all variables
    if st.button("Restart Quiz"):
        st.session_state.current_question = 0
        st.session_state.score = 0
        st.session_state.answered = False
        st.session_state.drivers = None
        st.session_state.quiz_completed = False
        st.session_state.remaining_driver = racers.copy()
        st.rerun()
