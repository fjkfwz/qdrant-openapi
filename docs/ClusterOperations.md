# ClusterOperations


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**move_shard** | [**MoveShard**](MoveShard.md) |  | 
**replicate_shard** | [**MoveShard**](MoveShard.md) |  | 
**abort_transfer** | [**MoveShard**](MoveShard.md) |  | 
**drop_replica** | [**Replica**](Replica.md) |  | 
**create_sharding_key** | [**CreateShardingKey**](CreateShardingKey.md) |  | 
**drop_sharding_key** | [**DropShardingKey**](DropShardingKey.md) |  | 

## Example

```python
from openapi_client.models.cluster_operations import ClusterOperations

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterOperations from a JSON string
cluster_operations_instance = ClusterOperations.from_json(json)
# print the JSON string representation of the object
print ClusterOperations.to_json()

# convert the object into a dict
cluster_operations_dict = cluster_operations_instance.to_dict()
# create an instance of ClusterOperations from a dict
cluster_operations_form_dict = cluster_operations.from_dict(cluster_operations_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


