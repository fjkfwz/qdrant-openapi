# PointIdsList


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**points** | [**List[ExtendedPointId]**](ExtendedPointId.md) |  | 
**shard_key** | [**ShardKeySelector**](ShardKeySelector.md) |  | [optional] 

## Example

```python
from openapi_client.models.point_ids_list import PointIdsList

# TODO update the JSON string below
json = "{}"
# create an instance of PointIdsList from a JSON string
point_ids_list_instance = PointIdsList.from_json(json)
# print the JSON string representation of the object
print PointIdsList.to_json()

# convert the object into a dict
point_ids_list_dict = point_ids_list_instance.to_dict()
# create an instance of PointIdsList from a dict
point_ids_list_form_dict = point_ids_list.from_dict(point_ids_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


