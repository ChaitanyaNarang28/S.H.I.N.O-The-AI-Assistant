import speech_recognition as sr
import os
import pyttsx3
import webbrowser
import datetime
import google.generativeai as genai
import random
from config import GENAI_API_KEY  # Import the API key from config.py

def ai(prompt):
   
    genai.configure(api_key=GENAI_API_KEY)  # Use the imported API key
    
    text=f"AI response for prompt:{prompt} \n ********************* \n \n"
    generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
    }
    safety_settings = [
    {
        "category": "HARM_CATEGORY_HARASSMENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE",
    },
    {
        "category": "HARM_CATEGORY_HATE_SPEECH",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE",
    },
    {
        "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE",
    },
    {
        "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE",
    },
    ]

    model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    safety_settings=safety_settings,
    generation_config=generation_config,
    )

    chat_session = model.start_chat(
    history=[
        {
        "role": "user",
        "parts": [
            prompt,
        ],
        },
        {
        "role": "model",
        "parts": [
            "## The Rise of the Machines: Exploring the Power and Potential of Artificial Intelligence\n\nArtificial Intelligence (AI) is no longer a futuristic fantasy relegated to science fiction. It has permeated our lives, from the personalized recommendations on our social media feeds to the self-driving cars slowly taking to our roads. This essay will explore the fascinating world of AI, examining its current capabilities, its potential for advancement, and the ethical considerations that accompany its rapid growth.\n\nAt its core, AI encompasses the creation of machines that can perform tasks typically requiring human intelligence, such as learning, problem-solving, and decision-making. This is achieved through algorithms and data sets that train AI systems to recognize patterns, make predictions, and adapt to new information. The field can be broadly categorized into two main types: Narrow AI, designed for specific tasks like playing chess or translating languages, and General AI, which",
        ],
        },
    ]
    )

    response = chat_session.send_message(prompt)
    response_text=response.text
    print(response_text)
    text+=response_text
     
    if not os.path.exists("AI"):
        os.mkdir('AI')
    
    filename_suffix = prompt.split("AI")[1].strip()
    if not filename_suffix:
        filename_suffix = "NoPromptText"  # Default filename if no text after "AI"

    # Constructing the filename
    filename = f"AI/{filename_suffix}.txt"
    print(f"Saving to file: {filename}")

    try:
        with open(filename, "w") as f:
            f.write(text)
            print("File saved successfully")
    except Exception as e:
        print(f"Error saving file: {e}")


chatstr = ""
stop_chat=False
def chat(query):
    global chatstr
    # print(chatstr)
    genai.configure(api_key="AIzaSyB8zuQL1oUKyhTMiY7cKzlMYWG446-mkcw")
    chatstr += f"Chaitanya: {query}\n Shino: "
    generation_config = {
        "temperature": 1,
        "top_p": 0.95,
        "top_k": 64,
        "max_output_tokens": 8192,
        "response_mime_type": "text/plain",
    }
    safety_settings = [
        {
            "category": "HARM_CATEGORY_HARASSMENT",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE",
        },
        {
            "category": "HARM_CATEGORY_HATE_SPEECH",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE",
        },
        {
            "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE",
        },
        {
            "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE",
        },
    ]

    model = genai.GenerativeModel(
        model_name="gemini-1.5-flash",
        safety_settings=safety_settings,
        generation_config=generation_config,
    )

    chat_session = model.start_chat(
        history=[
            {
                "role": "user",
                "parts": [
                    chatstr,
                ],
            },
            {
                "role": "model",
                "parts": [
                    "## The Rise of the Machines: Exploring the Power and Potential of Artificial Intelligence\n\nArtificial Intelligence (AI) is no longer a futuristic fantasy relegated to science fiction. It has permeated our lives, from the personalized recommendations on our social media feeds to the self-driving cars slowly taking to our roads. This essay will explore the fascinating world of AI, examining its current capabilities, its potential for advancement, and the ethical considerations that accompany its rapid growth.\n\nAt its core, AI encompasses the creation of machines that can perform tasks typically requiring human intelligence, such as learning, problem-solving, and decision-making. This is achieved through algorithms and data sets that train AI systems to recognize patterns, make predictions, and adapt to new information. The field can be broadly categorized into two main types: Narrow AI, designed for specific tasks like playing chess or translating languages, and General AI, which",
                ],
            },
        ]
    )
    while not stop_chat:
        response = chat_session.send_message(query)
        response_text = response.text
        say(response_text)
        chatstr += f"{response_text}\n"
        return response_text
    
    
def say(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
    
def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=1)
        r.pause_threshold=0.3
        r.non_speaking_duration = 0.2
        audio=r.listen(source)
        try:
            print("recognising")
            query=r.recognize_google(audio,language='en-in')
            print(f"User said: {query}")
            return query
        except Exception as e:
            return "Some Error Occured."

if __name__ == '__main__':
    print("Jai Siya Ram")
    say("Naammaastttaaa")
    say("SHINO this side")
    while True:
        print("Listening....") 
        query=takeCommand()
        sites=[["youtube","https://www.youtube.com"],['google',"https://www.google.com"],['cuims','https://uims.cuchd.in/'],['chat gpt','https://chatgpt.com/'],['instagram','https://www.instagram.com/accounts/login/?hl=en']]
        for site in sites:
            if f"Open {site[0]}".lower() in query.lower():
                say(f"Opening {site[0]} sir...") 
                webbrowser.open(site[1])
                
        if 'open music' in query:
            musicpath=r"C:\Users\chait\Downloads\_Jai Shri Ram_320(PagalWorld.com.sb).mp3"
            say("Playing Music")
            os.startfile(musicpath)
        
        
        elif 'the time' in query:
            strfTime=datetime.datetime.now().strftime("%H:%M:%S")
            say(f"Sir the time is {strfTime}")
        # say(query)
        
        elif "using AI".lower() in query.lower():
            ai(prompt=query)
        
        elif "QUIT".lower() in query.lower():
            exit()
        
        elif "reset chat".lower() in query.lower():
            chatstr=""
        
        elif "tell me about".lower() in query.lower():
            # print("Chatting")
            # chat(query)
            # stop_chat = False
            while not stop_chat:
                response = chat(query)
                if response is None:
                    break  # Break if chat function stops
                # Listen for stop command during chat
                query = takeCommand()
                if "stop chat" in query:
                    stop_chat = True
                    say("Stopping chat.")
                    break









            
        
