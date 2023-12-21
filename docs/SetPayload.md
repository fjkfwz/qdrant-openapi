# SetPayload

This data structure is used in API interface and applied across multiple shards

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payload** | **Dict[str, object]** |  | 
**points** | [**List[ExtendedPointId]**](ExtendedPointId.md) | Assigns payload to each point in this list | [optional] 
**filter** | [**Filter**](Filter.md) |  | [optional] 
**shard_key** | [**ShardKeySelector**](ShardKeySelector.md) |  | [optional] 

## Example

```python
from qdrant_openapi.models.set_payload import SetPayload

# TODO update the JSON string below
json = "{}"
# create an instance of SetPayload from a JSON string
set_payload_instance = SetPayload.from_json(json)
# print the JSON string representation of the object
print SetPayload.to_json()

# convert the object into a dict
set_payload_dict = set_payload_instance.to_dict()
# create an instance of SetPayload from a dict
set_payload_form_dict = set_payload.from_dict(set_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


