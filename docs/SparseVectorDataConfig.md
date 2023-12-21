# SparseVectorDataConfig

Config of single sparse vector data storage

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**index** | [**SparseIndexConfig**](SparseIndexConfig.md) |  | 

## Example

```python
from openapi_client.models.sparse_vector_data_config import SparseVectorDataConfig

# TODO update the JSON string below
json = "{}"
# create an instance of SparseVectorDataConfig from a JSON string
sparse_vector_data_config_instance = SparseVectorDataConfig.from_json(json)
# print the JSON string representation of the object
print SparseVectorDataConfig.to_json()

# convert the object into a dict
sparse_vector_data_config_dict = sparse_vector_data_config_instance.to_dict()
# create an instance of SparseVectorDataConfig from a dict
sparse_vector_data_config_form_dict = sparse_vector_data_config.from_dict(sparse_vector_data_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


