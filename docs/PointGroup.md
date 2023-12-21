# PointGroup


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hits** | [**List[ScoredPoint]**](ScoredPoint.md) | Scored points that have the same value of the group_by key | 
**id** | [**GroupId**](GroupId.md) |  | 
**lookup** | [**Record**](Record.md) |  | [optional] 

## Example

```python
from openapi_client.models.point_group import PointGroup

# TODO update the JSON string below
json = "{}"
# create an instance of PointGroup from a JSON string
point_group_instance = PointGroup.from_json(json)
# print the JSON string representation of the object
print PointGroup.to_json()

# convert the object into a dict
point_group_dict = point_group_instance.to_dict()
# create an instance of PointGroup from a dict
point_group_form_dict = point_group.from_dict(point_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


