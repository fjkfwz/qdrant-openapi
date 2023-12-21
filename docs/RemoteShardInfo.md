# RemoteShardInfo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**shard_id** | **int** | Remote shard id | 
**shard_key** | [**ShardKey**](ShardKey.md) |  | [optional] 
**peer_id** | **int** | Remote peer id | 
**state** | [**ReplicaState**](ReplicaState.md) |  | 

## Example

```python
from openapi_client.models.remote_shard_info import RemoteShardInfo

# TODO update the JSON string below
json = "{}"
# create an instance of RemoteShardInfo from a JSON string
remote_shard_info_instance = RemoteShardInfo.from_json(json)
# print the JSON string representation of the object
print RemoteShardInfo.to_json()

# convert the object into a dict
remote_shard_info_dict = remote_shard_info_instance.to_dict()
# create an instance of RemoteShardInfo from a dict
remote_shard_info_form_dict = remote_shard_info.from_dict(remote_shard_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


