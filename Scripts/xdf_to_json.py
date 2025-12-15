import pyxdf
import json
 
# 1. Load XDF file
data, header = pyxdf.load_xdf('sub-P001_ses-S001_task-Default_run-001_eeg.xdf')
 
# 2. Prepare structured dictionary
output = {
    "version": "1.0",
    "datetime": "",
    "time_units": "seconds",
    "streams": [],
}
 
# 3. Loop through streams
for stream in data:
    stream_info = {
    "name": stream['info']['name'][0] if 'name' in stream['info'] else "Unnamed",
    "type": stream['info'].get('type', [""])[0],
    "units": "microsiemens",
    "channel_count": int(stream['info'].get('channel_count', [1])[0]),
    "nominal_srate": float(stream['info'].get('nominal_srate', [0])[0]),
    "time_stamps": stream['time_stamps'].tolist(),
}
    # Convert time series depending on type
    y = stream['time_series']
 
    # Case 1: numeric array
    if isinstance(y, (list, tuple)):
        stream_info["time_series"] = y
    elif hasattr(y, "tolist"):
        stream_info["time_series"] = y.tolist()
    else:
        stream_info["time_series"] = str(y)
 
    output["streams"].append(stream_info)
 
# 4. Save as JSON
with open("test_unreal.json", "w", encoding="utf-8") as f:
    json.dump(output, f, indent=2)
 
print("Exported to test.json")