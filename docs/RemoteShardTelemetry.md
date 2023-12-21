# RemoteShardTelemetry


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**shard_id** | **int** |  | 
**peer_id** | **int** |  | [optional] 
**searches** | [**OperationDurationStatistics**](OperationDurationStatistics.md) |  | 
**updates** | [**OperationDurationStatistics**](OperationDurationStatistics.md) |  | 

## Example

```python
from qdrant_openapi.models.remote_shard_telemetry import RemoteShardTelemetry

# TODO update the JSON string below
json = "{}"
# create an instance of RemoteShardTelemetry from a JSON string
remote_shard_telemetry_instance = RemoteShardTelemetry.from_json(json)
# print the JSON string representation of the object
print RemoteShardTelemetry.to_json()

# convert the object into a dict
remote_shard_telemetry_dict = remote_shard_telemetry_instance.to_dict()
# create an instance of RemoteShardTelemetry from a dict
remote_shard_telemetry_form_dict = remote_shard_telemetry.from_dict(remote_shard_telemetry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


