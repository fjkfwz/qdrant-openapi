# CreateSnapshot200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**time** | **float** | Time spent to process this request | [optional] 
**status** | **str** |  | [optional] 
**result** | [**SnapshotDescription**](SnapshotDescription.md) |  | [optional] 

## Example

```python
from openapi_client.models.create_snapshot200_response import CreateSnapshot200Response

# TODO update the JSON string below
json = "{}"
# create an instance of CreateSnapshot200Response from a JSON string
create_snapshot200_response_instance = CreateSnapshot200Response.from_json(json)
# print the JSON string representation of the object
print CreateSnapshot200Response.to_json()

# convert the object into a dict
create_snapshot200_response_dict = create_snapshot200_response_instance.to_dict()
# create an instance of CreateSnapshot200Response from a dict
create_snapshot200_response_form_dict = create_snapshot200_response.from_dict(create_snapshot200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


