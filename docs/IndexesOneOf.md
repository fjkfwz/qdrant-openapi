# IndexesOneOf

Do not use any index, scan whole vector collection during search. Guarantee 100% precision, but may be time consuming on large collections.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**options** | **object** |  | 

## Example

```python
from qdrant_openapi.models.indexes_one_of import IndexesOneOf

# TODO update the JSON string below
json = "{}"
# create an instance of IndexesOneOf from a JSON string
indexes_one_of_instance = IndexesOneOf.from_json(json)
# print the JSON string representation of the object
print IndexesOneOf.to_json()

# convert the object into a dict
indexes_one_of_dict = indexes_one_of_instance.to_dict()
# create an instance of IndexesOneOf from a dict
indexes_one_of_form_dict = indexes_one_of.from_dict(indexes_one_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


