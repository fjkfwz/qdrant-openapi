# BatchUpdate200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**time** | **float** | Time spent to process this request | [optional] 
**status** | **str** |  | [optional] 
**result** | [**List[UpdateResult]**](UpdateResult.md) |  | [optional] 

## Example

```python
from openapi_client.models.batch_update200_response import BatchUpdate200Response

# TODO update the JSON string below
json = "{}"
# create an instance of BatchUpdate200Response from a JSON string
batch_update200_response_instance = BatchUpdate200Response.from_json(json)
# print the JSON string representation of the object
print BatchUpdate200Response.to_json()

# convert the object into a dict
batch_update200_response_dict = batch_update200_response_instance.to_dict()
# create an instance of BatchUpdate200Response from a dict
batch_update200_response_form_dict = batch_update200_response.from_dict(batch_update200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


