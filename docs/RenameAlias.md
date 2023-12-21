# RenameAlias

Change alias to a new one

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**old_alias_name** | **str** |  | 
**new_alias_name** | **str** |  | 

## Example

```python
from openapi_client.models.rename_alias import RenameAlias

# TODO update the JSON string below
json = "{}"
# create an instance of RenameAlias from a JSON string
rename_alias_instance = RenameAlias.from_json(json)
# print the JSON string representation of the object
print RenameAlias.to_json()

# convert the object into a dict
rename_alias_dict = rename_alias_instance.to_dict()
# create an instance of RenameAlias from a dict
rename_alias_form_dict = rename_alias.from_dict(rename_alias_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


