# CreateAlias

Create alternative name for a collection. Collection will be available under both names for search, retrieve,

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**collection_name** | **str** |  | 
**alias_name** | **str** |  | 

## Example

```python
from openapi_client.models.create_alias import CreateAlias

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAlias from a JSON string
create_alias_instance = CreateAlias.from_json(json)
# print the JSON string representation of the object
print CreateAlias.to_json()

# convert the object into a dict
create_alias_dict = create_alias_instance.to_dict()
# create an instance of CreateAlias from a dict
create_alias_form_dict = create_alias.from_dict(create_alias_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


