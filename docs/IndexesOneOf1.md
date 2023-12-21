# IndexesOneOf1

Use filterable HNSW index for approximate search. Is very fast even on a very huge collections, but require additional space to store index and additional time to build it.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**options** | [**HnswConfig**](HnswConfig.md) |  | 

## Example

```python
from qdrant_openapi.models.indexes_one_of1 import IndexesOneOf1

# TODO update the JSON string below
json = "{}"
# create an instance of IndexesOneOf1 from a JSON string
indexes_one_of1_instance = IndexesOneOf1.from_json(json)
# print the JSON string representation of the object
print IndexesOneOf1.to_json()

# convert the object into a dict
indexes_one_of1_dict = indexes_one_of1_instance.to_dict()
# create an instance of IndexesOneOf1 from a dict
indexes_one_of1_form_dict = indexes_one_of1.from_dict(indexes_one_of1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


