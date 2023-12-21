# CollectionInfo

Current statistics and configuration of the collection

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**CollectionStatus**](CollectionStatus.md) |  | 
**optimizer_status** | [**OptimizersStatus**](OptimizersStatus.md) |  | 
**vectors_count** | **int** | Approximate number of vectors in collection. All vectors in collection are available for querying. Calculated as &#x60;points_count x vectors_per_point&#x60;. Where &#x60;vectors_per_point&#x60; is a number of named vectors in schema. | [optional] 
**indexed_vectors_count** | **int** | Approximate number of indexed vectors in the collection. Indexed vectors in large segments are faster to query, as it is stored in a specialized vector index. | [optional] 
**points_count** | **int** | Approximate number of points (vectors + payloads) in collection. Each point could be accessed by unique id. | [optional] 
**segments_count** | **int** | Number of segments in collection. Each segment has independent vector as payload indexes | 
**config** | [**CollectionConfig**](CollectionConfig.md) |  | 
**payload_schema** | [**Dict[str, PayloadIndexInfo]**](PayloadIndexInfo.md) | Types of stored payload | 

## Example

```python
from openapi_client.models.collection_info import CollectionInfo

# TODO update the JSON string below
json = "{}"
# create an instance of CollectionInfo from a JSON string
collection_info_instance = CollectionInfo.from_json(json)
# print the JSON string representation of the object
print CollectionInfo.to_json()

# convert the object into a dict
collection_info_dict = collection_info_instance.to_dict()
# create an instance of CollectionInfo from a dict
collection_info_form_dict = collection_info.from_dict(collection_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


