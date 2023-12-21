# PayloadSelectorExclude


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**exclude** | **List[str]** | Exclude this fields from returning payload | 

## Example

```python
from qdrant_openapi.models.payload_selector_exclude import PayloadSelectorExclude

# TODO update the JSON string below
json = "{}"
# create an instance of PayloadSelectorExclude from a JSON string
payload_selector_exclude_instance = PayloadSelectorExclude.from_json(json)
# print the JSON string representation of the object
print PayloadSelectorExclude.to_json()

# convert the object into a dict
payload_selector_exclude_dict = payload_selector_exclude_instance.to_dict()
# create an instance of PayloadSelectorExclude from a dict
payload_selector_exclude_form_dict = payload_selector_exclude.from_dict(payload_selector_exclude_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


