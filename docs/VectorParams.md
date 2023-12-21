# VectorParams

Params of single vector data storage

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**size** | **int** | Size of a vectors used | 
**distance** | [**Distance**](Distance.md) |  | 
**hnsw_config** | [**HnswConfigDiff**](HnswConfigDiff.md) |  | [optional] 
**quantization_config** | [**QuantizationConfig**](QuantizationConfig.md) |  | [optional] 
**on_disk** | **bool** | If true, vectors are served from disk, improving RAM usage at the cost of latency Default: false | [optional] 

## Example

```python
from qdrant_openapi.models.vector_params import VectorParams

# TODO update the JSON string below
json = "{}"
# create an instance of VectorParams from a JSON string
vector_params_instance = VectorParams.from_json(json)
# print the JSON string representation of the object
print VectorParams.to_json()

# convert the object into a dict
vector_params_dict = vector_params_instance.to_dict()
# create an instance of VectorParams from a dict
vector_params_form_dict = vector_params.from_dict(vector_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


