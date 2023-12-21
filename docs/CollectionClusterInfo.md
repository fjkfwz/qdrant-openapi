# CollectionClusterInfo

Current clustering distribution for the collection

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**peer_id** | **int** | ID of this peer | 
**shard_count** | **int** | Total number of shards | 
**local_shards** | [**List[LocalShardInfo]**](LocalShardInfo.md) | Local shards | 
**remote_shards** | [**List[RemoteShardInfo]**](RemoteShardInfo.md) | Remote shards | 
**shard_transfers** | [**List[ShardTransferInfo]**](ShardTransferInfo.md) | Shard transfers | 

## Example

```python
from openapi_client.models.collection_cluster_info import CollectionClusterInfo

# TODO update the JSON string below
json = "{}"
# create an instance of CollectionClusterInfo from a JSON string
collection_cluster_info_instance = CollectionClusterInfo.from_json(json)
# print the JSON string representation of the object
print CollectionClusterInfo.to_json()

# convert the object into a dict
collection_cluster_info_dict = collection_cluster_info_instance.to_dict()
# create an instance of CollectionClusterInfo from a dict
collection_cluster_info_form_dict = collection_cluster_info.from_dict(collection_cluster_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


