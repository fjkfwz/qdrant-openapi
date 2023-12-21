# SparseIndexParams

Configuration for sparse inverted index.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**full_scan_threshold** | **int** | We prefer a full scan search upto (excluding) this number of vectors.  Note: this is number of vectors, not KiloBytes. | [optional] 
**on_disk** | **bool** | Store index on disk. If set to false, the index will be stored in RAM. Default: false | [optional] 

## Example

```python
from openapi_client.models.sparse_index_params import SparseIndexParams

# TODO update the JSON string below
json = "{}"
# create an instance of SparseIndexParams from a JSON string
sparse_index_params_instance = SparseIndexParams.from_json(json)
# print the JSON string representation of the object
print SparseIndexParams.to_json()

# convert the object into a dict
sparse_index_params_dict = sparse_index_params_instance.to_dict()
# create an instance of SparseIndexParams from a dict
sparse_index_params_form_dict = sparse_index_params.from_dict(sparse_index_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


