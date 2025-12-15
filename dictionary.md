# Data Dictionary

## Top-level Fields

### `version`

* **Type:** string
* **Description:** Version identifier for the JSON export format.
* **Example:** `"1.0"`

### `datetime`

* **Type:** string
* **Description:** Timestamp indicating when the JSON file was generated.
* **Example:** `"2025-11-23T22:25:41-0800"`

### `time_units`

* **Type:** string
* **Description:** Units used for all timestamps in the file.
* **Allowed value:** `"seconds"`

---

## `streams` (array)

Each element in `streams` represents either a **continuous biosignal stream** or an **event-based marker stream**.

---

## Stream-Level Fields

### `streams[i].name`

* **Type:** string
* **Description:** Human-readable name of the stream.
* **Examples:** `"EDA"`, `"Unreal_LSL_GazeHit_Logger"`

### `streams[i].type`

* **Type:** string
* **Description:** Stream modality or source type.
* **Examples:** `"EDA"`, `"Markers4"`

### `streams[i].units`

* **Type:** string
* **Description:** Measurement units of the stream values.
* **Examples:**

  * `"microsiemens"` (EDA)
  * `"n/a"` (event-based marker streams)

### `streams[i].channel_count`

* **Type:** integer
* **Description:** Number of channels per sample.
* **Example:** `1`

### `streams[i].nominal_srate`

* **Type:** number
* **Units:** Hz
* **Description:** Nominal sampling rate of the stream.

  * Values greater than `0` indicate continuous sampling.
  * A value of `0.0` indicates an event-based stream.

### `streams[i].time_stamps`

* **Type:** array of numbers
* **Units:** seconds
* **Description:** Timestamp for each sample or event in the stream.

### `streams[i].time_series`

* **Type:** array of arrays
* **Description:** Data samples aligned with `time_stamps`.

  * For continuous streams, entries contain numeric values.
  * For event-based streams, entries contain string markers.

---

## Summary

Data are stored as time-aligned streams, where continuous biosignals use numeric samples and discrete interaction markers are represented as event-based streams with a nominal sampling rate of 0 Hz.

