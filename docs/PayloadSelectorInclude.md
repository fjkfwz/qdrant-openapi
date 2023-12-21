# PayloadSelectorInclude


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**include** | **List[str]** | Only include this payload keys | 

## Example

```python
from qdrant_openapi.models.payload_selector_include import PayloadSelectorInclude

# TODO update the JSON string below
json = "{}"
# create an instance of PayloadSelectorInclude from a JSON string
payload_selector_include_instance = PayloadSelectorInclude.from_json(json)
# print the JSON string representation of the object
print PayloadSelectorInclude.to_json()

# convert the object into a dict
payload_selector_include_dict = payload_selector_include_instance.to_dict()
# create an instance of PayloadSelectorInclude from a dict
payload_selector_include_form_dict = payload_selector_include.from_dict(payload_selector_include_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


