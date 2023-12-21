# WithPayloadInterface

Options for specifying which payload to include or not

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**include** | **List[str]** | Only include this payload keys | 
**exclude** | **List[str]** | Exclude this fields from returning payload | 

## Example

```python
from openapi_client.models.with_payload_interface import WithPayloadInterface

# TODO update the JSON string below
json = "{}"
# create an instance of WithPayloadInterface from a JSON string
with_payload_interface_instance = WithPayloadInterface.from_json(json)
# print the JSON string representation of the object
print WithPayloadInterface.to_json()

# convert the object into a dict
with_payload_interface_dict = with_payload_interface_instance.to_dict()
# create an instance of WithPayloadInterface from a dict
with_payload_interface_form_dict = with_payload_interface.from_dict(with_payload_interface_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


