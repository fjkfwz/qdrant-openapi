# CollectionConfig


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**params** | [**CollectionParams**](CollectionParams.md) |  | 
**hnsw_config** | [**HnswConfig**](HnswConfig.md) |  | 
**optimizer_config** | [**OptimizersConfig**](OptimizersConfig.md) |  | 
**wal_config** | [**WalConfig**](WalConfig.md) |  | 
**quantization_config** | [**QuantizationConfig**](QuantizationConfig.md) |  | [optional] 

## Example

```python
from qdrant_openapi.models.collection_config import CollectionConfig

# TODO update the JSON string below
json = "{}"
# create an instance of CollectionConfig from a JSON string
collection_config_instance = CollectionConfig.from_json(json)
# print the JSON string representation of the object
print CollectionConfig.to_json()

# convert the object into a dict
collection_config_dict = collection_config_instance.to_dict()
# create an instance of CollectionConfig from a dict
collection_config_form_dict = collection_config.from_dict(collection_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


