# CreateShardingKey


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**shard_key** | [**ShardKey**](ShardKey.md) |  | 
**shards_number** | **int** | How many shards to create for this key If not specified, will use the default value from config | [optional] 
**replication_factor** | **int** | How many replicas to create for each shard If not specified, will use the default value from config | [optional] 
**placement** | **List[int]** | Placement of shards for this key List of peer ids, that can be used to place shards for this key If not specified, will be randomly placed among all peers | [optional] 

## Example

```python
from qdrant_openapi.models.create_sharding_key import CreateShardingKey

# TODO update the JSON string below
json = "{}"
# create an instance of CreateShardingKey from a JSON string
create_sharding_key_instance = CreateShardingKey.from_json(json)
# print the JSON string representation of the object
print CreateShardingKey.to_json()

# convert the object into a dict
create_sharding_key_dict = create_sharding_key_instance.to_dict()
# create an instance of CreateShardingKey from a dict
create_sharding_key_form_dict = create_sharding_key.from_dict(create_sharding_key_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


