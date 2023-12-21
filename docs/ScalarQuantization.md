# ScalarQuantization


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scalar** | [**ScalarQuantizationConfig**](ScalarQuantizationConfig.md) |  | 

## Example

```python
from qdrant_openapi.models.scalar_quantization import ScalarQuantization

# TODO update the JSON string below
json = "{}"
# create an instance of ScalarQuantization from a JSON string
scalar_quantization_instance = ScalarQuantization.from_json(json)
# print the JSON string representation of the object
print ScalarQuantization.to_json()

# convert the object into a dict
scalar_quantization_dict = scalar_quantization_instance.to_dict()
# create an instance of ScalarQuantization from a dict
scalar_quantization_form_dict = scalar_quantization.from_dict(scalar_quantization_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


