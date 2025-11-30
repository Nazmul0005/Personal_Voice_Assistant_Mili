#import necessary libraries
import speech_recognition as sr
import pyttsx3
import logging
import datetime
import os
import webbrowser
import subprocess
import random
import wikipedia
from google import genai
from google.genai import types
import pyjokes
import psutil
import ctypes
import pyautogui
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from comtypes import CLSCTX_ALL
from ctypes import cast, POINTER
import threading
import shutil
from pathlib import Path
import json
from github import Github
import git
from dotenv import load_dotenv
load_dotenv()

#logging configuration
LOG_DIR = "logs"
LOG_FILE_NAME="application.log"
os.makedirs(LOG_DIR, exist_ok=True)
log_path=os.path.join(LOG_DIR, LOG_FILE_NAME)
logging.basicConfig(
    filename=log_path,
    format="[%(asctime)s] %(levelname)s: %(message)s",
    level=logging.INFO
)


#Activate voice from our system
#initialize the speech engine
engine= pyttsx3.init('sapi5')

#Working on voice properties
#set voice property
voices=engine.getProperty('voices')
#voice type selection
engine.setProperty('voice', voices[1].id)
#voice rate selection
engine.setProperty('rate', 190)

#volume control
engine.setProperty('volume', 1)



def speak(text):
    """ This function will speak the text passed to it.

    Args:
        text
    returns:
        voice output
    """

    engine.say(text)
    print(f"Mili: {text}")
    #run and wait method to process the voice commands and wait until it's finished
    engine.runAndWait()


def close_application(app_name):
    """ This function will close an application by its process name.
    
    Args:
        app_name: name of the application to close (e.g., 'calc.exe', 'notepad.exe')
    returns:
        True if closed successfully, False otherwise
    """
    try:
        closed = False
        for proc in psutil.process_iter(['name']):
            if proc.info['name'].lower() == app_name.lower():
                proc.kill()
                closed = True
        
        if closed:
            speak(f"Closed {app_name.replace('.exe', '')}")
            logging.info(f"Closed {app_name}")
            return True
        else:
            speak(f"{app_name.replace('.exe', '')} is not running")
            logging.info(f"{app_name} was not found running")
            return False
    except Exception as e:
        speak(f"Could not close {app_name.replace('.exe', '')}")
        logging.info(f"Error closing {app_name}: {e}")
        return False


def get_system_stats():
    """ Get CPU and RAM usage statistics """
    try:
        cpu_percent = psutil.cpu_percent(interval=1)
        memory = psutil.virtual_memory()
        ram_percent = memory.percent
        ram_available_gb = memory.available / (1024**3)
        
        speak(f"CPU usage is {cpu_percent} percent")
        speak(f"RAM usage is {ram_percent} percent. {ram_available_gb:.1f} gigabytes available")
        logging.info(f"System stats: CPU {cpu_percent}%, RAM {ram_percent}%")
    except Exception as e:
        speak("Could not retrieve system statistics")
        logging.info(f"Error getting system stats: {e}")


def get_volume_interface():
    """ Get the volume interface for Windows """
    try:
        devices = AudioUtilities.GetSpeakers()
        interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
        volume = cast(interface, POINTER(IAudioEndpointVolume))
        return volume
    except:
        return None


def set_volume(level):
    """ Set system volume to a specific level (0-100) """
    try:
        volume = get_volume_interface()
        if volume:
            volume.SetMasterVolumeLevelScalar(level / 100, None)
            speak(f"Volume set to {level} percent")
            logging.info(f"Volume set to {level}%")
        else:
            speak("Could not control volume")
    except Exception as e:
        speak("Could not change volume")
        logging.info(f"Error setting volume: {e}")


def increase_volume():
    """ Increase system volume by 10% """
    try:
        volume = get_volume_interface()
        if volume:
            current = volume.GetMasterVolumeLevelScalar()
            new_volume = min(current + 0.1, 1.0)
            volume.SetMasterVolumeLevelScalar(new_volume, None)
            speak(f"Volume increased to {int(new_volume * 100)} percent")
            logging.info(f"Volume increased to {int(new_volume * 100)}%")
        else:
            speak("Could not control volume")
    except Exception as e:
        speak("Could not increase volume")
        logging.info(f"Error increasing volume: {e}")


