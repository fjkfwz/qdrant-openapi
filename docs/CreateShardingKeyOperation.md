# CreateShardingKeyOperation


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**create_sharding_key** | [**CreateShardingKey**](CreateShardingKey.md) |  | 

## Example

```python
from qdrant_openapi.models.create_sharding_key_operation import CreateShardingKeyOperation

# TODO update the JSON string below
json = "{}"
# create an instance of CreateShardingKeyOperation from a JSON string
create_sharding_key_operation_instance = CreateShardingKeyOperation.from_json(json)
# print the JSON string representation of the object
print CreateShardingKeyOperation.to_json()

# convert the object into a dict
create_sharding_key_operation_dict = create_sharding_key_operation_instance.to_dict()
# create an instance of CreateShardingKeyOperation from a dict
create_sharding_key_operation_form_dict = create_sharding_key_operation.from_dict(create_sharding_key_operation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


