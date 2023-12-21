# UpdateCollection

Operation for updating parameters of the existing collection

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vectors** | [**Dict[str, VectorParamsDiff]**](VectorParamsDiff.md) | Vector update params for multiple vectors  { \&quot;vector_name\&quot;: { \&quot;hnsw_config\&quot;: { \&quot;m\&quot;: 8 } } } | [optional] 
**optimizers_config** | [**OptimizersConfigDiff**](OptimizersConfigDiff.md) |  | [optional] 
**params** | [**CollectionParamsDiff**](CollectionParamsDiff.md) |  | [optional] 
**hnsw_config** | [**HnswConfigDiff**](HnswConfigDiff.md) |  | [optional] 
**quantization_config** | [**QuantizationConfigDiff**](QuantizationConfigDiff.md) |  | [optional] 
**sparse_vectors** | [**Dict[str, SparseVectorParams]**](SparseVectorParams.md) |  | [optional] 

## Example

```python
from openapi_client.models.update_collection import UpdateCollection

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateCollection from a JSON string
update_collection_instance = UpdateCollection.from_json(json)
# print the JSON string representation of the object
print UpdateCollection.to_json()

# convert the object into a dict
update_collection_dict = update_collection_instance.to_dict()
# create an instance of UpdateCollection from a dict
update_collection_form_dict = update_collection.from_dict(update_collection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


