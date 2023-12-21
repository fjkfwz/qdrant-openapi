# CollectionTelemetry


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**init_time_ms** | **int** |  | 
**config** | [**CollectionConfig**](CollectionConfig.md) |  | 
**shards** | [**List[ReplicaSetTelemetry]**](ReplicaSetTelemetry.md) |  | 
**transfers** | [**List[ShardTransferInfo]**](ShardTransferInfo.md) |  | 

## Example

```python
from openapi_client.models.collection_telemetry import CollectionTelemetry

# TODO update the JSON string below
json = "{}"
# create an instance of CollectionTelemetry from a JSON string
collection_telemetry_instance = CollectionTelemetry.from_json(json)
# print the JSON string representation of the object
print CollectionTelemetry.to_json()

# convert the object into a dict
collection_telemetry_dict = collection_telemetry_instance.to_dict()
# create an instance of CollectionTelemetry from a dict
collection_telemetry_form_dict = collection_telemetry.from_dict(collection_telemetry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


