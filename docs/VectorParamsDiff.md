# VectorParamsDiff


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hnsw_config** | [**HnswConfigDiff**](HnswConfigDiff.md) |  | [optional] 
**quantization_config** | [**QuantizationConfigDiff**](QuantizationConfigDiff.md) |  | [optional] 
**on_disk** | **bool** | If true, vectors are served from disk, improving RAM usage at the cost of latency | [optional] 

## Example

```python
from openapi_client.models.vector_params_diff import VectorParamsDiff

# TODO update the JSON string below
json = "{}"
# create an instance of VectorParamsDiff from a JSON string
vector_params_diff_instance = VectorParamsDiff.from_json(json)
# print the JSON string representation of the object
print VectorParamsDiff.to_json()

# convert the object into a dict
vector_params_diff_dict = vector_params_diff_instance.to_dict()
# create an instance of VectorParamsDiff from a dict
vector_params_diff_form_dict = vector_params_diff.from_dict(vector_params_diff_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


