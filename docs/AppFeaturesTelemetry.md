# AppFeaturesTelemetry


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**debug** | **bool** |  | 
**web_feature** | **bool** |  | 
**service_debug_feature** | **bool** |  | 
**recovery_mode** | **bool** |  | 

## Example

```python
from qdrant_openapi.models.app_features_telemetry import AppFeaturesTelemetry

# TODO update the JSON string below
json = "{}"
# create an instance of AppFeaturesTelemetry from a JSON string
app_features_telemetry_instance = AppFeaturesTelemetry.from_json(json)
# print the JSON string representation of the object
print AppFeaturesTelemetry.to_json()

# convert the object into a dict
app_features_telemetry_dict = app_features_telemetry_instance.to_dict()
# create an instance of AppFeaturesTelemetry from a dict
app_features_telemetry_form_dict = app_features_telemetry.from_dict(app_features_telemetry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


