# BinaryQuantizationConfig


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**always_ram** | **bool** |  | [optional] 

## Example

```python
from qdrant_openapi.models.binary_quantization_config import BinaryQuantizationConfig

# TODO update the JSON string below
json = "{}"
# create an instance of BinaryQuantizationConfig from a JSON string
binary_quantization_config_instance = BinaryQuantizationConfig.from_json(json)
# print the JSON string representation of the object
print BinaryQuantizationConfig.to_json()

# convert the object into a dict
binary_quantization_config_dict = binary_quantization_config_instance.to_dict()
# create an instance of BinaryQuantizationConfig from a dict
binary_quantization_config_form_dict = binary_quantization_config.from_dict(binary_quantization_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


