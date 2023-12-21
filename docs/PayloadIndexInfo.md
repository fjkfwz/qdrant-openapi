# PayloadIndexInfo

Display payload field type & index information

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data_type** | [**PayloadSchemaType**](PayloadSchemaType.md) |  | 
**params** | [**TextIndexParams**](TextIndexParams.md) |  | [optional] 
**points** | **int** | Number of points indexed with this index | 

## Example

```python
from openapi_client.models.payload_index_info import PayloadIndexInfo

# TODO update the JSON string below
json = "{}"
# create an instance of PayloadIndexInfo from a JSON string
payload_index_info_instance = PayloadIndexInfo.from_json(json)
# print the JSON string representation of the object
print PayloadIndexInfo.to_json()

# convert the object into a dict
payload_index_info_dict = payload_index_info_instance.to_dict()
# create an instance of PayloadIndexInfo from a dict
payload_index_info_form_dict = payload_index_info.from_dict(payload_index_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


