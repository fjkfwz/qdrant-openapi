# MatchText

Full-text match of the strings.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**text** | **str** |  | 

## Example

```python
from qdrant_openapi.models.match_text import MatchText

# TODO update the JSON string below
json = "{}"
# create an instance of MatchText from a JSON string
match_text_instance = MatchText.from_json(json)
# print the JSON string representation of the object
print MatchText.to_json()

# convert the object into a dict
match_text_dict = match_text_instance.to_dict()
# create an instance of MatchText from a dict
match_text_form_dict = match_text.from_dict(match_text_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


