# QuantizationSearchParams

Additional parameters of the search

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ignore** | **bool** | If true, quantized vectors are ignored. Default is false. | [optional] [default to False]
**rescore** | **bool** | If true, use original vectors to re-score top-k results. Might require more time in case if original vectors are stored on disk. If not set, qdrant decides automatically apply rescoring or not. | [optional] 
**oversampling** | **float** | Oversampling factor for quantization. Default is 1.0.  Defines how many extra vectors should be pre-selected using quantized index, and then re-scored using original vectors.  For example, if &#x60;oversampling&#x60; is 2.4 and &#x60;limit&#x60; is 100, then 240 vectors will be pre-selected using quantized index, and then top-100 will be returned after re-scoring. | [optional] 

## Example

```python
from qdrant_openapi.models.quantization_search_params import QuantizationSearchParams

# TODO update the JSON string below
json = "{}"
# create an instance of QuantizationSearchParams from a JSON string
quantization_search_params_instance = QuantizationSearchParams.from_json(json)
# print the JSON string representation of the object
print QuantizationSearchParams.to_json()

# convert the object into a dict
quantization_search_params_dict = quantization_search_params_instance.to_dict()
# create an instance of QuantizationSearchParams from a dict
quantization_search_params_form_dict = quantization_search_params.from_dict(quantization_search_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


