# CreateFieldIndex200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**time** | **float** | Time spent to process this request | [optional] 
**status** | **str** |  | [optional] 
**result** | [**UpdateResult**](UpdateResult.md) |  | [optional] 

## Example

```python
from qdrant_openapi.models.create_field_index200_response import CreateFieldIndex200Response

# TODO update the JSON string below
json = "{}"
# create an instance of CreateFieldIndex200Response from a JSON string
create_field_index200_response_instance = CreateFieldIndex200Response.from_json(json)
# print the JSON string representation of the object
print CreateFieldIndex200Response.to_json()

# convert the object into a dict
create_field_index200_response_dict = create_field_index200_response_instance.to_dict()
# create an instance of CreateFieldIndex200Response from a dict
create_field_index200_response_form_dict = create_field_index200_response.from_dict(create_field_index200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


