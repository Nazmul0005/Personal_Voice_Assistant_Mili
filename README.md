# Mili Voice Assistant (`mili.py`)

Mili is a powerful, Python-based personal voice assistant designed to automate system tasks, manage files, and assist with coding projects. It integrates with Google's Gemini AI for intelligent responses and code generation, and connects to GitHub for project management.

## 🚀 Features

### 1. 🤖 AI & Coding Assistance

-**General Queries**: Ask any question and get intelligent responses powered by Google Gemini 2.5 Flash.

-**Project Generation**:

    -**Command**: "Create a project called [description]" or "Generate project [description]"

    -**How it works**: Mili uses Google's Gemini AI to interpret your description and generates a complete, functional Python project.

    -**Output**: Creates a folder in `generated_projects/` containing:

    -`main.py`: The complete source code.

    -`requirements.txt`: List of necessary dependencies.

    -`README.md`: Documentation for the generated project.

-**GitHub Integration**:

    -**Automation**: After generating the project locally, Mili automatically:

    1. Creates a new**public** repository on your GitHub account.

    2. Initializes a local Git repository.

    3. Commits the generated files.

    4. Pushes the code to the new GitHub repository.

    -**Result**: You get a live GitHub URL ready to share or clone.

### 2. 💻 System Control

-**System Stats**: Check CPU and RAM usage.

-**Volume Control**: Increase, decrease, mute, or set specific volume levels.

-**Power Management**: Lock, sleep, or shutdown the computer (with timer options).

-**Battery Status**: Check battery percentage and charging status.

-**Screenshots**: Take and save screenshots instantly.

### 3. 📁 File & Folder Management

-**Create/Delete**: Create or delete folders and files via voice commands.

-**Search**: Find files by extension (e.g., "Find PDF files").

-**Navigation**: Open common directories like Downloads, Documents, Desktop, Pictures, etc.

### 4. 🌐 Web & Applications

-**App Control**: Open and close applications like Calculator, Notepad, Terminal, and PyCharm.

-**Web Navigation**: Open Google, YouTube, GitHub, LinkedIn, and Google Calendar.

-**Information**: Get current time, search Wikipedia, or hear a joke.

## 🛠️ Prerequisites

-**OS**: Windows (Required for `pyttsx3` sapi5 engine and system commands).

-**Python**: 3.x installed.

-**Git**: Installed and configured for GitHub integration.

## 📦 Installation

1. **Clone the repository** (if applicable) or download `mili.py`.
2. **Install dependencies**:

   ```bash

   pip install -r requirements.txt

   ```

   *Key libraries: `SpeechRecognition`, `pyttsx3`, `google-genai`, `psutil`, `pyautogui`, `pycaw`, `PyGithub`, `GitPython`.*
3. **Environment Setup**:

   Create a `.env` file in the same directory with your API keys:

   ```env

   GOOGLE_API_KEY=your_gemini_api_key

   GITHUB_TOKEN=your_github_personal_access_token

   ```

## 🎤 Usage

Run the assistant:

```bash

pythonmili.py

```

### Common Voice Commands

| Category | Command Examples |

|----------|------------------|

| **AI & Code** | "Create a project called [description]", "Who made you?" |

| **System** | "What's my CPU usage?", "Increase volume", "Take a screenshot", "Lock my computer" |

| **Files** | "Create a folder called [name]", "Find PDF files", "Open Downloads" |

| **Apps** | "Open Calculator", "Close Notepad", "Open PyCharm" |

| **Web** | "Open Google", "Search Wikipedia for [topic]", "Play music" |

| **General** | "What time is it?", "Tell me a joke", "Exit" |

## 📝 Notes

-**Microphone**: Ensure your microphone is set as the default recording device. The script currently uses `device_index=2` (you may need to adjust this in `takeCommand()` if it doesn't pick up audio).

-**Admin Rights**: Some system commands (like shutdown) might require running the script as Administrator.

## 🗣️ Demo Conversation

Here is a real interaction with Mili:

```text

User: sing a song for me

Mili: I can't physically sing, but I can share some lyrics for you! How about "Twinkle, twinkle, little star, how I wonder what you are?"


User: ok create a project

Mili: Okay, I can help with that! To get started, what kind of project are you looking to create, or what topic interests you?


User: create project

Mili: Sure! Please describe the project you want to create.


User: project which actually multiplication two number

Mili: Generating project code. This may take a moment...

Mili: Creating project files...

Mili: Creating GitHub repository...

Mili: Pushing code to GitHub...

Mili: Success! Repository created and pushed to GitHub.

Mili: You can view it at https://github.com/Nazmul0005/two-number-multiplier


User: open calculator

Mili: Opening Calculator


User: close calculator

Mili: Closed CalculatorApp


User: open YouTube content

Mili: Opening YouTube


User: what can you do for me

Mili: I can assist you by providing information, answering your questions, or helping with various tasks you might have. Just let me know what you need!


User: open pictures

Mili: Opening pictures folder


User: create folders document

Mili: Folder s document created successfully


User: delete folder I

Mili: Folder i deleted successfully


User: according Wikipedia what is python

Mili: Searching Wikipedia...

Mili: According to Wikipedia

Mili: Monty Python, also known as the Pythons, were a British comedy troupe formed in 1969...


User: what is your name

Mili: I am Mili, your personal assistant.


User: what time is now

Mili: The time is 16:35:29


User: who made you

Mili: I was created by a Nazmul Islam.


User: I want to hear a joke

Mili: Unix is user friendly. It's just very particular about who its friends are.


User: what is the CPU

Mili: CPU usage is 11.0 percent

Mili: RAM usage is 85.2 percent. 2.3 gigabytes available


User: ok bye

Mili: Goodbye! Have a nice day.

```
