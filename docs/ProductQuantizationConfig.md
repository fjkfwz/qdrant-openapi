# ProductQuantizationConfig


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**compression** | [**CompressionRatio**](CompressionRatio.md) |  | 
**always_ram** | **bool** |  | [optional] 

## Example

```python
from qdrant_openapi.models.product_quantization_config import ProductQuantizationConfig

# TODO update the JSON string below
json = "{}"
# create an instance of ProductQuantizationConfig from a JSON string
product_quantization_config_instance = ProductQuantizationConfig.from_json(json)
# print the JSON string representation of the object
print ProductQuantizationConfig.to_json()

# convert the object into a dict
product_quantization_config_dict = product_quantization_config_instance.to_dict()
# create an instance of ProductQuantizationConfig from a dict
product_quantization_config_form_dict = product_quantization_config.from_dict(product_quantization_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


