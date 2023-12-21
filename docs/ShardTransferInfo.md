# ShardTransferInfo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**shard_id** | **int** |  | 
**var_from** | **int** |  | 
**to** | **int** |  | 
**sync** | **bool** | If &#x60;true&#x60; transfer is a synchronization of a replicas If &#x60;false&#x60; transfer is a moving of a shard from one peer to another | 
**method** | [**ShardTransferMethod**](ShardTransferMethod.md) |  | [optional] 

## Example

```python
from openapi_client.models.shard_transfer_info import ShardTransferInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ShardTransferInfo from a JSON string
shard_transfer_info_instance = ShardTransferInfo.from_json(json)
# print the JSON string representation of the object
print ShardTransferInfo.to_json()

# convert the object into a dict
shard_transfer_info_dict = shard_transfer_info_instance.to_dict()
# create an instance of ShardTransferInfo from a dict
shard_transfer_info_form_dict = shard_transfer_info.from_dict(shard_transfer_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


