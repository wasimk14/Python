import streamlit as st
import random

# -----------------------------
# WORD LIST WITH HINTS
# -----------------------------
word_list = {
    # Fruits
    "apple": "A red or green fruit that keeps the doctor away.",
    "banana": "Juice do doe! A long yellow fruit, monkeys love it.",
    "grape": "Tiny purple or green fruit, used to make wine.",
    "orange": "A citrus fruit and also a color.",
    "mango": "A tropical fruit, king of fruits in India.",
    "pear": "Green fruit with a soft bottom and firm top.",
    "peach": "A fuzzy fruit with a big pit inside.",
    "plum": "A small, purple stone fruit.",
    "cherry": "Small red fruit, often on cakes.",
    "kiwi": "Brown fuzzy outside, green inside with black seeds.",

    # Animals
    "lion": "Known as the king of the jungle.",
    "tiger": "Striped big cat.",
    "zebra": "Looks like a horse with black and white stripes.",
    "giraffe": "Tum kabhi baithe kya? Tallest animal, has a long neck.",
    "camel": "The ship of the desert.",
    "rabbit": "Small mammal with long ears.",
    "monkey": "Primate that likes to swing on trees.",
    "panda": "Black and white bear from China.",
    "kangaroo": "Australian animal with a pouch.",
    "elephant": "Largest land animal, has a trunk.",

    # Vehicles
    "car": "Has four wheels, common mode of transport.",
    "bus": "Carries many passengers at once.",
    "truck": "Large vehicle used to transport goods.",
    "train": "Runs on tracks.",
    "plane": "Flies in the sky.",
    "boat": "Abbu nahi bithaye Floats on water.",
    "ship": "Big boat for carrying people or cargo.",
    "scooter": "Two-wheeler, lighter than a motorcycle.",
    "bicycle": "Two wheels, powered by pedaling.",
    "rocket": "Flies into space.",

    # Household objects
    "table": "Furniture with legs, used for meals or work.",
    "chair": "Something you sit on.",
    "bed": "You sleep on it.",
    "lamp": "Gives light indoors.",
    "mirror": "Shows your reflection.",
    "clock": "Tells the time.",
    "door": "You open and close it to enter a room.",
    "window": "Opening in a wall to let light in.",
    "couch": "Another word for sofa.",
    "shelf": "Used to store books or things.",

    # Nature
    "river": "Flows from mountains to oceans.",
    "lake": "Still body of fresh water.",
    "ocean": "Covers most of Earth, salty water.",
    "beach": "Sandy place by the sea.",
    "mountain": "High land, often with snow.",
    "forest": "Land covered with trees.",
    "island": "Land surrounded by water.",
    "desert": "Dry land with very little rain.",
    "valley": "Low land between hills.",
    "volcano": "Mountain that erupts with lava.",

    # Colors
    "red": "The color of blood.",
    "blue": "The color of the sky.",
    "green": "The color of grass.",
    "yellow": "The color of the sun.",
    "black": "Opposite of white.",
    "white": "Opposite of black.",
    "pink": "Light red.",
    "purple": "Mix of red and blue.",
    "brown": "Color of soil and chocolate.",
    "grey": "Mix of black and white.",

    # Food
    "bread": "Staple made from flour.",
    "butter": "Made by churning cream.",
    "cheese": "Tum kab khaye! Comes from milk, many varieties.",
    "milk": "White liquid from cows.",
    "egg": "Laid by hens.",
    "rice": "Staple grain in Asia.",
    "noodles": "Long, thin strips of dough.",
    "pizza": "Italian dish with cheese and toppings.",
    "burger": "Bun with patty inside.",
    "salad": "Mixed vegetables, eaten raw.",

    # Professions
    "doctor": "Treats sick people.",
    "teacher": "Works in a school.",
    "farmer": "Grows crops.",
    "chef": "Cooks food professionally.",
    "pilot": "Flies airplanes.",
    "driver": "Operates vehicles.",
    "nurse": "Helps doctors in hospitals.",
    "singer": "Performs songs.",
    "actor": "Performs in movies or plays.",
    "police": "Enforces the law.",

    # Miscellaneous
    "music": "Organized sound, can be sung or played.",
    "dance": "Moving rhythmically to music.",
    "poem": "A piece of writing in verse.",
    "story": "Narrative, can be true or fictional.",
    "book": "Made of pages, full of knowledge.",
    "game": "Played for fun.",
    "toy": "Children play with it.",
    "coin": "Round metal money.",
    "key": "Opens locks.",
    "pen": "Used for writing."
}

# -----------------------------
# INITIALIZE SESSION STATE
# -----------------------------
if "chosen_word" not in st.session_state:
    st.session_state.chosen_word = random.choice(list(word_list.keys()))
    st.session_state.hint = word_list[st.session_state.chosen_word]
    st.session_state.word_length = len(st.session_state.chosen_word)
    st.session_state.lives = len(st.session_state.chosen_word) + 5
    st.session_state.guessed_letters = []
    st.session_state.placeholder = ["_"] * st.session_state.word_length

# -----------------------------
# UI HEADER
# -----------------------------
st.title("🐍 Hangman Game")
st.write("Guess the word, one letter at a time!")

st.subheader("Word to guess:")
st.write(" ".join(st.session_state.placeholder))

st.write(f"Lives left: {st.session_state.lives} ❤️")
if st.session_state.guessed_letters:
    st.write(f"Guessed letters: {', '.join(st.session_state.guessed_letters)}")

# -----------------------------
# INPUT
# -----------------------------
guess = st.text_input("Enter a letter (or type 'hint')").lower()

# -----------------------------
# GAME LOGIC
# -----------------------------
if guess:
    if guess == "hint":
        st.info(f"Hint: {st.session_state.hint}")
    elif guess in st.session_state.guessed_letters:
        st.warning(f"You already guessed '{guess}'. Try something else.")
    else:
        st.session_state.guessed_letters.append(guess)

        if guess in st.session_state.chosen_word:
            for i, letter in enumerate(st.session_state.chosen_word):
                if letter == guess:
                    st.session_state.placeholder[i] = guess
            st.success("Correct guess!")
        else:
            st.session_state.lives -= 1
            st.error(f"Wrong guess! Lives left: {st.session_state.lives}")

    # -----------------------------
    # CHECK WIN / LOSE
    # -----------------------------
    if "_" not in st.session_state.placeholder:
        st.success(f"🎉 My Baby won! The word was {st.session_state.chosen_word.upper()}")
        if st.button("New Game"):
            for key in list(st.session_state.keys()):
                del st.session_state[key]
            st.rerun()

    elif st.session_state.lives == 0:
        st.error(f"💀 Game over! The word was {st.session_state.chosen_word.upper()}")
        if st.button("Play Again"):
            for key in list(st.session_state.keys()):
                del st.session_state[key]
            st.rerun()


