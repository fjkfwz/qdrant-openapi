# PointInsertOperations


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**batch** | [**Batch**](Batch.md) |  | 
**shard_key** | [**ShardKeySelector**](ShardKeySelector.md) |  | [optional] 
**points** | [**List[PointStruct]**](PointStruct.md) |  | 

## Example

```python
from qdrant_openapi.models.point_insert_operations import PointInsertOperations

# TODO update the JSON string below
json = "{}"
# create an instance of PointInsertOperations from a JSON string
point_insert_operations_instance = PointInsertOperations.from_json(json)
# print the JSON string representation of the object
print PointInsertOperations.to_json()

# convert the object into a dict
point_insert_operations_dict = point_insert_operations_instance.to_dict()
# create an instance of PointInsertOperations from a dict
point_insert_operations_form_dict = point_insert_operations.from_dict(point_insert_operations_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


