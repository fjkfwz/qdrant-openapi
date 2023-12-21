# CollectionParams


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vectors** | [**VectorsConfig**](VectorsConfig.md) |  | [optional] 
**shard_number** | **int** | Number of shards the collection has | [optional] [default to 1]
**sharding_method** | [**ShardingMethod**](ShardingMethod.md) |  | [optional] 
**replication_factor** | **int** | Number of replicas for each shard | [optional] [default to 1]
**write_consistency_factor** | **int** | Defines how many replicas should apply the operation for us to consider it successful. Increasing this number will make the collection more resilient to inconsistencies, but will also make it fail if not enough replicas are available. Does not have any performance impact. | [optional] [default to 1]
**read_fan_out_factor** | **int** | Defines how many additional replicas should be processing read request at the same time. Default value is Auto, which means that fan-out will be determined automatically based on the busyness of the local replica. Having more than 0 might be useful to smooth latency spikes of individual nodes. | [optional] 
**on_disk_payload** | **bool** | If true - point&#39;s payload will not be stored in memory. It will be read from the disk every time it is requested. This setting saves RAM by (slightly) increasing the response time. Note: those payload values that are involved in filtering and are indexed - remain in RAM. | [optional] [default to False]
**sparse_vectors** | [**Dict[str, SparseVectorParams]**](SparseVectorParams.md) | Configuration of the sparse vector storage | [optional] 

## Example

```python
from qdrant_openapi.models.collection_params import CollectionParams

# TODO update the JSON string below
json = "{}"
# create an instance of CollectionParams from a JSON string
collection_params_instance = CollectionParams.from_json(json)
# print the JSON string representation of the object
print CollectionParams.to_json()

# convert the object into a dict
collection_params_dict = collection_params_instance.to_dict()
# create an instance of CollectionParams from a dict
collection_params_form_dict = collection_params.from_dict(collection_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


