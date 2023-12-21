# NamedVector

Vector data with name

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of vector data | 
**vector** | **List[float]** | Vector data | 

## Example

```python
from openapi_client.models.named_vector import NamedVector

# TODO update the JSON string below
json = "{}"
# create an instance of NamedVector from a JSON string
named_vector_instance = NamedVector.from_json(json)
# print the JSON string representation of the object
print NamedVector.to_json()

# convert the object into a dict
named_vector_dict = named_vector_instance.to_dict()
# create an instance of NamedVector from a dict
named_vector_form_dict = named_vector.from_dict(named_vector_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


