# SparseVector

Sparse vector structure

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**indices** | **List[int]** | indices must be unique | 
**values** | **List[float]** | values and indices must be the same length | 

## Example

```python
from qdrant_openapi.models.sparse_vector import SparseVector

# TODO update the JSON string below
json = "{}"
# create an instance of SparseVector from a JSON string
sparse_vector_instance = SparseVector.from_json(json)
# print the JSON string representation of the object
print SparseVector.to_json()

# convert the object into a dict
sparse_vector_dict = sparse_vector_instance.to_dict()
# create an instance of SparseVector from a dict
sparse_vector_form_dict = sparse_vector.from_dict(sparse_vector_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


