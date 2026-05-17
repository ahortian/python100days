"""
A simple Rock Paper Scissor app using Streamlit.

Run with:
    streamlit run rock_paper_scissor.py
"""

import random

import streamlit as st

OPTIONS = ["rock", "paper", "scissor"]


def init_state():
    if "user_score" not in st.session_state:
        st.session_state.user_score = 0
    if "computer_score" not in st.session_state:
        st.session_state.computer_score = 0
    if "computer_choice" not in st.session_state:
        st.session_state.computer_choice = "?"
    if "user_choice" not in st.session_state:
        st.session_state.user_choice = "?"
    if "result_text" not in st.session_state:
        st.session_state.result_text = "Choose rock, paper, or scissor to start."
    if "n_games" not in st.session_state:
        st.session_state.n_games = 0
    if "n_wins" not in st.session_state:
        st.session_state.n_wins = 0
    if "n_loose" not in st.session_state:
        st.session_state.n_loose = 0
    if "n_ties" not in st.session_state:
        st.session_state.n_ties = 0


def play_round(user_choice: str):
    computer_choice = random.choice(OPTIONS)
    st.session_state.computer_choice = computer_choice
    st.session_state.user_choice = user_choice

    st.session_state.n_games += 1
    if user_choice == computer_choice:
        st.session_state.result_text = "It's a tie!"
        st.session_state.n_ties += 1
    elif (user_choice == "rock" and computer_choice == "scissor") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissor" and computer_choice == "paper"):
        st.session_state.result_text = "You win!"
        st.session_state.user_score += 1
        st.session_state.n_wins += 1
    else:
        st.session_state.result_text = "Computer wins!"
        st.session_state.computer_score += 1
        st.session_state.n_loose += 1


def reset_game():
    st.session_state.user_score = 0
    st.session_state.computer_score = 0
    st.session_state.computer_choice = "?"
    st.session_state.user_choice = "?"
    st.session_state.result_text = "Choose rock, paper, or scissor to start."


init_state()

st.title("Rock Paper Scissor")
st.write("Play against the computer and see the score update instantly.")

col1, col2, col3 = st.columns(3)
with col1:
    if st.button("Rock"):
        play_round("rock")
with col2:
    if st.button("Paper"):
        play_round("paper")
with col3:
    if st.button("Scissor"):
        play_round("scissor")

st.markdown("---")

st.markdown(f"You chose {st.session_state.user_choice}, Computer chose {st.session_state.computer_choice}, {st.session_state.result_text}")

st.write(f"**Score — You:** {st.session_state.user_score}  **Computer:** {st.session_state.computer_score}")
st.write(f"**Games:** {st.session_state.n_games}  **Wins:** {st.session_state.n_wins}  **Loose:** {st.session_state.n_loose}  **Ties:** {st.session_state.n_ties}")

st.button("Reset", on_click=reset_game)
