# PayloadSelector

Specifies how to treat payload selector

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**include** | **List[str]** | Only include this payload keys | 
**exclude** | **List[str]** | Exclude this fields from returning payload | 

## Example

```python
from openapi_client.models.payload_selector import PayloadSelector

# TODO update the JSON string below
json = "{}"
# create an instance of PayloadSelector from a JSON string
payload_selector_instance = PayloadSelector.from_json(json)
# print the JSON string representation of the object
print PayloadSelector.to_json()

# convert the object into a dict
payload_selector_dict = payload_selector_instance.to_dict()
# create an instance of PayloadSelector from a dict
payload_selector_form_dict = payload_selector.from_dict(payload_selector_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