def decrease_volume():
    """ Decrease system volume by 10% """
    try:
        volume = get_volume_interface()
        if volume:
            current = volume.GetMasterVolumeLevelScalar()
            new_volume = max(current - 0.1, 0.0)
            volume.SetMasterVolumeLevelScalar(new_volume, None)
            speak(f"Volume decreased to {int(new_volume * 100)} percent")
            logging.info(f"Volume decreased to {int(new_volume * 100)}%")
        else:
            speak("Could not control volume")
    except Exception as e:
        speak("Could not decrease volume")
        logging.info(f"Error decreasing volume: {e}")


def mute_system():
    """ Mute or unmute the system """
    try:
        volume = get_volume_interface()
        if volume:
            is_muted = volume.GetMute()
            volume.SetMute(not is_muted, None)
            if is_muted:
                speak("System unmuted")
                logging.info("System unmuted")
            else:
                speak("System muted")
                logging.info("System muted")
        else:
            speak("Could not control volume")
    except Exception as e:
        speak("Could not mute system")
        logging.info(f"Error muting system: {e}")


def get_battery_status():
    """ Get battery percentage and charging status """
    try:
        battery = psutil.sensors_battery()
        if battery:
            percent = battery.percent
            plugged = battery.power_plugged
            status = "charging" if plugged else "not charging"
            speak(f"Battery is at {percent} percent and {status}")
            logging.info(f"Battery: {percent}%, {status}")
        else:
            speak("Could not detect battery. You might be using a desktop computer")
            logging.info("No battery detected")
    except Exception as e:
        speak("Could not retrieve battery status")
        logging.info(f"Error getting battery status: {e}")


def take_screenshot():
    """ Take a screenshot and save it """
    try:
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        screenshot_dir = os.path.join(os.path.expanduser("~"), "Pictures", "Screenshots")
        os.makedirs(screenshot_dir, exist_ok=True)
        
        filename = os.path.join(screenshot_dir, f"screenshot_{timestamp}.png")
        screenshot = pyautogui.screenshot()
        screenshot.save(filename)
        
        speak("Screenshot taken and saved")
        logging.info(f"Screenshot saved: {filename}")
    except Exception as e:
        speak("Could not take screenshot")
        logging.info(f"Error taking screenshot: {e}")


def lock_computer():
    """ Lock the computer """
    try:
        speak("Locking your computer")
        logging.info("Locking computer")
        ctypes.windll.user32.LockWorkStation()
    except Exception as e:
        speak("Could not lock computer")
        logging.info(f"Error locking computer: {e}")


def sleep_computer():
    """ Put computer to sleep """
    try:
        speak("Putting computer to sleep")
        logging.info("Computer going to sleep")
        os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
    except Exception as e:
        speak("Could not put computer to sleep")
        logging.info(f"Error sleeping computer: {e}")


def shutdown_computer(delay=0):
    """ Shutdown computer with optional delay in seconds """
    try:
        if delay > 0:
            minutes = delay // 60
            speak(f"Computer will shutdown in {minutes} minutes")
            logging.info(f"Shutdown scheduled in {delay} seconds")
            os.system(f"shutdown /s /t {delay}")
        else:
            speak("Shutting down computer now")
            logging.info("Immediate shutdown")
            os.system("shutdown /s /t 0")
    except Exception as e:
        speak("Could not shutdown computer")
        logging.info(f"Error shutting down: {e}")


def cancel_shutdown():
    """ Cancel a scheduled shutdown """
    try:
        os.system("shutdown /a")
        speak("Shutdown cancelled")
        logging.info("Shutdown cancelled")
    except Exception as e:
        speak("Could not cancel shutdown")
        logging.info(f"Error cancelling shutdown: {e}")


# File and Folder Management Functions

def create_folder(folder_name, location=None):
    """ Create a new folder """
    try:
        if location is None:
            location = os.path.expanduser("~\\Desktop")
        
        folder_path = os.path.join(location, folder_name)
        os.makedirs(folder_path, exist_ok=True)
        speak(f"Folder {folder_name} created successfully")
        logging.info(f"Created folder: {folder_path}")
        return True
    except Exception as e:
        speak(f"Could not create folder {folder_name}")
        logging.info(f"Error creating folder: {e}")
        return False


