# GrpcTelemetry


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**responses** | [**Dict[str, OperationDurationStatistics]**](OperationDurationStatistics.md) |  | 

## Example

```python
from openapi_client.models.grpc_telemetry import GrpcTelemetry

# TODO update the JSON string below
json = "{}"
# create an instance of GrpcTelemetry from a JSON string
grpc_telemetry_instance = GrpcTelemetry.from_json(json)
# print the JSON string representation of the object
print GrpcTelemetry.to_json()

# convert the object into a dict
grpc_telemetry_dict = grpc_telemetry_instance.to_dict()
# create an instance of GrpcTelemetry from a dict
grpc_telemetry_form_dict = grpc_telemetry.from_dict(grpc_telemetry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


