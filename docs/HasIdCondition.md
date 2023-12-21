# HasIdCondition

ID-based filtering condition

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**has_id** | [**List[ExtendedPointId]**](ExtendedPointId.md) |  | 

## Example

```python
from qdrant_openapi.models.has_id_condition import HasIdCondition

# TODO update the JSON string below
json = "{}"
# create an instance of HasIdCondition from a JSON string
has_id_condition_instance = HasIdCondition.from_json(json)
# print the JSON string representation of the object
print HasIdCondition.to_json()

# convert the object into a dict
has_id_condition_dict = has_id_condition_instance.to_dict()
# create an instance of HasIdCondition from a dict
has_id_condition_form_dict = has_id_condition.from_dict(has_id_condition_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


