# SparseIndexConfig

Configuration for sparse inverted index.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**full_scan_threshold** | **int** | We prefer a full scan search upto (excluding) this number of vectors.  Note: this is number of vectors, not KiloBytes. | [optional] 
**index_type** | [**SparseIndexType**](SparseIndexType.md) |  | 

## Example

```python
from openapi_client.models.sparse_index_config import SparseIndexConfig

# TODO update the JSON string below
json = "{}"
# create an instance of SparseIndexConfig from a JSON string
sparse_index_config_instance = SparseIndexConfig.from_json(json)
# print the JSON string representation of the object
print SparseIndexConfig.to_json()

# convert the object into a dict
sparse_index_config_dict = sparse_index_config_instance.to_dict()
# create an instance of SparseIndexConfig from a dict
sparse_index_config_form_dict = sparse_index_config.from_dict(sparse_index_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


