# AliasOperations

Group of all the possible operations related to collection aliases

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**create_alias** | [**CreateAlias**](CreateAlias.md) |  | 
**delete_alias** | [**DeleteAlias**](DeleteAlias.md) |  | 
**rename_alias** | [**RenameAlias**](RenameAlias.md) |  | 

## Example

```python
from qdrant_openapi.models.alias_operations import AliasOperations

# TODO update the JSON string below
json = "{}"
# create an instance of AliasOperations from a JSON string
alias_operations_instance = AliasOperations.from_json(json)
# print the JSON string representation of the object
print AliasOperations.to_json()

# convert the object into a dict
alias_operations_dict = alias_operations_instance.to_dict()
# create an instance of AliasOperations from a dict
alias_operations_form_dict = alias_operations.from_dict(alias_operations_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


