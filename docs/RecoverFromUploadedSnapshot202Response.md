# RecoverFromUploadedSnapshot202Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**time** | **float** | Time spent to process this request | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from qdrant_openapi.models.recover_from_uploaded_snapshot202_response import RecoverFromUploadedSnapshot202Response

# TODO update the JSON string below
json = "{}"
# create an instance of RecoverFromUploadedSnapshot202Response from a JSON string
recover_from_uploaded_snapshot202_response_instance = RecoverFromUploadedSnapshot202Response.from_json(json)
# print the JSON string representation of the object
print RecoverFromUploadedSnapshot202Response.to_json()

# convert the object into a dict
recover_from_uploaded_snapshot202_response_dict = recover_from_uploaded_snapshot202_response_instance.to_dict()
# create an instance of RecoverFromUploadedSnapshot202Response from a dict
recover_from_uploaded_snapshot202_response_form_dict = recover_from_uploaded_snapshot202_response.from_dict(recover_from_uploaded_snapshot202_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


