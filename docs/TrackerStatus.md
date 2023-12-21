# TrackerStatus

Represents the current state of the optimizer being tracked

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cancelled** | **str** |  | 
**error** | **str** |  | 

## Example

```python
from openapi_client.models.tracker_status import TrackerStatus

# TODO update the JSON string below
json = "{}"
# create an instance of TrackerStatus from a JSON string
tracker_status_instance = TrackerStatus.from_json(json)
# print the JSON string representation of the object
print TrackerStatus.to_json()

# convert the object into a dict
tracker_status_dict = tracker_status_instance.to_dict()
# create an instance of TrackerStatus from a dict
tracker_status_form_dict = tracker_status.from_dict(tracker_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


