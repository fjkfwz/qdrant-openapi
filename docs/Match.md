# Match

Match filter request

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**ValueVariants**](ValueVariants.md) |  | 
**text** | **str** |  | 
**any** | [**AnyVariants**](AnyVariants.md) |  | 
**var_except** | [**AnyVariants**](AnyVariants.md) |  | 

## Example

```python
from openapi_client.models.match import Match

# TODO update the JSON string below
json = "{}"
# create an instance of Match from a JSON string
match_instance = Match.from_json(json)
# print the JSON string representation of the object
print Match.to_json()

# convert the object into a dict
match_dict = match_instance.to_dict()
# create an instance of Match from a dict
match_form_dict = match.from_dict(match_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


