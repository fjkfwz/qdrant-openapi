# ErrorResponseStatus


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | **str** | Description of the occurred error. | [optional] 

## Example

```python
from openapi_client.models.error_response_status import ErrorResponseStatus

# TODO update the JSON string below
json = "{}"
# create an instance of ErrorResponseStatus from a JSON string
error_response_status_instance = ErrorResponseStatus.from_json(json)
# print the JSON string representation of the object
print ErrorResponseStatus.to_json()

# convert the object into a dict
error_response_status_dict = error_response_status_instance.to_dict()
# create an instance of ErrorResponseStatus from a dict
error_response_status_form_dict = error_response_status.from_dict(error_response_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


