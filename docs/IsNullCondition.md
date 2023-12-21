# IsNullCondition

Select points with null payload for a specified field

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_null** | [**PayloadField**](PayloadField.md) |  | 

## Example

```python
from qdrant_openapi.models.is_null_condition import IsNullCondition

# TODO update the JSON string below
json = "{}"
# create an instance of IsNullCondition from a JSON string
is_null_condition_instance = IsNullCondition.from_json(json)
# print the JSON string representation of the object
print IsNullCondition.to_json()

# convert the object into a dict
is_null_condition_dict = is_null_condition_instance.to_dict()
# create an instance of IsNullCondition from a dict
is_null_condition_form_dict = is_null_condition.from_dict(is_null_condition_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


