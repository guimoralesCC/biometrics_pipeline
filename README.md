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

3. Unreal Quest 3 Application Framework 

The VR application was built in Unreal Engine 5.4 and successfully deployed to the Meta Quest 3 as a standalone Android build. Key features include: 

3.1 Interaction Model 

Grabbing, releasing, and placing objects 

Hand-tracking-based interactions (OculusXR plugin) 

3.2 Interaction Logging 

Every significant action is logged with both Unreal time and LSL time: 

{"event":"grab",} 

These logs support later alignment with EEG and physiological events. 

Shape 

4. Biosignal Data Integration 

4.1 EEG Stream (Mindtooth) 

The pipeline: 

Mindtooth → BrainFlow → Python → LSL Outlet → LabRecorder 

Key properties: 

8 EEG channels 

<1 % packet loss during 3+ minute sessions 

Tests confirmed stable numerical output, clean signal structure, and valid timestamps. 

Shape 

4.2 EmotiBit Stream 

EmotiBit data includes: 

Electrodermal activity (EDA) 

ECG 

Temperature 

Accelerometer/gyroscope 

Data is parsed and broadcast via Python as an LSL outlet containing structured JSON. 
Real-time streaming and graphical checks confirmed consistent sampling. 

Shape 

4.3 Multi-Stream Synchronization Mechanism 

LabRecorder automatically maintains a shared timebase. 
This allowed EEG, ECG, EDA, accelerometer, and VR events to occupy the same global timeline without manual offsetting. 

Shape 

5. JSON Schema and Data Synchronization 

A unified dictionary format was developed to standardize all incoming samples: 

{ 

  "device": "Mindtooth", 

} 

VR interaction events follow a nearly identical structure, allowing seamless merging inside Python. 

5.1 Alignment Results

Used performance.py 
System performance was evaluated by examining the timing of recorded samples. For each continuous stream, we measured the time difference between consecutive timestamps to check whether samples arrived at regular intervals. These measured intervals closely matched the expected sampling periods, with very little variation and no detected dropouts, indicating stable and reliable data collection.

To evaluate synchronization, we compared the timestamps of Unreal interaction events with the nearest biosignal samples and measured the time difference between them. The average and maximum alignment errors were small and consistent with the biosignal sampling rate, showing that interaction events and physiological signals were well synchronized within the limits of the sampling resolution.

Shape 

6. Pilot Dataset Collection 

Shape 

7. System Performance Evaluation
   System performance was evaluated by examining the timing of recorded samples. For each continuous stream, we measured the time difference between consecutive timestamps to check    whether samples arrived at regular intervals. These measured intervals closely matched the expected sampling periods, with very little variation and no detected dropouts, indicating stable and reliable data collection.

To evaluate synchronization, we compared the timestamps of Unreal interaction events with the nearest biosignal samples and measured the time difference between them. The average and maximum alignment errors were small and consistent with the biosignal sampling rate, showing that interaction events and physiological signals were well synchronized within the limits of the sampling resolution.


7.1 Measurement Framework 

Three metrics were analyzed: 

End-to-End Latency 
Time from VR action  recorded biosignal marker. 

Example of perfomance anaylized 

=== Reliability (continuous streams) ===
EDA: 15.0 Hz, n=893, dt_mean=0.066660s (expected 0.066667s), jitter_std=2.00e-10s, dropouts=0
PPG_RED: 25.0 Hz, n=1486, dt_mean=0.040081s (expected 0.040000s), jitter_std=1.47e-10s, dropouts=0
102808-1051_eeg: 125.0 Hz, n=7440, dt_mean=0.008000s (expected 0.008000s), jitter_std=1.77e-10s, dropouts=0

=== Event streams (informational) ===
Unreal_LSL_GreenShape_Logger: n=5, avg gap=10.209s, max gap varies (event-based)
Unreal_LSL_BlueShape_Logger: n=3, avg gap=20.680s, max gap varies (event-based)
Unreal_LSL_GazeHit_Logger: n=1660, avg gap=0.028s, max gap varies (event-based)
HR: n=56, avg gap=1.033s, max gap varies (event-based)
102808-1051_bat: n=5, avg gap=10.170s, max gap varies (event-based)
Unreal_LSL_RedShape_Logger: n=6, avg gap=8.282s, max gap varies (event-based)

=== Sync Accuracy (Marker ↔ Bio) ===
marker: Unreal_LSL_GazeHit_Logger
bio:    EDA
events: 1660
mean |Δt|: 0.016655s
max  |Δt|: 0.033310s

7.2 Data Collection Method 

Quest app logs events to LSL + local JSON 

Mindtooth and EmotiBit stream to LSL 

LabRecorder collects all 

Python scripts compute metrics from the .xdf dump 

7.3 Results 

7.4 Analysis 

Shape 

8. Documentation and Dissemination 

A structured public GitHub repository includes: 

Source code for the Unreal Quest application 

LSL plugin code for Android and desktop 

Python scripts for EEG/physio acquisition 

JSON schemas and dataset examples 

Setup instructions 

Development logs and weekly updates 

A demo video will showcase: 

Real-time biosignal capture 

Interaction logging 

The VR task experience 

Synchronization results 

This repository forms the foundation for future replication and expansion of the system. 

Shape 

9. Research Practices and Data Ethics 

All datasets are pseudonymized using session IDs. 
No personally identifying information is stored. 
Sensors are handled safely using IRB-aligned practices for pilot physiological data. 
Regular communication, weekly check-ins, and responsible documentation demonstrate strong professionalism throughout the project cycle. 

Shape 

10. Conclusion and Future Directions 

This project demonstrates a fully operational XR biosensing system on the Meta Quest 3 capable of real-time EEG and physiological integration with synchronized VR interactions. 
The system is flexible, extensible, and suitable for cognitive research, attention modeling, and experimental human-computer interaction studies. 

Future directions include: 

Real-time cognitive state estimation 

Adaptive VR environments based on biosignal feedback 

More robust Android-native LSL recorders 

Integration with AR components in Fresh++ and Mad Vision research 

Additional datasets from multiple participants 

Advanced machine learning models for workload and engagement prediction 

The work represents a major step in building augmentation interfaces that empower users with real-time self-awareness inside immersive environments. 

Shape 

References 

