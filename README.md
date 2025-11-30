# 🎤 Mili Voice Assistant

A powerful Python-based personal voice assistant that automates system tasks, manages files, and assists with coding projects. Mili integrates with Google's Gemini AI for intelligent responses and code generation, with seamless GitHub integration for project management.

## ✨ Features

### 🤖 AI & Coding Assistance

- **Intelligent Conversations**: Ask questions and receive AI-powered responses using Google Gemini 2.5 Flash
- **Automated Project Generation**: 
  - Describe your project idea in natural language
  - Mili generates complete, functional Python projects with:
    - `main.py` - Complete source code
    - `requirements.txt` - All dependencies listed
    - `README.md` - Project documentation
  - Projects are saved in `generated_projects/` directory

- **GitHub Integration**:
  - Automatically creates public repositories on your GitHub account
  - Initializes local Git repository
  - Commits and pushes code to GitHub
  - Provides live GitHub URL for sharing

**Example Commands:**
- "Create a project called calculator app"
- "Generate project for web scraper"

### 💻 System Control

- **System Monitoring**: Check CPU and RAM usage in real-time
- **Volume Management**: Increase, decrease, mute, or set specific volume levels
- **Power Options**: Lock, sleep, or shutdown with optional timers
- **Battery Info**: Monitor battery percentage and charging status
- **Screenshots**: Capture and save screenshots instantly

**Example Commands:**
- "What's my CPU usage?"
- "Increase volume"
- "Take a screenshot"
- "Lock my computer"

### 📁 File & Folder Management

- **Create/Delete**: Manage folders and files through voice commands
- **Search**: Find files by extension (PDF, DOCX, etc.)
- **Quick Navigation**: Open common directories (Downloads, Documents, Desktop, Pictures)

**Example Commands:**
- "Create a folder called projects"
- "Find PDF files"
- "Open Downloads"

### 🌐 Web & Applications

- **Application Control**: Launch and close apps (Calculator, Notepad, Terminal, PyCharm)
- **Web Navigation**: Quick access to Google, YouTube, GitHub, LinkedIn, Google Calendar
- **Information Services**: Current time, Wikipedia searches, jokes, and more

**Example Commands:**
- "Open Calculator"
- "Search Wikipedia for Python programming"
- "What time is it?"

## 📋 Prerequisites

- **Operating System**: Windows (required for `pyttsx3` SAPI5 engine and system commands)
- **Python**: Version 3.7 or higher
- **Git**: Installed and configured for GitHub integration
- **Microphone**: Connected and set as default recording device

## 🔧 Installation

1. **Clone or download the repository**
   ```bash
   git clone <repository-url>
   cd mili-voice-assistant
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

   **Key dependencies:**
   - `SpeechRecognition` - Voice input processing
   - `pyttsx3` - Text-to-speech engine
   - `google-generativeai` - Gemini AI integration
   - `psutil` - System monitoring
   - `pyautogui` - Screenshot functionality
   - `pycaw` - Volume control
   - `PyGithub` - GitHub API integration
   - `GitPython` - Git operations

3. **Configure API keys**
   
   Create a `.env` file in the project root:
   ```env
   GOOGLE_API_KEY=your_gemini_api_key_here
   GITHUB_TOKEN=your_github_personal_access_token_here
   ```

   **To get your API keys:**
   - **Google Gemini API**: Visit [Google AI Studio](https://makersuite.google.com/app/apikey)
   - **GitHub Token**: Go to GitHub Settings → Developer settings → Personal access tokens → Generate new token (classic)
     - Required scopes: `repo`, `user`

## 🚀 Usage

Start Mili by running:
```bash
python mili.py
```

Speak clearly into your microphone after hearing Mili's prompt. The assistant will process your command and respond accordingly.

### Command Categories

| Category | Examples |
|----------|----------|
| **AI & Coding** | "Create a project called weather app", "Who made you?" |
| **System Info** | "CPU usage", "Battery status", "Take a screenshot" |
| **File Operations** | "Create folder reports", "Find PDF files", "Open Downloads" |
| **Applications** | "Open Calculator", "Close Notepad", "Launch PyCharm" |
| **Web Browsing** | "Open Google", "Search Wikipedia for AI", "Open YouTube" |
| **Utilities** | "What time is it?", "Tell me a joke", "Exit" |

## 🎯 Example Interaction

```
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

## ⚙️ Configuration

### Microphone Setup

The script uses `device_index=2` by default. If Mili doesn't pick up your voice:

1. List available microphones:
   ```python
   import speech_recognition as sr
   for index, name in enumerate(sr.Microphone.list_microphone_names()):
       print(f"Microphone {index}: {name}")
   ```

2. Update the `device_index` in the `takeCommand()` function in `mili.py`

### Permissions

Some commands require elevated permissions:
- **Shutdown/Sleep**: Run as Administrator on Windows
- **Volume Control**: Requires audio devices to be properly configured

## 🛠️ Troubleshooting

**Mili doesn't hear me:**
- Check microphone permissions and default device settings
- Adjust `device_index` in `takeCommand()` function

**GitHub push fails:**
- Verify your GitHub token has `repo` permissions
- Ensure Git is installed and configured (`git config --global user.name` and `user.email`)

**API errors:**
- Confirm `.env` file exists with valid API keys
- Check API quotas and rate limits

## 📄 License

This project is open source and available under the MIT License.

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the issues page.

## 👤 Author

**Nazmul Islam**

---

*Built with ❤️ using Python and Google Gemini AI*
