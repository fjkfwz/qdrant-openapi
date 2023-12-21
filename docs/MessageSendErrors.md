# MessageSendErrors

Message send failures for a particular peer

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**latest_error** | **str** |  | [optional] 

## Example

```python
from qdrant_openapi.models.message_send_errors import MessageSendErrors

# TODO update the JSON string below
json = "{}"
# create an instance of MessageSendErrors from a JSON string
message_send_errors_instance = MessageSendErrors.from_json(json)
# print the JSON string representation of the object
print MessageSendErrors.to_json()

# convert the object into a dict
message_send_errors_dict = message_send_errors_instance.to_dict()
# create an instance of MessageSendErrors from a dict
message_send_errors_form_dict = message_send_errors.from_dict(message_send_errors_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


