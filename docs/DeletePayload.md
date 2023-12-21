# DeletePayload

This data structure is used in API interface and applied across multiple shards

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**keys** | **List[str]** | List of payload keys to remove from payload | 
**points** | [**List[ExtendedPointId]**](ExtendedPointId.md) | Deletes values from each point in this list | [optional] 
**filter** | [**Filter**](Filter.md) |  | [optional] 
**shard_key** | [**ShardKeySelector**](ShardKeySelector.md) |  | [optional] 

## Example

```python
from openapi_client.models.delete_payload import DeletePayload

# TODO update the JSON string below
json = "{}"
# create an instance of DeletePayload from a JSON string
delete_payload_instance = DeletePayload.from_json(json)
# print the JSON string representation of the object
print DeletePayload.to_json()

# convert the object into a dict
delete_payload_dict = delete_payload_instance.to_dict()
# create an instance of DeletePayload from a dict
delete_payload_form_dict = delete_payload.from_dict(delete_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