def delete_folder(folder_name, location=None):
    """ Delete a folder """
    try:
        if location is None:
            location = os.path.expanduser("~\\Desktop")
        
        folder_path = os.path.join(location, folder_name)
        if os.path.exists(folder_path) and os.path.isdir(folder_path):
            shutil.rmtree(folder_path)
            speak(f"Folder {folder_name} deleted successfully")
            logging.info(f"Deleted folder: {folder_path}")
            return True
        else:
            speak(f"Folder {folder_name} not found")
            logging.info(f"Folder not found: {folder_path}")
            return False
    except Exception as e:
        speak(f"Could not delete folder {folder_name}")
        logging.info(f"Error deleting folder: {e}")
        return False


def delete_file(filename, location=None):
    """ Delete a file """
    try:
        if location is None:
            location = os.path.expanduser("~\\Desktop")
        
        file_path = os.path.join(location, filename)
        if os.path.exists(file_path) and os.path.isfile(file_path):
            os.remove(file_path)
            speak(f"File {filename} deleted successfully")
            logging.info(f"Deleted file: {file_path}")
            return True
        else:
            speak(f"File {filename} not found")
            logging.info(f"File not found: {file_path}")
            return False
    except Exception as e:
        speak(f"Could not delete file {filename}")
        logging.info(f"Error deleting file: {e}")
        return False


def search_files(extension, location=None):
    """ Search for files with specific extension """
    try:
        if location is None:
            location = os.path.expanduser("~\\Documents")
        
        # Add dot if not present
        if not extension.startswith('.'):
            extension = '.' + extension
        
        found_files = []
        for root, dirs, files in os.walk(location):
            for file in files:
                if file.endswith(extension):
                    found_files.append(os.path.join(root, file))
                    if len(found_files) >= 10:  # Limit to 10 files
                        break
            if len(found_files) >= 10:
                break
        
        if found_files:
            speak(f"Found {len(found_files)} {extension} files")
            for i, file in enumerate(found_files[:5], 1):
                filename = os.path.basename(file)
                speak(f"{i}. {filename}")
            if len(found_files) > 5:
                speak(f"And {len(found_files) - 5} more files")
            logging.info(f"Found {len(found_files)} {extension} files in {location}")
        else:
            speak(f"No {extension} files found in {os.path.basename(location)}")
            logging.info(f"No {extension} files found in {location}")
        
        return found_files
    except Exception as e:
        speak(f"Could not search for files")
        logging.info(f"Error searching files: {e}")
        return []


def open_folder(folder_name):
    """ Open a specific folder """
    try:
        user_home = os.path.expanduser("~")
        
        # Common folder mappings
        folders = {
            "downloads": os.path.join(user_home, "Downloads"),
            "documents": os.path.join(user_home, "Documents"),
            "desktop": os.path.join(user_home, "Desktop"),
            "pictures": os.path.join(user_home, "Pictures"),
            "videos": os.path.join(user_home, "Videos"),
            "music": os.path.join(user_home, "Music"),
        }
        
        folder_path = folders.get(folder_name.lower())
        
        if folder_path and os.path.exists(folder_path):
            os.startfile(folder_path)
            speak(f"Opening {folder_name} folder")
            logging.info(f"Opened folder: {folder_path}")
            return True
        else:
            speak(f"Could not find {folder_name} folder")
            logging.info(f"Folder not found: {folder_name}")
            return False
    except Exception as e:
        speak(f"Could not open {folder_name} folder")
        logging.info(f"Error opening folder: {e}")
        return False




#This function recognizes the voice command from the user
def takeCommand():
    """ This function will take the voice command from the user and return it as text.

    Args:
        text as query
    """
    # print(sr.Microphone.list_microphone_names())
    r=sr.Recognizer()
    with sr.Microphone(device_index=2) as source:
        r.adjust_for_ambient_noise(source, duration=1)
        print("Listening...")
        # r.pause_threshold=1
        audio=r.listen(source)

    try:
        print("Recognizing...")
        text=r.recognize_google(audio, language='en-in')
        print(f"User said: {text}\n")

    except Exception as e:
        logging.info(e)
        print("Say that again please...")
        return None

    return text


def greeting():
    """ This function will greet the user based on the time of the day.

    Args:
        None
    returns:
        voice output
    """
    hour=int(datetime.datetime.now().hour)
    if 0<=hour<12:
        speak("Good Morning!")
    elif 12<=hour<18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")

    speak("I am Mili. How can I help you today?")

