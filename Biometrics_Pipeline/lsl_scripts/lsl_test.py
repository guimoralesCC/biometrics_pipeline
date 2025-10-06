
# import LSL Python interface
# StreamInlet(reads data from stream)
# resolve_byprop (finds stream that matchs given property like "name")
from pylsl import StreamInlet, resolve_byprop
import json, time

### Finding LSL Stream ###

print("Looking for LSL stream 'lsl_markers_guru' ...")

# Find stream(s) with name 'lsl_markers_guru", wait 5s for response
streams = resolve_byprop('name', 'lsl_markers_guru', timeout=5.0)

####  Stream Connection  ###

if not streams:
    print("No stream found")
else:
    print("Stream found!")
    # Create StreamInlet object to open a live connection to the first matching stream, 0
    inlet = StreamInlet(streams[0])
    # Show 5 samples 
    print("Connected — showing 5 samples:\n")

    for i in range(5):
        # pulls sample data, waits 2s for a new sample
        sample, timestamp = inlet.pull_sample(timeout=2.0)
        # Return sample data and print or no data
        if sample:
         print(f"{i+1}) t={timestamp:.3f}  sample={sample}")
        else:
         print(f"{i+1}) timeout — no data.")

####  JSON logging  ###

# Open and create json file named mindtooth_data for writing
# "w" overwrites every time script is run, use 'a' to append
with open("mindtooth_data.json", "w", encoding="utf-8") as f:

    # Continuous loop to record incoming samples 
    while True:
        # Get next sample
        # ts means timestamp (seconds -float)

        # If no sample continue
        sample, ts = inlet.pull_sample(timeout=2.0)
        if not sample:
           continue
        
        # Save mindtooth data as json strings into a list
        data =json.loads(sample[0])
        
        # Add two types of timestamps in json file, ts and unix time
        # unix time is current system time
        data["lsl_time"]=ts
        data["unix_time"] = time.time()

        # Convert dictionary/list line to json string and add to file
        f.write(json.dumps(data) + "\n")

        # Print data onto console to watch live
        print(data)