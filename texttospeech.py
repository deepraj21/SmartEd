import pyttsx3

def text_to_speech(text):
    engine = pyttsx3.init()

    # Set properties (optional)
    # engine.setProperty('rate', 150)  # Speed of speech
    # engine.setProperty('volume', 0.9)  # Volume level (0.0 to 1.0)

    engine.say(text)

    engine.runAndWait()

def read_text_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return None

file_path = input("Enter the path of the text file: ")

text_content = read_text_from_file(file_path)

if text_content:
    text_to_speech(text_content)
