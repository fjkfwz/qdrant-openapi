# NamedSparseVector

Sparse vector data with name

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of vector data | 
**vector** | [**SparseVector**](SparseVector.md) |  | 

## Example

```python
from qdrant_openapi.models.named_sparse_vector import NamedSparseVector

# TODO update the JSON string below
json = "{}"
# create an instance of NamedSparseVector from a JSON string
named_sparse_vector_instance = NamedSparseVector.from_json(json)
# print the JSON string representation of the object
print NamedSparseVector.to_json()

# convert the object into a dict
named_sparse_vector_dict = named_sparse_vector_instance.to_dict()
# create an instance of NamedSparseVector from a dict
named_sparse_vector_form_dict = named_sparse_vector.from_dict(named_sparse_vector_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


