# RenameAliasOperation

Change alias to a new one

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rename_alias** | [**RenameAlias**](RenameAlias.md) |  | 

## Example

```python
from openapi_client.models.rename_alias_operation import RenameAliasOperation

# TODO update the JSON string below
json = "{}"
# create an instance of RenameAliasOperation from a JSON string
rename_alias_operation_instance = RenameAliasOperation.from_json(json)
# print the JSON string representation of the object
print RenameAliasOperation.to_json()

# convert the object into a dict
rename_alias_operation_dict = rename_alias_operation_instance.to_dict()
# create an instance of RenameAliasOperation from a dict
rename_alias_operation_form_dict = rename_alias_operation.from_dict(rename_alias_operation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


