# DeleteVectors


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**points** | [**List[ExtendedPointId]**](ExtendedPointId.md) | Deletes values from each point in this list | [optional] 
**filter** | [**Filter**](Filter.md) |  | [optional] 
**vector** | **List[str]** | Vector names | 
**shard_key** | [**ShardKeySelector**](ShardKeySelector.md) |  | [optional] 

## Example

```python
from qdrant_openapi.models.delete_vectors import DeleteVectors

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteVectors from a JSON string
delete_vectors_instance = DeleteVectors.from_json(json)
# print the JSON string representation of the object
print DeleteVectors.to_json()

# convert the object into a dict
delete_vectors_dict = delete_vectors_instance.to_dict()
# create an instance of DeleteVectors from a dict
delete_vectors_form_dict = delete_vectors.from_dict(delete_vectors_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


