import streamlit as st
import pyautogui
import time
import random
import os

st.set_page_config(page_title=" Advanced Desktop Assistant", layout="wide")
st.title("AI-Powered Desktop Automation Tool")


st.header("Open Applications")
app_option = st.selectbox("Select an application:", ["Notepad", "Calc", "Chrome", "Notepad++"])
if st.button("Open Application"):
    pyautogui.hotkey("win", "r")
    time.sleep(1)
    pyautogui.write(app_option)  # Works for most apps
    pyautogui.press("enter")
    st.success(f"{app_option} opened successfully!")


st.header("Type and Save a Message")
message = st.text_area("Enter a message:")
if st.button("Type & Save Message in Notepad"):
    if message:
        pyautogui.hotkey("win", "r")
        time.sleep(1)
        pyautogui.write("notepad")
        pyautogui.press("enter")
        time.sleep(1)
        pyautogui.write(message)
        time.sleep(2)
        pyautogui.hotkey("ctrl", "s")
        time.sleep(1)
        pyautogui.write("message.txt")
        pyautogui.press("enter")
        st.success("Message saved successfully!")
    else:
        st.warning("Please enter a message.")

st.header("Take a Screenshot")
if st.button("Capture Screenshot"):
    screenshot = pyautogui.screenshot()
    screenshot.save("screenshot.png")
    st.image("screenshot.png", caption="Screenshot", use_column_width=True)
    st.success("Screenshot saved as 'screenshot.png'!")


st.header("Mouse Auto-Move")
if st.button("Move Mouse Randomly"):
    x, y = random.randint(100, 1000), random.randint(100, 700)
    pyautogui.moveTo(x, y, duration=1)
    st.success(f"Mouse moved to ({x}, {y})")


st.header("Volume Control")
volume_action = st.radio("Select Volume Action", ["Increase", "Decrease"])
if st.button("Adjust Volume"):
    if volume_action == "Increase":
        for _ in range(5):
            pyautogui.press("volumeup")
    else:
        for _ in range(5):
            pyautogui.press("volumedown")
    st.success(f"Volume {volume_action.lower()}d!")


st.header("Automated Typing Speed Test")
if st.button("Start Typing Test in Notepad"):
    pyautogui.hotkey("win", "r")
    time.sleep(1)
    pyautogui.write("notepad")
    pyautogui.press("enter")
    time.sleep(1)
    sentences = [
        "The quick brown fox jumps over the lazy dog.",
        "Python is a powerful programming language.",
        "Artificial intelligence is shaping the future.",
        "Streamlit makes it easy to create web apps.",
        "Automation saves time and effort."
    ]
    sentence = random.choice(sentences)
    pyautogui.write(sentence, interval=0.1)
    st.success("Typing test completed with sentence: " + sentence)

