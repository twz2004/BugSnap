#!/usr/bin/env python3
"""Launcher wrapper to hide Python from dock before starting the main app"""

import sys
import os

# CRITICAL: Set activation policy BEFORE any other imports
# This must happen before any GUI frameworks are loaded
from AppKit import NSApp, NSApplicationActivationPolicyProhibited
NSApp.setActivationPolicy_(NSApplicationActivationPolicyProhibited)

# Add parent directory to path to import the main script
sys.path.insert(0, '/Users/jeremywheeler/Dropbox/Code/Projects/Debug')

# Now import and run the main app
import bugsnap_menubar
app = bugsnap_menubar.BugSnapApp()
app.run()