greeting()


def play_music():
    """ This function will play a random music from the music directory.

    Args:
        None
    returns:
        voice output
    """
    music_dir=r"C:\Users\nazmu\Music\incpetion\personal_voice_assistant_mili\music"
    try:
        songs=os.listdir(music_dir)
        if songs:
            random_song=random.choice(songs)
            os.startfile(os.path.join(music_dir,random_song))
        else:
            speak("No songs found in the music directory.")
            logging.info("No songs found in the music directory.")
    except Exception as e:
        speak("sorry, I could not find the music directory.")
        logging.info(e)


client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))
def gemini_model_response(prompt):
    """ This function will get the response from the Gemini model.

    Args:
        prompt
    returns:
        response from the model
    """
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        config=types.GenerateContentConfig(
        system_instruction="You are Mili. You are a personal asistant. Who answer everthing in 1 or 2 sentences."),
        contents=prompt
    )
    return response.text



def generate_project_code(description):
    """Generate complete project code based on description using Gemini.
    
    Args:
        description: Problem description
    Returns:
        Dictionary with project files
    """
    prompt = f"""
    Create a complete Python project for: {description}
    
    Return ONLY a valid JSON object with this structure (no markdown, no explanation):
    {{
        "project_name": "short-kebab-case-name",
        "description": "brief description",
        "main_code": "complete main.py code",
        "requirements": "list of pip packages (one per line)",
        "readme": "complete README.md content"
    }}
    
    Make sure the code is complete, functional, and well-commented.
    """
    
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )
    
    try:
        # Clean the response
        text = response.text.strip()
        # Remove markdown code blocks if present
        if text.startswith("```json"):
            text = text[7:]
        if text.startswith("```"):
            text = text[3:]
        if text.endswith("```"):
            text = text[:-3]
        text = text.strip()
        
        project_data = json.loads(text)
        return project_data
    except json.JSONDecodeError as e:
        logging.error(f"JSON parsing error: {e}")
        logging.error(f"Response text: {response.text}")
        return None


def create_github_repo(project_name, description, project_path):
    """Create GitHub repository and push code.
    
    Args:
        project_name: Name of the repository
        description: Repository description
        project_path: Local path of the project
    Returns:
        Repository URL or None
    """
    try:
        # Initialize GitHub
        github_token = os.getenv("GITHUB_TOKEN")
        if not github_token:
            speak("GitHub token not found. Please add it to your .env file.")
            logging.error("GITHUB_TOKEN not found in environment variables")
            return None
        
        g = Github(github_token)
        user = g.get_user()
        
        speak("Creating GitHub repository...")
        
        # Create repo
        repo = user.create_repo(
            name=project_name,
            description=description,
            private=False,
            auto_init=False
        )
        
        logging.info(f"GitHub repo created: {repo.html_url}")
        
        # Initialize git and push
        repo_obj = git.Repo.init(project_path)
        origin = repo_obj.create_remote('origin', repo.clone_url)
        
        # Add all files
        repo_obj.git.add(A=True)
        repo_obj.index.commit("Initial commit: Project setup")
        
        # Push to GitHub
        speak("Pushing code to GitHub...")
        origin.push(refspec='master:main')
        
        return repo.html_url
        
    except Exception as e:
        logging.error(f"GitHub error: {e}")
        speak(f"Error creating GitHub repository: {str(e)}")
        return None


