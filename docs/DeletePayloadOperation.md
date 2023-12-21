# DeletePayloadOperation


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**delete_payload** | [**DeletePayload**](DeletePayload.md) |  | 

## Example

```python
from qdrant_openapi.models.delete_payload_operation import DeletePayloadOperation

# TODO update the JSON string below
json = "{}"
# create an instance of DeletePayloadOperation from a JSON string
delete_payload_operation_instance = DeletePayloadOperation.from_json(json)
# print the JSON string representation of the object
print DeletePayloadOperation.to_json()

# convert the object into a dict
delete_payload_operation_dict = delete_payload_operation_instance.to_dict()
# create an instance of DeletePayloadOperation from a dict
delete_payload_operation_form_dict = delete_payload_operation.from_dict(delete_payload_operation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


