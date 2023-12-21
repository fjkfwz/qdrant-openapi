# SetPayloadOperation


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**set_payload** | [**SetPayload**](SetPayload.md) |  | 

## Example

```python
from qdrant_openapi.models.set_payload_operation import SetPayloadOperation

# TODO update the JSON string below
json = "{}"
# create an instance of SetPayloadOperation from a JSON string
set_payload_operation_instance = SetPayloadOperation.from_json(json)
# print the JSON string representation of the object
print SetPayloadOperation.to_json()

# convert the object into a dict
set_payload_operation_dict = set_payload_operation_instance.to_dict()
# create an instance of SetPayloadOperation from a dict
set_payload_operation_form_dict = set_payload_operation.from_dict(set_payload_operation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


