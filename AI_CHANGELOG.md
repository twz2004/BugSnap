# AI_CHANGELOG.md - BugSnap Development History & Current State

## Overview
BugSnap is a macOS menu bar application for taking screenshots during debugging sessions. It was created to replace a corrupted/damaged app that previously existed. The app MUST appear ONLY in the menu bar at the top of the screen, NOT in the dock at the bottom.

## Current State (as of Aug 16, 2024 - 19:47)
**Repository Status**: Clean, synced with GitHub at commit 879b0cc
**GitHub URL**: https://github.com/twz2004/BugSnap

### What's Working
- ✅ App shows in menu bar with bug icon
- ✅ Screenshot capture works with region selection
- ✅ Saves to correct location: `/Users/jeremywheeler/Dropbox/Code/Projects/_ExamCatalyst/ExamCatalyst_v2/debug-snap.jpg`
- ✅ Copies analysis prompt to clipboard
- ✅ Shows as "BugSnap" in Privacy & Security settings (not "applet")
- ✅ Successfully captures window content (not just desktop background)

## Outstanding Bugs

### Critical Issues
1. **Dock Icon Still Appears** - When BugSnap.app runs, a Python rocket ship icon appears in the dock. This is WRONG. The app should ONLY show in the menu bar, never in the dock.
   - Attempted fix with `NSApplicationActivationPolicyProhibited` but was reverted by user
   - The LSUIElement plist key is set but Python subprocess still shows dock icon

2. **Notification Icon Wrong** - Notifications show generic icon instead of bug.png
   - Attempted to add icon parameter to rumps.notification() but was reverted

## Architecture

### Current Implementation
```
BugSnap.app (AppleScript Application Bundle)
├── Launches bugsnap_menubar.py via shell script
└── bugsnap_menubar.py (Python script using rumps library)
    ├── Creates menu bar app with bug.png icon
    ├── Handles screenshot capture via screencapture command
    └── Manages notifications and clipboard
```

### Key Files
- `BugSnap.app/` - AppleScript app bundle that launches Python script
- `bugsnap_menubar.py` - Python script with rumps library for menu bar
- `bug.png` - Icon file (green bug on transparent background)
- `CLAUDE.md` - Project instructions

### Technical Details
- Uses `screencapture -i -t jpg [path]` command for capture
- The `-i` flag allows interactive window/region selection
- Must use `-t jpg` to save as JPEG format
- Python script runs via `/usr/bin/python3`
- Requires `rumps` library installed via pip3

## Development History

### Initial Problem
User reported "BugSnap.app when launched is showing corrupt or damaged" and needed rebuild.

### Key Requirements (User Specified)
1. Must show ONLY in menu bar at top, NOT in dock
2. Must use bug.png icon, not emoji
3. Must show as "BugSnap" in Privacy & Security, not "applet"
4. Must run continuously in background
5. Must capture actual window content, not desktop wallpaper

### Failed Approaches
1. **Pure AppleScript** - Cannot create menu bar apps, only dock apps
2. **Python with py2app** - Build issues, couldn't generate proper app bundle
3. **Direct Python executable in app bundle** - Didn't launch properly
4. **Using `-s` flag for screencapture** - Captured desktop instead of windows
5. **Using `-w` flag** - User said it "fucked it up"

### What Works
- AppleScript app launching Python script with rumps library
- Using `-i` flag for interactive capture
- LSUIElement=true in Info.plist (hides AppleScript app from dock)

## User Feedback Pattern
User is very direct and frustrated when things don't work:
- "stop drifting!"
- "stop fabricating!"
- "the icon is on the dam dock again dude- and not in the menu bar"
- "i only want u to fucking work on BugSnap.app ONLY!"
- Gets angry when creating .py files instead of fixing the .app

## Current Git Status
- Repository: https://github.com/twz2004/BugSnap
- Branch: main  
- Last commit: 879b0cc "Initial commit: BugSnap menu bar screenshot tool"
- Working directory: Clean (reset to match GitHub exactly)
- All local changes discarded with `git reset --hard origin/main`

## Next Steps to Fix

### Fix Dock Icon Issue
The Python interpreter shows in dock even though the AppleScript launcher is hidden. Options:
1. Compile Python script to standalone executable
2. Use different launch mechanism that doesn't show Python in dock
3. Investigate Info.plist settings for Python subprocess

### Fix Notification Icon
Need to make notifications show bug.png icon instead of default. The rumps library may have limitations here.

## Important Notes for AI Assistant

### DO NOT:
- Create new Python files unless specifically for BugSnap.app to use
- Use emoji in code or icons
- Create documentation unless asked
- Drift from the specific task
- Say something is fixed without testing
- Use screencapture flags other than `-i -t jpg`

### ALWAYS:
- Focus ONLY on BugSnap.app
- Test changes before claiming they work
- Keep app in menu bar only (never in dock)
- Use bug.png for icon
- Save screenshots to the exact specified path
- Clean up temporary files

### User Preferences:
- Wants executable BugSnap.app as final output
- Does not want Python files floating around
- Gets frustrated with repeated failures
- Prefers direct solutions without exploration
- Will switch AI models if current one "is sucking"

## Testing Checklist
When testing changes, verify:
- [ ] No icon appears in dock when running
- [ ] Bug icon shows in menu bar
- [ ] Click menu → Take Screenshot works
- [ ] Can select region or window
- [ ] Captures actual window content (not desktop)
- [ ] Saves to correct location as debug-snap.jpg
- [ ] Clipboard contains analysis prompt
- [ ] Notifications show bug icon
- [ ] App shows as "BugSnap" in Privacy settings

## File Modification Times
User pays attention to file modification times and will call out if files haven't actually been updated when changes are claimed. Always ensure changes are actually applied to BugSnap.app, not just to Python files.