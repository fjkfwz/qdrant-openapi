# CollectionTelemetryEnum


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**init_time_ms** | **int** |  | 
**config** | [**CollectionConfig**](CollectionConfig.md) |  | 
**shards** | [**List[ReplicaSetTelemetry]**](ReplicaSetTelemetry.md) |  | 
**transfers** | [**List[ShardTransferInfo]**](ShardTransferInfo.md) |  | 
**vectors** | **int** |  | 
**optimizers_status** | [**OptimizersStatus**](OptimizersStatus.md) |  | 
**params** | [**CollectionParams**](CollectionParams.md) |  | 

## Example

```python
from openapi_client.models.collection_telemetry_enum import CollectionTelemetryEnum

# TODO update the JSON string below
json = "{}"
# create an instance of CollectionTelemetryEnum from a JSON string
collection_telemetry_enum_instance = CollectionTelemetryEnum.from_json(json)
# print the JSON string representation of the object
print CollectionTelemetryEnum.to_json()

# convert the object into a dict
collection_telemetry_enum_dict = collection_telemetry_enum_instance.to_dict()
# create an instance of CollectionTelemetryEnum from a dict
collection_telemetry_enum_form_dict = collection_telemetry_enum.from_dict(collection_telemetry_enum_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


