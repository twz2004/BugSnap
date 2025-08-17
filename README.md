# BugSnap

A lightweight macOS menu bar application for taking screenshots during debugging sessions.

## Features

- Lives in the menu bar (not in the dock)
- Quick screenshot capture with region selection
- Automatically saves screenshots as `debug-snap.jpg`
- Copies analysis prompt to clipboard for use with AI assistants
- Shows as "BugSnap" in Privacy & Security settings

## Installation

1. Download or clone this repository
2. Double-click `BugSnap.app` to launch
3. Grant screen recording permissions when prompted

## Usage

1. Click the bug icon in the menu bar
2. Select "Take Screenshot"
3. Click and drag to select the area to capture
4. Screenshot is saved to `/Users/jeremywheeler/Dropbox/Code/Projects/_ExamCatalyst/ExamCatalyst_v2/debug-snap.jpg`
5. A prompt is automatically copied to your clipboard

## Requirements

- macOS 10.15 or later
- Python 3.9+
- rumps library (`pip3 install rumps`)

## Files

- `BugSnap.app` - Main application bundle
- `bugsnap_menubar.py` - Python script that powers the menu bar app
- `bug.png` - Icon source file
- `CLAUDE.md` - Development documentation

## Development

The app uses AppleScript to launch a Python script with the rumps library for menu bar functionality.