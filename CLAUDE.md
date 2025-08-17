# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This repository contains debugging tools for Claude Code development workflows.

### Screenshot Tool
A macOS app for capturing screenshots during debugging sessions. Automatically saves screenshots as `debug-snap.jpg` and copies analysis text to clipboard for use with Claude Code.

## Build and Development Commands

### Screenshot Tool
- **Run directly**: Double-click `ScreenshotTool_v4.app`
- **Test shell version**: `./screenshot.sh`
- **Setup dependencies**: `./setup.sh`

## Architecture Overview

### Technology Stack
- **AppleScript**: Main screenshot tool implementation
- **Python**: Alternative implementations and icon generation
- **Shell Scripts**: Simple command-line alternatives

### File Structure
```
Debug/
├── ScreenshotTool_v4.app          # Main screenshot app (recommended)
├── screenshot.sh                  # Shell script version
├── bug.png                        # Icon source file
├── menubar_screenshot.py          # Menu bar version (experimental)
├── quick_screenshot.py            # Single-shot Python version
└── create_bug_icon.py            # Icon generation utility
```

### Key Features
- **Region Selection**: Uses `screencapture -s` for accurate window/area capture
- **Auto-save**: Saves to `/Users/jeremywheeler/Dropbox/Code/Projects/_ExamCatalyst/ExamCatalyst_v2/debug-snap.jpg`
- **Clipboard Integration**: Automatically copies "Please analyze 'debug-snap.jpg', which is a screenshot I just took. Focus specifically on the following: "
- **Custom Icon**: Uses bug.png as app icon

## Development Guidelines

### Screenshot Tool Usage
1. Click `ScreenshotTool_v4.app` to launch
2. Drag to select screen region
3. Screenshot automatically saved as `debug-snap.jpg`
4. Paste clipboard text in Claude Code for analysis

### Troubleshooting
- **Permission Issues**: Use `ScreenshotTool_v4.app` (bypasses screen recording permissions)
- **Icon Not Showing**: Run `killall Finder && killall Dock` to refresh
- **Wrong Capture Area**: Ensure using v4 which has `-s` flag for proper selection