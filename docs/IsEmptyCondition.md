# IsEmptyCondition

Select points with empty payload for a specified field

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_empty** | [**PayloadField**](PayloadField.md) |  | 

## Example

```python
from openapi_client.models.is_empty_condition import IsEmptyCondition

# TODO update the JSON string below
json = "{}"
# create an instance of IsEmptyCondition from a JSON string
is_empty_condition_instance = IsEmptyCondition.from_json(json)
# print the JSON string representation of the object
print IsEmptyCondition.to_json()

# convert the object into a dict
is_empty_condition_dict = is_empty_condition_instance.to_dict()
# create an instance of IsEmptyCondition from a dict
is_empty_condition_form_dict = is_empty_condition.from_dict(is_empty_condition_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