def create_project_and_push(description):
    """Main function to create project and push to GitHub.
    
    Args:
        description: Problem description
    """
    try:
        speak("Generating project code. This may take a moment...")
        logging.info(f"Generating project for: {description}")
        
        # Generate code
        project_data = generate_project_code(description)
        
        if not project_data:
            speak("Failed to generate project. Please try again.")
            return
        
        project_name = project_data.get("project_name", "generated-project")
        
        # Create project directory
        projects_dir = "generated_projects"
        os.makedirs(projects_dir, exist_ok=True)
        project_path = os.path.join(projects_dir, project_name)
        
        if os.path.exists(project_path):
            speak("A project with this name already exists. Please try a different description.")
            return
        
        os.makedirs(project_path)
        
        speak("Creating project files...")
        
        # Write main.py
        with open(os.path.join(project_path, "main.py"), "w", encoding="utf-8") as f:
            f.write(project_data.get("main_code", "# Code generation failed"))
        
        # Write requirements.txt
        with open(os.path.join(project_path, "requirements.txt"), "w", encoding="utf-8") as f:
            f.write(project_data.get("requirements", ""))
        
        # Write README.md
        with open(os.path.join(project_path, "README.md"), "w", encoding="utf-8") as f:
            f.write(project_data.get("readme", f"# {project_name}"))
        
        logging.info(f"Project files created at: {project_path}")
        
        # Create GitHub repo and push
        repo_url = create_github_repo(
            project_name,
            project_data.get("description", description),
            project_path
        )
        
        if repo_url:
            speak(f"Success! Repository created and pushed to GitHub.")
            speak(f"You can view it at {repo_url}")
            logging.info(f"Project successfully pushed to: {repo_url}")
            
            # Optionally open in browser
            webbrowser.open(repo_url)
        else:
            speak("Project created locally but failed to push to GitHub.")
            logging.warning("GitHub push failed but local project created")
        
    except Exception as e:
        logging.error(f"Project creation error: {e}")
        speak(f"An error occurred: {str(e)}")













