# DropShardingKey


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**shard_key** | [**ShardKey**](ShardKey.md) |  | 

## Example

```python
from qdrant_openapi.models.drop_sharding_key import DropShardingKey

# TODO update the JSON string below
json = "{}"
# create an instance of DropShardingKey from a JSON string
drop_sharding_key_instance = DropShardingKey.from_json(json)
# print the JSON string representation of the object
print DropShardingKey.to_json()

# convert the object into a dict
drop_sharding_key_dict = drop_sharding_key_instance.to_dict()
# create an instance of DropShardingKey from a dict
drop_sharding_key_form_dict = drop_sharding_key.from_dict(drop_sharding_key_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


