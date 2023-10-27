from youtube_transcript_api import YouTubeTranscriptApi
import google.generativeai as palm
import os
import time
from flask_sqlalchemy import SQLAlchemy
from flask import render_template, request, redirect, url_for, session
from flask import Flask

app = Flask(__name__)
app.secret_key = 'MYSECRETKEY'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

def get_video_transcript(video_id):
    try:
        transcript_list = YouTubeTranscriptApi.get_transcript(video_id)
        transcript = ' '.join([line['text'] for line in transcript_list])
        return transcript
    except Exception as e:
        print(f"Error: {str(e)}")
        return None



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



class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

def create_tables():
    with app.app_context():
        db.create_all()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User(username=username, password=password)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username, password=password).first()
        if user:
            session['user_id'] = user.id
            return redirect(url_for('dashboard'))
    return render_template('login.html')

@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    response=""
    if 'user_id' in session:
        user = User.query.get(session['user_id'])  # Retrieve the user from the database
        if user:
            username = user.username
            if request.method == 'POST':
                video_url = request.form['video_url']
                video_id = video_url.split("=")[-1]
                transcript = get_video_transcript(video_id)

                if transcript:
                    with open('transcript.txt', 'w') as f:
                        f.write(transcript)
                        print("Transcript saved to transcript.txt")
                else:
                    print("Failed to retrieve the transcript.")
                    
                # response = ""

                # Read the transcript from the file
                with open("transcript.txt", "r") as file:
                    text = file.read().strip().split("\n")
                
                # print("Summary:")

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
                
                    # print(response)
                    # summary = f"{summary} {response}\n\n"
                    time.sleep(19) 

            return render_template('dashboard.html', username=username,response=response)
    
    return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session.pop('user_id', None)  # Remove the user_id from the session
    return redirect(url_for('index'))  

if __name__ == '__main__':
    create_tables()
    app.run(debug=True)
