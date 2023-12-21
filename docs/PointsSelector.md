# PointsSelector


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**points** | [**List[ExtendedPointId]**](ExtendedPointId.md) |  | 
**shard_key** | [**ShardKeySelector**](ShardKeySelector.md) |  | [optional] 
**filter** | [**Filter**](Filter.md) |  | 

## Example

```python
from qdrant_openapi.models.points_selector import PointsSelector

# TODO update the JSON string below
json = "{}"
# create an instance of PointsSelector from a JSON string
points_selector_instance = PointsSelector.from_json(json)
# print the JSON string representation of the object
print PointsSelector.to_json()

# convert the object into a dict
points_selector_dict = points_selector_instance.to_dict()
# create an instance of PointsSelector from a dict
points_selector_form_dict = points_selector.from_dict(points_selector_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


