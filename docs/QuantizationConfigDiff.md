# QuantizationConfigDiff


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scalar** | [**ScalarQuantizationConfig**](ScalarQuantizationConfig.md) |  | 
**product** | [**ProductQuantizationConfig**](ProductQuantizationConfig.md) |  | 
**binary** | [**BinaryQuantizationConfig**](BinaryQuantizationConfig.md) |  | 

## Example

```python
from openapi_client.models.quantization_config_diff import QuantizationConfigDiff

# TODO update the JSON string below
json = "{}"
# create an instance of QuantizationConfigDiff from a JSON string
quantization_config_diff_instance = QuantizationConfigDiff.from_json(json)
# print the JSON string representation of the object
print QuantizationConfigDiff.to_json()

# convert the object into a dict
quantization_config_diff_dict = quantization_config_diff_instance.to_dict()
# create an instance of QuantizationConfigDiff from a dict
quantization_config_diff_form_dict = quantization_config_diff.from_dict(quantization_config_diff_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


