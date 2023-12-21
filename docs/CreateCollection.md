# CreateCollection

Operation for creating new collection and (optionally) specify index params

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vectors** | [**VectorsConfig**](VectorsConfig.md) |  | [optional] 
**shard_number** | **int** | For auto sharding: Number of shards in collection. - Default is 1 for standalone, otherwise equal to the number of nodes - Minimum is 1 For custom sharding: Number of shards in collection per shard group. - Default is 1, meaning that each shard key will be mapped to a single shard - Minimum is 1 | [optional] 
**sharding_method** | [**ShardingMethod**](ShardingMethod.md) |  | [optional] 
**replication_factor** | **int** | Number of shards replicas. Default is 1 Minimum is 1 | [optional] 
**write_consistency_factor** | **int** | Defines how many replicas should apply the operation for us to consider it successful. Increasing this number will make the collection more resilient to inconsistencies, but will also make it fail if not enough replicas are available. Does not have any performance impact. | [optional] 
**on_disk_payload** | **bool** | If true - point&#39;s payload will not be stored in memory. It will be read from the disk every time it is requested. This setting saves RAM by (slightly) increasing the response time. Note: those payload values that are involved in filtering and are indexed - remain in RAM. | [optional] 
**hnsw_config** | [**HnswConfigDiff**](HnswConfigDiff.md) |  | [optional] 
**wal_config** | [**WalConfigDiff**](WalConfigDiff.md) |  | [optional] 
**optimizers_config** | [**OptimizersConfigDiff**](OptimizersConfigDiff.md) |  | [optional] 
**init_from** | [**InitFrom**](InitFrom.md) |  | [optional] 
**quantization_config** | [**QuantizationConfig**](QuantizationConfig.md) |  | [optional] 
**sparse_vectors** | [**Dict[str, SparseVectorParams]**](SparseVectorParams.md) | Sparse vector data config. | [optional] 

## Example

```python
from openapi_client.models.create_collection import CreateCollection

# TODO update the JSON string below
json = "{}"
# create an instance of CreateCollection from a JSON string
create_collection_instance = CreateCollection.from_json(json)
# print the JSON string representation of the object
print CreateCollection.to_json()

# convert the object into a dict
create_collection_dict = create_collection_instance.to_dict()
# create an instance of CreateCollection from a dict
create_collection_form_dict = create_collection.from_dict(create_collection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


