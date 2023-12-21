# RequestsTelemetry


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rest** | [**WebApiTelemetry**](WebApiTelemetry.md) |  | 
**grpc** | [**GrpcTelemetry**](GrpcTelemetry.md) |  | 

## Example

```python
from qdrant_openapi.models.requests_telemetry import RequestsTelemetry

# TODO update the JSON string below
json = "{}"
# create an instance of RequestsTelemetry from a JSON string
requests_telemetry_instance = RequestsTelemetry.from_json(json)
# print the JSON string representation of the object
print RequestsTelemetry.to_json()

# convert the object into a dict
requests_telemetry_dict = requests_telemetry_instance.to_dict()
# create an instance of RequestsTelemetry from a dict
requests_telemetry_form_dict = requests_telemetry.from_dict(requests_telemetry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


