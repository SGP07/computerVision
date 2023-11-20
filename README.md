# Hand Gesture Control

## Overview
This project utilizes computer vision to interpret hand gestures and perform actions on a computer. Two separate scripts are provided: one for controlling system volume based on hand gestures, and another for controlling the mouse cursor and interacting with the screen.

## Features

### Hand Gesture Volume Control
- Adjusts system volume based on the distance between the thumb and index finger.
- Provides visual feedback on the screen.
- Uses the HandTracking module for hand detection and tracking.

### Hand Gesture Mouse Control
- Controls the mouse cursor using hand gestures.
- Allows left-click, right-click, and movement actions.
- Utilizes the HandTracking module for hand detection and tracking.

## Setup

### Requirements
- Python 3.x
- OpenCV
- NumPy
- PyAutoGUI

### Installation
1. Install the required packages:
   ```bash
   pip install opencv-python numpy pyautogui
   ```

  ## Usage

### Hand Gesture Volume Control
1. Run the `hand_volume_control.py` script.
2. Adjust the system volume by bringing the thumb and index finger closer or farther apart.
3. Visual feedback on the screen indicates the current volume level.

### Hand Gesture Mouse Control
1. Run the `hand_mouse_control.py` script.
2. Control the mouse cursor using hand gestures:
   - Move the index finger to move the cursor.
   - Close the thumb and index finger to left-click.
   - Raise the pinky to right-click.


