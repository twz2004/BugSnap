#!/usr/bin/env python3
import os
import sys
import subprocess
import rumps

class BugSnapApp(rumps.App):
    def __init__(self):
        icon_path = "/Users/jeremywheeler/Dropbox/Code/Projects/Debug/bug.png"
        super(BugSnapApp, self).__init__(name="BugSnap", icon=icon_path, quit_button=None)
        self.menu = ["Take Screenshot", None, "Quit"]
        
    @rumps.clicked("Take Screenshot")
    def take_screenshot(self, _):
        target_dir = '/Users/jeremywheeler/Dropbox/Code/Projects/_ExamCatalyst/ExamCatalyst_v2'
        target_file = 'debug-snap.jpg'
        target_path = os.path.join(target_dir, target_file)
        clipboard_text = "Please analyze 'debug-snap.jpg', which is a screenshot I just took. Focus specifically on the following: "
        
        try:
            os.makedirs(target_dir, exist_ok=True)
            # Interactive capture with JPG format
            result = subprocess.run(['screencapture', '-i', '-t', 'jpg', target_path], capture_output=True)
            
            if result.returncode == 0 and os.path.exists(target_path) and os.path.getsize(target_path) > 0:
                subprocess.run(['pbcopy'], input=clipboard_text, text=True)
                rumps.notification('Screenshot Saved', 'debug-snap.jpg saved', 'Text copied to clipboard')
            else:
                if os.path.exists(target_path):
                    os.unlink(target_path)
                rumps.notification('Screenshot Cancelled', 'No screenshot taken', '')
        except Exception as e:
            rumps.notification('Screenshot Error', str(e), '')

    @rumps.clicked("Quit")
    def quit_app(self, _):
        rumps.quit_application()

if __name__ == '__main__':
    app = BugSnapApp()
    app.run()