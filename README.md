# BugSnap 🐛

A lightweight macOS menu bar application for capturing screenshots during debugging sessions. Perfect for developers who need quick, hassle-free screenshots with automatic clipboard formatting for AI assistants.

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![macOS](https://img.shields.io/badge/macOS-10.15%2B-green.svg)
![Python](https://img.shields.io/badge/python-3.9%2B-blue.svg)

## Features

- 🎯 **Menu Bar Only** - Lives exclusively in your menu bar, no dock clutter
- 📸 **Smart Screenshot** - Interactive region/window selection with proper window capture
- 💾 **Auto-Save** - Automatically saves as `debug-snap.jpg` to a predefined location  
- 📋 **AI-Ready Clipboard** - Copies formatted prompt for immediate use with Claude, ChatGPT, etc.
- 🔒 **Privacy Friendly** - Shows as "BugSnap" in System Settings > Privacy & Security
- 🎨 **Custom Icon** - Clean bug icon for easy identification

## Installation

### Quick Start
1. Download the latest release from [Releases](https://github.com/twz2004/BugSnap/releases)
2. Double-click `BugSnap.app` to launch
3. Grant screen recording permissions when prompted
4. Look for the bug icon in your menu bar!

### From Source
```bash
# Clone the repository
git clone https://github.com/twz2004/BugSnap.git
cd BugSnap

# Install dependencies
pip3 install rumps

# Launch the app
open BugSnap.app
```

## Usage

1. **Click** the bug icon in your menu bar
2. **Select** "Take Screenshot" from the dropdown
3. **Click and drag** to select a region, or click on a window
4. **Done!** Your screenshot is saved and the clipboard is ready

### Screenshot Location
Screenshots are automatically saved to:
```
~/Dropbox/Code/Projects/_ExamCatalyst/ExamCatalyst_v2/debug-snap.jpg
```

### Clipboard Content
After capturing, your clipboard will contain:
```
Please analyze 'debug-snap.jpg', which is a screenshot I just took. Focus specifically on the following: 
```

Perfect for pasting directly into AI assistants!

## Requirements

- **macOS** 10.15 (Catalina) or later
- **Python** 3.9 or later
- **rumps** library (installed via pip)

## Project Structure

```
BugSnap/
├── BugSnap.app/          # macOS application bundle
├── bugsnap_menubar.py    # Core Python script
├── bug.png               # Application icon
├── README.md             # This file
└── CLAUDE.md            # AI assistant instructions
```

## Known Issues

- **Dock Icon**: Python interpreter may show briefly in dock during launch
- **Notification Icon**: System notifications use default icon instead of bug icon

## Development

BugSnap uses a hybrid approach:
- **AppleScript** application wrapper for macOS integration
- **Python + rumps** for menu bar functionality
- **screencapture** command-line tool for capturing

### Building from Source

Currently, the app uses AppleScript to launch a Python script. Future versions may use py2app for a more integrated experience.

### Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Troubleshooting

### App doesn't appear in menu bar
- Make sure Python 3.9+ is installed
- Check that rumps is installed: `pip3 install rumps`
- Try launching from Terminal to see error messages: `python3 bugsnap_menubar.py`

### Screenshots not saving
- Verify the target directory exists
- Check write permissions for the save location
- Ensure you've granted screen recording permissions

### Permission Issues
- Go to System Settings > Privacy & Security > Screen Recording
- Ensure "BugSnap" is checked
- You may need to restart the app after granting permissions

## License

MIT License - feel free to use this in your own projects!

## Acknowledgments

- Built with [rumps](https://github.com/jaredks/rumps) - Ridiculously Uncomplicated macOS Python Statusbar apps
- Icon from custom design
- Created to streamline debugging workflows with AI assistants

## Author

Created by Jeremy Wheeler ([@twz2004](https://github.com/twz2004))

---

**Note**: This tool saves screenshots to a specific hardcoded path. You may want to modify `bugsnap_menubar.py` to customize the save location for your workflow.