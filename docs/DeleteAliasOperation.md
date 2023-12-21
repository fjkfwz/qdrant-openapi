# DeleteAliasOperation

Delete alias if exists

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**delete_alias** | [**DeleteAlias**](DeleteAlias.md) |  | 

## Example

```python
from qdrant_openapi.models.delete_alias_operation import DeleteAliasOperation

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteAliasOperation from a JSON string
delete_alias_operation_instance = DeleteAliasOperation.from_json(json)
# print the JSON string representation of the object
print DeleteAliasOperation.to_json()

# convert the object into a dict
delete_alias_operation_dict = delete_alias_operation_instance.to_dict()
# create an instance of DeleteAliasOperation from a dict
delete_alias_operation_form_dict = delete_alias_operation.from_dict(delete_alias_operation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


