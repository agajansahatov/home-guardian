# Home Guardian - An IoT Smart Home Environmental Monitoring System

The "Home Guardian" project is an IoT-based smart home environmental monitoring system implemented using a Mini Practice Board, Python, Arduino, and the PyMata4Ex library. It allows users to monitor and control various environmental factors within their home, such as temperature, humidity, and air quality, to ensure a comfortable and safe living environment.
The project leverages the Arduino UNO microcontroller as its core to create an IoT-based smart home environmental monitoring system. It integrates various sensors to collect data on temperature, humidity, light levels, and proximity. This data is then processed by a Python script running on a computer, which communicates with the Arduino board via RS232 communication. 

## Overall Features

1. **Data Acquisition**: The system gathers data from sensors including temperature, humidity, light, and ultrasonic sensors connected to the Arduino UNO controller.

2. **Data Display**: Collected data is displayed in real-time on an LCD screen, providing users with insights into the environmental conditions within their home.

3. **Data Analysis**: The Python script analyzes the collected data to derive insights and make decisions based on predefined criteria.

4. **Control of External Devices**: Based on the data analysis results, the system controls various external function modules such as LED lights, DC motors, servo motors, buzzers, etc., to implement basic smart home functions.

## Current Version Features

The current version of the "Home Guardian" system offers the following functionalities:

- **Continuous Temperature Monitoring**: The system continuously monitors the temperature using a mini Arduino Practice Board.

- **Simulated Temperature Input**: Users can simulate temperature changes using the "Sliding Rheostat" connected to analog pin A2 on the board. This feature allows users to test and observe how the system responds to temperature fluctuations. After testing, users can switch to real-time temperature monitoring using the "Temperature and Humidity" sensor connected to digital pin 2 on the mini Practice Board.

- **Temperature-Based Control Logic**:
  - When the temperature is below 10 degrees Celsius, the RGB LEDs display a blue color. At this temperature range, both the fan and the fire alarm are turned off.
  - When the temperature is between 15 and 35 degrees Celsius, the RGB LEDs display a green color. The fan and fire alarm remain off.
  - When the temperature is between 35 and 60 degrees Celsius, the RGB LEDs display a red color, indicating increased temperature. Additionally, the fan starts operating to regulate the temperature. The fire alarm remains off.
  - If the temperature exceeds 60 degrees Celsius, the system activates the fire alarm sound, and the RGB LEDs alternate between red and yellow colors continuously until the temperature decreases below 60 degrees Celsius.
  - When the temperature drops below 60 degrees Celsius, the fire alarm stops sounding, but the fan continues to operate.
  - If the temperature drops below 35 degrees Celsius, the fan is turned off to prevent overcooling.
  
- **RGB LED Functionality**: The RGB LED lights operate at all temperature ranges and only change color based on the temperature reading.

These functionalities enable the "Home Guardian" system to effectively monitor environmental conditions and respond accordingly, ensuring a comfortable and safe living environment for users. Users can easily understand the system's behavior and make adjustments as needed to maintain optimal conditions within their home.



## Technologies Used

1. **Arduino Microcontroller Technology**: The Arduino UNO microcontroller serves as the central processing unit for the system, interfacing with sensors and external devices to collect data and execute control commands.

2. **Sensor Technology**: Various sensors including temperature sensors, humidity sensors, light sensors, and ultrasonic sensors are employed to gather environmental data.

3. **RS232 Communication Technology**: RS232 serial communication protocol is used for communication between the Arduino board and the computer running the Python script, enabling data transfer and command execution.

4. **Python Programming Technology**: Python programming language is used to develop the script responsible for data processing, analysis, and decision-making based on the collected sensor data.

5. **I2C Bus Technology**: The I2C (Inter-Integrated Circuit) bus protocol may be utilized for communication between certain sensors and the Arduino board, enabling efficient data exchange over short distances.

## Arduino Mini Practice Board Information

The Arduino Mini Practice Board provides a versatile platform for experimenting with various sensors, actuators, and electronic components. Here's an overview of its features and capabilities:

- **Analog Input**: Pins A0~A5 accept analog input values ranging from 0 to 1023, representing the intensity or level of the input signal.

