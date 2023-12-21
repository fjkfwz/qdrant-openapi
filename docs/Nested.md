# Nested

Select points with payload for a specified nested field

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** |  | 
**filter** | [**Filter**](Filter.md) |  | 

## Example

```python
from openapi_client.models.nested import Nested

# TODO update the JSON string below
json = "{}"
# create an instance of Nested from a JSON string
nested_instance = Nested.from_json(json)
# print the JSON string representation of the object
print Nested.to_json()

# convert the object into a dict
nested_dict = nested_instance.to_dict()
# create an instance of Nested from a dict
nested_form_dict = nested.from_dict(nested_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