while True:
    query=takeCommand()
    
    if query is None:
        continue
    
    query = query.lower()

    if "your name" in query:
        speak("I am Mili, your personal assistant.")
        logging.info("User asked for assistant's name.")
    
    elif "time" in query:
        strTime=datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"The time is {strTime}")
        logging.info("User asked for current time.")
    
    elif "who made you" in query or "who created you" in query:
        speak("I was created by a Nazmul Islam.")
        logging.info("User asked about assistant's creator.")

    elif "thank you" in query or "thanks" in query or "thank" in query:
        responses = [
            "You're welcome!",
            "No problem!",
            "Glad I could help!",
            "Anytime!"
        ]
        speak(random.choice(responses))
        logging.info("User expressed gratitude.")
    
    elif "joke" in query:
        joke=pyjokes.get_joke(language="en", category="all")
        speak(joke)
        logging.info("User requested a joke.")

    elif "play music" in query or "music" in query:
        speak("Playing music for you.")
        play_music()
        logging.info("User requested to play music.")
    
    # System Control Commands
    elif "cpu usage" in query or ("cpu" in query and "usage" not in query):
        get_system_stats()
        logging.info("User requested system stats.")
    
    elif "ram" in query or "memory" in query:
        get_system_stats()
        logging.info("User requested memory stats.")
    
    elif "increase volume" in query or "volume up" in query:
        increase_volume()
        logging.info("User increased volume.")
    
    elif "decrease volume" in query or "volume down" in query:
        decrease_volume()
        logging.info("User decreased volume.")
    
    elif "set volume" in query:
        try:
            # Extract number from query
            words = query.split()
            for i, word in enumerate(words):
                if word.isdigit():
                    level = int(word)
                    set_volume(level)
                    break
        except:
            speak("Please specify a volume level between 0 and 100")
        logging.info("User set volume level.")
    
    elif "mute" in query or "unmute" in query:
        mute_system()
        logging.info("User toggled mute.")
    
    elif "battery" in query:
        get_battery_status()
        logging.info("User requested battery status.")
    
    elif "screenshot" in query or "take screenshot" in query:
        take_screenshot()
        logging.info("User took screenshot.")
    
    elif "lock" in query and "computer" in query:
        lock_computer()
        logging.info("User locked computer.")
    
    elif "sleep" in query and "computer" in query:
        sleep_computer()
        logging.info("User put computer to sleep.")
    
    elif "shutdown" in query:
        if "cancel" in query:
            cancel_shutdown()
        elif "10 minutes" in query or "ten minutes" in query:
            shutdown_computer(600)
        elif "5 minutes" in query or "five minutes" in query:
            shutdown_computer(300)
        else:
            speak("Do you want to shutdown now? Say yes to confirm")
            confirmation = takeCommand()
            if confirmation and "yes" in confirmation.lower():
                shutdown_computer(0)
            else:
                speak("Shutdown cancelled")
        logging.info("User requested shutdown.")

    # File Management Commands
    elif "create folder" in query:
        # Extract folder name
        folder_name = query.replace("create folder", "").replace("called", "").replace("a", "").strip()
        if folder_name:
            create_folder(folder_name)
        else:
            speak("Please specify a folder name")
        logging.info("User requested to create folder")

    elif "delete folder" in query:
        folder_name = query.replace("delete folder", "").replace("called", "").strip()
        if folder_name:
            delete_folder(folder_name)
        else:
            speak("Please specify a folder name")
        logging.info("User requested to delete folder")

    elif "delete file" in query:
        filename = query.replace("delete file", "").strip()
        if filename:
            delete_file(filename)
        else:
            speak("Please specify a file name")
        logging.info("User requested to delete file")

    elif "find" in query and "files" in query:
        # Extract file extension (e.g., "find PDF files")
        words = query.split()
        for i, word in enumerate(words):
            if word.lower() in ["pdf", "docx", "txt", "jpg", "png", "mp3", "mp4", "xlsx", "pptx"]:
                search_files(word)
                break
        logging.info("User requested file search")

    elif "open downloads" in query or "open download" in query:
        open_folder("downloads")
        logging.info("User opened Downloads folder")

    elif "open documents" in query:
        open_folder("documents")
        logging.info("User opened Documents folder")

    elif "open desktop" in query:
        open_folder("desktop")
        logging.info("User opened Desktop folder")

    elif "open pictures" in query:
        open_folder("pictures")
        logging.info("User opened Pictures folder")


    elif "create project" in query or "generate project" in query:
        speak("Sure! Please describe the project you want to create.")
        project_description = takeCommand()
        
        if "say that again" not in project_description.lower():
            create_project_and_push(project_description)
        else:
            speak("I didn't catch that. Let's try again later.")
        
        logging.info("User requested project creation.")


    #if wikipedias do not found any information then handle the exception
    elif "wikipedia" in query:
        speak("Searching Wikipedia...")
        query=query.replace("wikipedia", "")
        results=wikipedia.summary(query, sentences=2)
        speak("According to Wikipedia")
        speak(results)
        logging.info("User searched Wikipedia.")
    
    elif "open google" in query:
        speak("Opening Google")
        webbrowser.open("google.com")
        logging.info("User opened Google.")
    
    elif "youtube" in query:
        speak("Opening YouTube")
        query=query.replace("youtube", "")
        webbrowser.open(f'https://www.youtube.com/results?search_query={query}')
        # webbrowser.open("youtube.com")
        logging.info("User opened YouTube.")
    
    elif "github" in query:
        speak("Opening GitHub")
        webbrowser.open("github.com")
        logging.info("User opened GitHub.")

    elif "linkedin" in query:
        speak("Opening LinkedIn")
        webbrowser.open("linkedin.com")
        logging.info("User opened LinkedIn.")
    
    elif "open calculator" in query:
        speak("Opening Calculator")
        subprocess.Popen('calc.exe')
        logging.info("User opened Calculator.")
    
    elif "close calculator" in query:
        close_application("CalculatorApp.exe")
        logging.info("User requested to close Calculator.")

    elif "open notepad" in query:
        speak("Opening Notepad")
        subprocess.Popen('notepad.exe')
        logging.info("User opened Notepad.")
    
    elif "close notepad" in query:
        close_application("notepad.exe")
        logging.info("User requested to close Notepad.")
    
    # if a exe is not opening, make sure to provide the correct path of the exe file
    #fix this issue
    #close the file after opening it

    #opening terminal is an issue now fix it
    elif "open terminal" in query or "terminal" in query:
        speak("Opening Terminal")
        subprocess.Popen('cmd.exe')
        logging.info("User opened Terminal.")
    
    elif "close terminal" in query:
        close_application("cmd.exe")
        logging.info("User requested to close Terminal.")

    elif "open calendar" in query or "calendar" in query:
        speak("Opening Calendar")
        webbrowser.open("calendar.google.com")
        logging.info("User opened Calendar.")
    
    elif 'exit' in query or 'stop' in query or 'bye' in query:
        speak("Goodbye! Have a nice day.")
        logging.info("User exited the application.")
        exit()

    else:
        try:
            response=gemini_model_response(query)
            speak(response)
            logging.info("User asked for other question")
        except Exception as e:
            speak("I'm sorry, I didn't understand that command.")
            logging.info("User command not recognized.")
        

#do the modularization
