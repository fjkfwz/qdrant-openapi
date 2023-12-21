# NamedVectorStruct

Vector data separator for named and unnamed modes Unnamed mode:  { \"vector\": [1.0, 2.0, 3.0] }  or named mode:  { \"vector\": { \"vector\": [1.0, 2.0, 3.0], \"name\": \"image-embeddings\" } }

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of vector data | 
**vector** | [**SparseVector**](SparseVector.md) |  | 

## Example

```python
from openapi_client.models.named_vector_struct import NamedVectorStruct

# TODO update the JSON string below
json = "{}"
# create an instance of NamedVectorStruct from a JSON string
named_vector_struct_instance = NamedVectorStruct.from_json(json)
# print the JSON string representation of the object
print NamedVectorStruct.to_json()

# convert the object into a dict
named_vector_struct_dict = named_vector_struct_instance.to_dict()
# create an instance of NamedVectorStruct from a dict
named_vector_struct_form_dict = named_vector_struct.from_dict(named_vector_struct_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


