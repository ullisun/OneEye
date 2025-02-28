## OneEye - Autonomous Mini-Robot

Overview
OneEye is a small, autonomous robot equipped with a Raspberry Pi Zero 2W, a PiCamera, and a ToF sensor for navigation. It is designed to detect its environment based on color recognition and adjust its movement accordingly. This project is part of an experiment to enhance object detection using OpenCV and adaptive lighting conditions.
# Features

Real-time Color Recognition: Detects the surface color using OpenCV.
Adaptive Navigation: Avoids leaving a predefined area based on color analysis.
Independent Lighting System: Uses an onboard LED strip to illuminate the surface in low-light conditions.
Remote Processing: Streams video data to a computer for analysis and receives movement commands.
System Components

Hardware:
Raspberry Pi Zero 2W
PiCamera
ToF Sensor
LED Strip for illumination
Motorized chassis
Software:
OpenCV for image processing
Python for control scripts
MPEG streaming for remote processing

Color Detection & Challenges
OneEye relies on HSV color detection to determine the surface it is driving on. Various light sources can significantly impact color readings, making it essential to calibrate at the start of each session.

Key Findings from Color Experiments
Color perception changes drastically under different light sources.

LED lights can heavily distort color recognition.
Green and white surfaces are most affected by lighting variations.
Red surfaces remain relatively stable in different lighting conditions.
Black surfaces produce extreme variations due to low reflectivity.

Surface Color

H Value (Artificial Light)

H Value (LED Light)

Distortion %

Green

81

36

~50%

Red

120

141

~18%

White

31

15

~50%

Black

97

21

Extreme

Next Steps

Test under natural daylight to compare results.

Implement automatic color calibration at startup.

Improve lighting conditions to reduce distortions.

Expand to outdoor environments with varying surface textures.

Contributions

Feel free to contribute to this project by testing different lighting conditions, optimizing the color recognition algorithm, or proposing new navigation strategies. Pull requests are welcome!

Contact

For more details or to discuss the project, feel free to reach out via GitHub or social media.

"A mistake should only be made once – because we learn from it." 🚀

