# LocalShardInfo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**shard_id** | **int** | Local shard id | 
**shard_key** | [**ShardKey**](ShardKey.md) |  | [optional] 
**points_count** | **int** | Number of points in the shard | 
**state** | [**ReplicaState**](ReplicaState.md) |  | 

## Example

```python
from qdrant_openapi.models.local_shard_info import LocalShardInfo

# TODO update the JSON string below
json = "{}"
# create an instance of LocalShardInfo from a JSON string
local_shard_info_instance = LocalShardInfo.from_json(json)
# print the JSON string representation of the object
print LocalShardInfo.to_json()

# convert the object into a dict
local_shard_info_dict = local_shard_info_instance.to_dict()
# create an instance of LocalShardInfo from a dict
local_shard_info_form_dict = local_shard_info.from_dict(local_shard_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


