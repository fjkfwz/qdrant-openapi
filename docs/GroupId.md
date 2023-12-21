# GroupId

Value of the group_by key, shared across all the hits in the group

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from qdrant_openapi.models.group_id import GroupId

# TODO update the JSON string below
json = "{}"
# create an instance of GroupId from a JSON string
group_id_instance = GroupId.from_json(json)
# print the JSON string representation of the object
print GroupId.to_json()

# convert the object into a dict
group_id_dict = group_id_instance.to_dict()
# create an instance of GroupId from a dict
group_id_form_dict = group_id.from_dict(group_id_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


