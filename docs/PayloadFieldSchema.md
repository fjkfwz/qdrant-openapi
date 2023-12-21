# PayloadFieldSchema


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**TextIndexType**](TextIndexType.md) |  | 
**tokenizer** | [**TokenizerType**](TokenizerType.md) |  | [optional] 
**min_token_len** | **int** |  | [optional] 
**max_token_len** | **int** |  | [optional] 
**lowercase** | **bool** | If true, lowercase all tokens. Default: true | [optional] 

## Example

```python
from openapi_client.models.payload_field_schema import PayloadFieldSchema

# TODO update the JSON string below
json = "{}"
# create an instance of PayloadFieldSchema from a JSON string
payload_field_schema_instance = PayloadFieldSchema.from_json(json)
# print the JSON string representation of the object
print PayloadFieldSchema.to_json()

# convert the object into a dict
payload_field_schema_dict = payload_field_schema_instance.to_dict()
# create an instance of PayloadFieldSchema from a dict
payload_field_schema_form_dict = payload_field_schema.from_dict(payload_field_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


