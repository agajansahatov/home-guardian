# Home Guardian - An IoT Smart Home Environmental Monitoring System

The "Home Guardian" project is an IoT-based smart home environmental monitoring system implemented using Python, Arduino, and the PyMata4Ex library. It allows users to monitor and control various environmental factors within their home, such as temperature, humidity, and air quality, to ensure a comfortable and safe living environment.

## Installation Guide

Before getting started with the "Home Guardian" project, make sure you have the following prerequisites installed:

- Python (v3.12.3)
- PyCharm (v2024.1)
- Arduino IDE (v2.3.2)

### PyMata4Ex Library Setup

1. Navigate to the following directory: `C:\Users\your-user-name\AppData\Local\Programs\Python\Python312\Lib\site-packages`.
2. If the file `pymata4EX-0.1-py3.12.egg` exists, delete it.
3. If the file does not exist, skip this step.

### Arduino Setup

1. Open the Arduino IDE.
2. Go to `Tools` > `Manage Libraries` (shortcut: `Ctrl+Shift+I`).
3. In the Library Manager, search for "FirmataExpress" and install version `1.1.0`.

### Project Setup

1. Clone the project repository into your desired folder.
2. Open a command prompt (cmd) and navigate to the project directory.
3. Run the command `python setup.py install` to install the required dependencies.

## Running the Project

1. Open the Arduino, navigate to `File` > `Examples` > `Examples from Custom Libraries` > `FirmataExpress`. Select the board "Arduino Uno" and choose the appropriate port to which your Arduino board is connected. Click the upload button (->) to upload the FirmataExpress sketch to your Arduino board.
2. Open the project in PyCharm. 
3. Navigate to the `src` package. 
4. Run the `main.py` script to start the "Home Guardian" system. 
5. If you want the system work based on the real-time climate, then pass the climate_sensor to the home_guardian system like this - home_guardian.initialize(climate_sensor, "get_temperature"). 
6. If we want to simulate the system to check the system works or not, use the slider on the board, pass slide_potentiometer object and its read_value method to the home_guardian system like this - home_guardian.initialize(slide_potentiometer, "read_value").

Sure, here's an addition to your README.md explaining how the system works:

## System Overview

The "Home Guardian" system utilizes the principles of object-oriented programming (OOP) and several design patterns to create an effective and flexible smart home environmental monitoring system. I have put the images of the working system and the UML diagram in the "results" folder. Here's an overview of how the system works:

### Object-Oriented Design

The system is designed using OOP principles, with each component represented as a separate class. These classes encapsulate the behavior and state of individual components, making the system modular and easy to maintain.

### Design Patterns

#### Observer Pattern

The system employs the Observer pattern to monitor changes in environmental factors such as temperature, humidity, and air quality. The `HomeGuardian` class acts as the observer, while the `ClimateSensor` and `SlidePotentiometer` classes serve as the subjects. When the state of a subject changes, it notifies the observer, allowing the system to react accordingly.

#### Strategy Pattern

The Strategy pattern is used to handle different input sources for the system. The `HomeGuardian` class defines a method `initialize`, which accepts an object and a method name as parameters. This allows the system to dynamically switch between different input sources, such as real-time sensor data or simulated input from a slider.

### System Workflow

1. Initialization: The system is initialized by creating instances of various components, including the `Display`, `Fan`, `FireAlarm`, `LightBulb`, and input sources such as the `ClimateSensor` and `SlidePotentiometer`.

2. Input Handling: The `HomeGuardian` class handles input from the selected source (e.g., temperature sensor or slider). If real-time sensor data is used, the system continuously monitors changes in environmental factors. If simulated input is used, the system periodically reads input from the slider.

3. State Monitoring: As changes in environmental factors are detected, the `HomeGuardian` class updates the system's state and determines the appropriate actions to take. This may include adjusting the fan speed, changing the color of the light bulb, or activating the fire alarm in case of emergency.

4. User Interaction: The system provides feedback to the user through the display, indicating the current status of environmental factors and any actions being taken. Users can also interact with the system by adjusting settings or input parameters.

By combining object-oriented design principles with design patterns such as Observer and Strategy, the "Home Guardian" system provides a robust and adaptable solution for smart home environmental monitoring.

### Collaborating
You can collaborate to this project if you want. Just contact me though email - agajan.st@gmail.com.