# PointsList


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**points** | [**List[PointStruct]**](PointStruct.md) |  | 
**shard_key** | [**ShardKeySelector**](ShardKeySelector.md) |  | [optional] 

## Example

```python
from qdrant_openapi.models.points_list import PointsList

# TODO update the JSON string below
json = "{}"
# create an instance of PointsList from a JSON string
points_list_instance = PointsList.from_json(json)
# print the JSON string representation of the object
print PointsList.to_json()

# convert the object into a dict
points_list_dict = points_list_instance.to_dict()
# create an instance of PointsList from a dict
points_list_form_dict = points_list.from_dict(points_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


