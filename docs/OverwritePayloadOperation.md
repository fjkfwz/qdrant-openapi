# OverwritePayloadOperation


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**overwrite_payload** | [**SetPayload**](SetPayload.md) |  | 

## Example

```python
from qdrant_openapi.models.overwrite_payload_operation import OverwritePayloadOperation

# TODO update the JSON string below
json = "{}"
# create an instance of OverwritePayloadOperation from a JSON string
overwrite_payload_operation_instance = OverwritePayloadOperation.from_json(json)
# print the JSON string representation of the object
print OverwritePayloadOperation.to_json()

# convert the object into a dict
overwrite_payload_operation_dict = overwrite_payload_operation_instance.to_dict()
# create an instance of OverwritePayloadOperation from a dict
overwrite_payload_operation_form_dict = overwrite_payload_operation.from_dict(overwrite_payload_operation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


