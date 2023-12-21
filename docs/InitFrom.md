# InitFrom

Operation for creating new collection and (optionally) specify index params

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**collection** | **str** |  | 

## Example

```python
from qdrant_openapi.models.init_from import InitFrom

# TODO update the JSON string below
json = "{}"
# create an instance of InitFrom from a JSON string
init_from_instance = InitFrom.from_json(json)
# print the JSON string representation of the object
print InitFrom.to_json()

# convert the object into a dict
init_from_dict = init_from_instance.to_dict()
# create an instance of InitFrom from a dict
init_from_form_dict = init_from.from_dict(init_from_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


