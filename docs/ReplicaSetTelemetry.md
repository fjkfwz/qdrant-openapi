# ReplicaSetTelemetry


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**local** | [**LocalShardTelemetry**](LocalShardTelemetry.md) |  | [optional] 
**remote** | [**List[RemoteShardTelemetry]**](RemoteShardTelemetry.md) |  | 
**replicate_states** | [**Dict[str, ReplicaState]**](ReplicaState.md) |  | 

## Example

```python
from qdrant_openapi.models.replica_set_telemetry import ReplicaSetTelemetry

# TODO update the JSON string below
json = "{}"
# create an instance of ReplicaSetTelemetry from a JSON string
replica_set_telemetry_instance = ReplicaSetTelemetry.from_json(json)
# print the JSON string representation of the object
print ReplicaSetTelemetry.to_json()

# convert the object into a dict
replica_set_telemetry_dict = replica_set_telemetry_instance.to_dict()
# create an instance of ReplicaSetTelemetry from a dict
replica_set_telemetry_form_dict = replica_set_telemetry.from_dict(replica_set_telemetry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


