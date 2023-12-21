# Record

Point data

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**ExtendedPointId**](ExtendedPointId.md) |  | 
**payload** | **Dict[str, object]** |  | [optional] 
**vector** | [**VectorStruct**](VectorStruct.md) |  | [optional] 
**shard_key** | [**ShardKey**](ShardKey.md) |  | [optional] 

## Example

```python
from openapi_client.models.record import Record

# TODO update the JSON string below
json = "{}"
# create an instance of Record from a JSON string
record_instance = Record.from_json(json)
# print the JSON string representation of the object
print Record.to_json()

# convert the object into a dict
record_dict = record_instance.to_dict()
# create an instance of Record from a dict
record_form_dict = record.from_dict(record_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


