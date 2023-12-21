# Indexes

Vector index configuration

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**options** | [**HnswConfig**](HnswConfig.md) |  | 

## Example

```python
from qdrant_openapi.models.indexes import Indexes

# TODO update the JSON string below
json = "{}"
# create an instance of Indexes from a JSON string
indexes_instance = Indexes.from_json(json)
# print the JSON string representation of the object
print Indexes.to_json()

# convert the object into a dict
indexes_dict = indexes_instance.to_dict()
# create an instance of Indexes from a dict
indexes_form_dict = indexes.from_dict(indexes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


