import pyxdf
import json
 
# 1. Load XDF file
data, header = pyxdf.load_xdf('test_unreal.xdf')
 
# 2. Prepare structured dictionary
output = {
    "header": header,
    "streams": []
}
 
# 3. Loop through streams
for stream in data:
    stream_info = {
        "name": stream['info']['name'][0] if 'name' in stream['info'] else "Unnamed",
        "type": stream['info'].get('type', [""])[0],
        "channel_count": stream['info'].get('channel_count', [""])[0],
        "nominal_srate": stream['info'].get('nominal_srate', [""])[0],
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
 
print("Exported to test_unreal.json")