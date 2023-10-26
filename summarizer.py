import google.generativeai as palm
import os
import time

palm.configure(api_key='AIzaSyB5v4JcdsO0gLlgPhSkPD6CZYefcWY7aHk')

# Use the palm.list_models function to find available models:
models = [m for m in palm.list_models() if 'generateText' in m.supported_generation_methods]
model = models[0].name

def get_completion(prompt):
    completion = palm.generate_text(model=model,
                                    prompt=prompt,
                                    temperature=0,
                                    max_output_tokens=200)
    return completion.result

summary = ""

# Read the transcript from the file
with open("transcript.txt", "r") as file:
    text = file.read().strip().split("\n")
 
print("Summary:")

for i in range(len(text)):
    prompt = f"""
    Your task is to act as a Text Summariser.
    I'll give you text.
    And your job is to summarise the whole text in less than 100 words.
    Don't be conversational. I need a plain 100 word answer.
    Text is shared below, delimited with triple backticks:

```{text[i]}```
    """
    try:
        response = get_completion(prompt)
    except:
        response = get_completion(prompt)
   
    print(response)
    # summary = f"{summary} {response}\n\n"
    time.sleep(19) 
