# VectorDataConfig

Config of single vector data storage

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**size** | **int** | Size/dimensionality of the vectors used | 
**distance** | [**Distance**](Distance.md) |  | 
**storage_type** | [**VectorStorageType**](VectorStorageType.md) |  | 
**index** | [**Indexes**](Indexes.md) |  | 
**quantization_config** | [**QuantizationConfig**](QuantizationConfig.md) |  | [optional] 

## Example

```python
from qdrant_openapi.models.vector_data_config import VectorDataConfig

# TODO update the JSON string below
json = "{}"
# create an instance of VectorDataConfig from a JSON string
vector_data_config_instance = VectorDataConfig.from_json(json)
# print the JSON string representation of the object
print VectorDataConfig.to_json()

# convert the object into a dict
vector_data_config_dict = vector_data_config_instance.to_dict()
# create an instance of VectorDataConfig from a dict
vector_data_config_form_dict = vector_data_config.from_dict(vector_data_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


