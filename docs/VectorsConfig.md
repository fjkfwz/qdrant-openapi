# VectorsConfig

Vector params separator for single and multiple vector modes Single mode:  { \"size\": 128, \"distance\": \"Cosine\" }  or multiple mode:  { \"default\": { \"size\": 128, \"distance\": \"Cosine\" } }

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
from qdrant_openapi.models.vectors_config import VectorsConfig

# TODO update the JSON string below
json = "{}"
# create an instance of VectorsConfig from a JSON string
vectors_config_instance = VectorsConfig.from_json(json)
# print the JSON string representation of the object
print VectorsConfig.to_json()

# convert the object into a dict
vectors_config_dict = vectors_config_instance.to_dict()
# create an instance of VectorsConfig from a dict
vectors_config_form_dict = vectors_config.from_dict(vectors_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


