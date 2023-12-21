# Batch


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ids** | [**List[ExtendedPointId]**](ExtendedPointId.md) |  | 
**vectors** | [**BatchVectorStruct**](BatchVectorStruct.md) |  | 
**payloads** | [**List[BatchPayloadsInner]**](BatchPayloadsInner.md) |  | [optional] 

## Example

```python
from qdrant_openapi.models.batch import Batch

# TODO update the JSON string below
json = "{}"
# create an instance of Batch from a JSON string
batch_instance = Batch.from_json(json)
# print the JSON string representation of the object
print Batch.to_json()

# convert the object into a dict
batch_dict = batch_instance.to_dict()
# create an instance of Batch from a dict
batch_form_dict = batch.from_dict(batch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


