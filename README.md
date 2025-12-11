# biometrics_pipeline
Technical Report: VR Biometrics Pipeline
Author: Guillermo Morales
Course: CS406 — Honors Thesis / Independent Research
University: Oregon State University
Date: December 2025

1. Introduction
This project intergrates multimodal biosignals into an immersive virtual reality (VR) environment running on the Meta Quest 3. The system captures and synchronizes real-time EEG and physiological data streams while the user performs interactive tasks in Unreal Engine 5.4.
The primary objectives of this project were:
1.	Build and deploy an Unreal Engine VR application to the Quest 3 with interaction logging.
2.	Integrate Mindtooth EEG and EmotiBit physiological sensors through the LabStreamingLayer (LSL).
3.	Synchronize biosignals and VR interactions using a unified JSON schema.
4.	Collect at least one complete labeled dataset.
5.	Measure system reliability based on latency, packet loss, and timing accuracy.
6.	Document the system and prepare a reproducible workflow for further research
2. System Architecture
2.1 Hardware Setup
•	Meta Quest 2 (standalone)
o	Runs a packaged Unreal Engine app in Android ASTC build
•	Mindtooth Smartband (EEG)
o	8 channels 
o	Raw EEG data
•	EmotiBit Biometric Module
o	EDA, ECG, temperature, accelerometer, etc
•	Laptop
o	Runs LabRecorder for multi-stream synchronization
o	Used for analysis and tethered debugging
•	XRLab – Private Wi-Fi Router
o	Ensures low-latency network communication for LSL between Quest and PC


2.2 Software Pipeline Overview
The complete system consists of five coordinated components:
1.	Quest 2 Unreal App
o	Interaction logic
o	Event logging
o	Ghost cues and 3D assembly tasks
2.	Custom LSL Integration (Unreal C++)
o	Publishes interaction markers
o	Saves side-car JSON logs to the Quest filesystem
o	Can subscribe to remote LSL streams if needed
3.	Biosignal Ingestion (Python)
o	Mindtooth + EmotiBit SDKs
o	Emit structured JSON samples through LSL outlets
4.	LabRecorder (PC)
o	Collects all streams
o	Produces synced .xdf datasets
5.	Data Processing & Visualization (Python)
o	Converts .xdf → JSON/CSV
o	Checks synchronization
o	Plots EEG/physio vs interactions
o	Computes latency and packet loss
This modular pipeline allows each subsystem to evolve independently while maintaining timing integrity through LSL’s shared clock.
