# MatchExcept

Should have at least one value not matching the any given values

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_except** | [**AnyVariants**](AnyVariants.md) |  | 

## Example

```python
from qdrant_openapi.models.match_except import MatchExcept

# TODO update the JSON string below
json = "{}"
# create an instance of MatchExcept from a JSON string
match_except_instance = MatchExcept.from_json(json)
# print the JSON string representation of the object
print MatchExcept.to_json()

# convert the object into a dict
match_except_dict = match_except_instance.to_dict()
# create an instance of MatchExcept from a dict
match_except_form_dict = match_except.from_dict(match_except_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


