# ScalarQuantizationConfig


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**ScalarType**](ScalarType.md) |  | 
**quantile** | **float** | Quantile for quantization. Expected value range in [0.5, 1.0]. If not set - use the whole range of values | [optional] 
**always_ram** | **bool** | If true - quantized vectors always will be stored in RAM, ignoring the config of main storage | [optional] 

## Example

```python
from qdrant_openapi.models.scalar_quantization_config import ScalarQuantizationConfig

# TODO update the JSON string below
json = "{}"
# create an instance of ScalarQuantizationConfig from a JSON string
scalar_quantization_config_instance = ScalarQuantizationConfig.from_json(json)
# print the JSON string representation of the object
print ScalarQuantizationConfig.to_json()

# convert the object into a dict
scalar_quantization_config_dict = scalar_quantization_config_instance.to_dict()
# create an instance of ScalarQuantizationConfig from a dict
scalar_quantization_config_form_dict = scalar_quantization_config.from_dict(scalar_quantization_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


