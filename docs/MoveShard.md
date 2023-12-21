# MoveShard


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**shard_id** | **int** |  | 
**to_peer_id** | **int** |  | 
**from_peer_id** | **int** |  | 
**method** | [**ShardTransferMethod**](ShardTransferMethod.md) |  | [optional] 

## Example

```python
from qdrant_openapi.models.move_shard import MoveShard

# TODO update the JSON string below
json = "{}"
# create an instance of MoveShard from a JSON string
move_shard_instance = MoveShard.from_json(json)
# print the JSON string representation of the object
print MoveShard.to_json()

# convert the object into a dict
move_shard_dict = move_shard_instance.to_dict()
# create an instance of MoveShard from a dict
move_shard_form_dict = move_shard.from_dict(move_shard_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


