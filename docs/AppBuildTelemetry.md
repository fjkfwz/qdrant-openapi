# AppBuildTelemetry


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**version** | **str** |  | 
**features** | [**AppFeaturesTelemetry**](AppFeaturesTelemetry.md) |  | [optional] 
**system** | [**RunningEnvironmentTelemetry**](RunningEnvironmentTelemetry.md) |  | [optional] 
**startup** | **datetime** |  | 

## Example

```python
from openapi_client.models.app_build_telemetry import AppBuildTelemetry

# TODO update the JSON string below
json = "{}"
# create an instance of AppBuildTelemetry from a JSON string
app_build_telemetry_instance = AppBuildTelemetry.from_json(json)
# print the JSON string representation of the object
print AppBuildTelemetry.to_json()

# convert the object into a dict
app_build_telemetry_dict = app_build_telemetry_instance.to_dict()
# create an instance of AppBuildTelemetry from a dict
app_build_telemetry_form_dict = app_build_telemetry.from_dict(app_build_telemetry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


