# SparseVectorParams

Params of single sparse vector data storage

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**index** | [**SparseIndexParams**](SparseIndexParams.md) |  | [optional] 

## Example

```python
from qdrant_openapi.models.sparse_vector_params import SparseVectorParams

# TODO update the JSON string below
json = "{}"
# create an instance of SparseVectorParams from a JSON string
sparse_vector_params_instance = SparseVectorParams.from_json(json)
# print the JSON string representation of the object
print SparseVectorParams.to_json()

# convert the object into a dict
sparse_vector_params_dict = sparse_vector_params_instance.to_dict()
# create an instance of SparseVectorParams from a dict
sparse_vector_params_form_dict = sparse_vector_params.from_dict(sparse_vector_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


