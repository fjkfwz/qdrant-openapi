# ShardSnapshotRecover


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**location** | [**ShardSnapshotLocation**](ShardSnapshotLocation.md) |  | 
**priority** | [**SnapshotPriority**](SnapshotPriority.md) |  | [optional] 

## Example

```python
from openapi_client.models.shard_snapshot_recover import ShardSnapshotRecover

# TODO update the JSON string below
json = "{}"
# create an instance of ShardSnapshotRecover from a JSON string
shard_snapshot_recover_instance = ShardSnapshotRecover.from_json(json)
# print the JSON string representation of the object
print ShardSnapshotRecover.to_json()

# convert the object into a dict
shard_snapshot_recover_dict = shard_snapshot_recover_instance.to_dict()
# create an instance of ShardSnapshotRecover from a dict
shard_snapshot_recover_form_dict = shard_snapshot_recover.from_dict(shard_snapshot_recover_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


