# QuantizationConfig


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scalar** | [**ScalarQuantizationConfig**](ScalarQuantizationConfig.md) |  | 
**product** | [**ProductQuantizationConfig**](ProductQuantizationConfig.md) |  | 
**binary** | [**BinaryQuantizationConfig**](BinaryQuantizationConfig.md) |  | 

## Example

```python
from openapi_client.models.quantization_config import QuantizationConfig

# TODO update the JSON string below
json = "{}"
# create an instance of QuantizationConfig from a JSON string
quantization_config_instance = QuantizationConfig.from_json(json)
# print the JSON string representation of the object
print QuantizationConfig.to_json()

# convert the object into a dict
quantization_config_dict = quantization_config_instance.to_dict()
# create an instance of QuantizationConfig from a dict
quantization_config_form_dict = quantization_config.from_dict(quantization_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