- **Digital Input**: Digital pins 0-13 support digital input signals, with values of either 0 or 1. These pins are typically used to detect the presence or absence of an electrical signal.

- **Analog Output**: Pins 3, 5, 6, 9, 10, and 11 can be used for analog output, allowing control over the intensity or voltage level of the output signal. Output values range from 0 to 255.

- **Digital Output**: Digital pins 0-13 can also function as digital outputs. They can be set to either a high (1) or low (0) state to control the flow of electrical current.

- **Power Supply**: The board provides both +5V and +3.3V power supply pins, as well as GND pins for connecting to the positive and negative terminals of external components.

### Digital input/output pins

- **Hall Sensor / Servo Motor**: Pin 12 is commonly used for connecting a Hall sensor or servo motor.

- **8x8 Dot Matrix Display**: Pins 8, 11, and 13 can be used to interface with an 8x8 dot matrix display.

- **Ultrasonic Sensor**: Pins 7 (Trig) and 9 (Echo) are used to interface with an ultrasonic sensor for distance measurement.

- **RGB LED**: Pins 5 (Red), 6 (Green), and 10 (Blue) control the color and intensity of an RGB LED.

- **Buzzer**: Pin 4 can be connected to a buzzer for generating audible alerts or tones.

- **Fan Sensor**: Pin 3 can be used to control a fan or monitor its status.

- **DHT11 Sensor**: Pin 2 interfaces with a DHT11 temperature and humidity sensor for environmental monitoring.

- **Bluetooth Module**: Pins 0 (RX) and 1 (TX) are commonly used to interface with a Bluetooth module for wireless communication.

### Analog input pins

- **Light Sensor**: Analog pin AO can be connected to a light transmitter or photosensitive sensor for measuring ambient light levels.

- **Sound Sensor**: Analog pin A1 interfaces with a sound sensor for detecting acoustic signals.

- **Slide Potentiometer**: Analog pin A2 can be connected to a slide potentiometer or sliding rheostat for manual input control.

- **Infrared Receiver**: Analog pin A3 can receive signals from an infrared (IR) remote control.

- **LCD Display**: Analog pins A4 and A5 are typically used to interface with an LCD display for visual output.

The Arduino Mini Practice Board offers a wide range of input and output options, making it ideal for experimenting with various electronic projects and learning about sensors, actuators, and microcontroller programming.







## Installation Guide

Before getting started with the "Home Guardian" project, make sure you have the following prerequisites installed:

- Python (v3.12.3)
- PyCharm (v2024.1)
- Arduino IDE (v2.3.2)
- Connect Mini Practice Board.

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

1. Connect your Practice Board to your computer.
2. Open the Arduino, navigate to `File` > `Examples` > `Examples from Custom Libraries` > `FirmataExpress`. Select the board "Arduino Uno" and choose the appropriate port to which your Arduino board is connected. Click the upload button (->) to upload the FirmataExpress sketch to your Arduino board.
2. Open the project in PyCharm. 
3. Navigate to the `src` package. 
4. Run the `main.py` script to start the "Home Guardian" system. 
5. If you want the system work based on the real-time climate, then pass the climate_sensor to the home_guardian system like this - home_guardian.initialize(climate_sensor, "get_temperature"). 
6. If we want to simulate the system to check the system works or not, use the slider on the board, pass slide_potentiometer object and its read_value method to the home_guardian system like this - home_guardian.initialize(slide_potentiometer, "read_value").





## Implementation
The system is implemented using a combination of hardware and software components, including Arduino UNO boards, sensors, actuators, and a Python script. The Arduino board interfaces with sensors to collect environmental data, while the Python script processes this data and controls external devices based on predefined rules and conditions. The integration of various technologies enables the creation of a versatile and effective smart home environmental monitoring system.

### System Overview

The system utilizes the principles of object-oriented programming (OOP) and several design patterns to create an effective and flexible smart home environmental monitoring system. I have put the images of the working system and the UML diagram in the "internship" directory.

Here's an overview of how the system works:

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

## Collaborating
You can collaborate to this project if you want. Just contact me though email - agajan.st@gmail.com.