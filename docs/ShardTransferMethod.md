# ShardTransferMethod

Methods for transferring a shard from one node to another.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from qdrant_openapi.models.shard_transfer_method import ShardTransferMethod

# TODO update the JSON string below
json = "{}"
# create an instance of ShardTransferMethod from a JSON string
shard_transfer_method_instance = ShardTransferMethod.from_json(json)
# print the JSON string representation of the object
print ShardTransferMethod.to_json()

# convert the object into a dict
shard_transfer_method_dict = shard_transfer_method_instance.to_dict()
# create an instance of ShardTransferMethod from a dict
shard_transfer_method_form_dict = shard_transfer_method.from_dict(shard_transfer_method_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


