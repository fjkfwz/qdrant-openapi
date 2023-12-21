# MatchValue

Exact match of the given value

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**ValueVariants**](ValueVariants.md) |  | 

## Example

```python
from qdrant_openapi.models.match_value import MatchValue

# TODO update the JSON string below
json = "{}"
# create an instance of MatchValue from a JSON string
match_value_instance = MatchValue.from_json(json)
# print the JSON string representation of the object
print MatchValue.to_json()

# convert the object into a dict
match_value_dict = match_value_instance.to_dict()
# create an instance of MatchValue from a dict
match_value_form_dict = match_value.from_dict(match_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


