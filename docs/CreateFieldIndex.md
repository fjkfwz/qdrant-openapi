# CreateFieldIndex


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**field_name** | **str** |  | 
**field_schema** | [**PayloadFieldSchema**](PayloadFieldSchema.md) |  | [optional] 

## Example

```python
from openapi_client.models.create_field_index import CreateFieldIndex

# TODO update the JSON string below
json = "{}"
# create an instance of CreateFieldIndex from a JSON string
create_field_index_instance = CreateFieldIndex.from_json(json)
# print the JSON string representation of the object
print CreateFieldIndex.to_json()

# convert the object into a dict
create_field_index_dict = create_field_index_instance.to_dict()
# create an instance of CreateFieldIndex from a dict
create_field_index_form_dict = create_field_index.from_dict(create_field_index_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


