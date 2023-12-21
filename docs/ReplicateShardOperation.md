# ReplicateShardOperation


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**replicate_shard** | [**MoveShard**](MoveShard.md) |  | 

## Example

```python
from qdrant_openapi.models.replicate_shard_operation import ReplicateShardOperation

# TODO update the JSON string below
json = "{}"
# create an instance of ReplicateShardOperation from a JSON string
replicate_shard_operation_instance = ReplicateShardOperation.from_json(json)
# print the JSON string representation of the object
print ReplicateShardOperation.to_json()

# convert the object into a dict
replicate_shard_operation_dict = replicate_shard_operation_instance.to_dict()
# create an instance of ReplicateShardOperation from a dict
replicate_shard_operation_form_dict = replicate_shard_operation.from_dict(replicate_shard_operation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


