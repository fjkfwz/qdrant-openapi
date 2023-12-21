# TrackerTelemetry

Tracker object used in telemetry

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the optimizer | 
**segment_ids** | **List[int]** | Segment IDs being optimized | 
**status** | [**TrackerStatus**](TrackerStatus.md) |  | 
**start_at** | **datetime** | Start time of the optimizer | 
**end_at** | **datetime** | End time of the optimizer | [optional] 

## Example

```python
from qdrant_openapi.models.tracker_telemetry import TrackerTelemetry

# TODO update the JSON string below
json = "{}"
# create an instance of TrackerTelemetry from a JSON string
tracker_telemetry_instance = TrackerTelemetry.from_json(json)
# print the JSON string representation of the object
print TrackerTelemetry.to_json()

# convert the object into a dict
tracker_telemetry_dict = tracker_telemetry_instance.to_dict()
# create an instance of TrackerTelemetry from a dict
tracker_telemetry_form_dict = tracker_telemetry.from_dict(tracker_telemetry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


