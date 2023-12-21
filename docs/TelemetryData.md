# TelemetryData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**app** | [**AppBuildTelemetry**](AppBuildTelemetry.md) |  | 
**collections** | [**CollectionsTelemetry**](CollectionsTelemetry.md) |  | 
**cluster** | [**ClusterTelemetry**](ClusterTelemetry.md) |  | 
**requests** | [**RequestsTelemetry**](RequestsTelemetry.md) |  | 

## Example

```python
from openapi_client.models.telemetry_data import TelemetryData

# TODO update the JSON string below
json = "{}"
# create an instance of TelemetryData from a JSON string
telemetry_data_instance = TelemetryData.from_json(json)
# print the JSON string representation of the object
print TelemetryData.to_json()

# convert the object into a dict
telemetry_data_dict = telemetry_data_instance.to_dict()
# create an instance of TelemetryData from a dict
telemetry_data_form_dict = telemetry_data.from_dict(telemetry_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


