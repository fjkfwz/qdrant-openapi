# GetLocks200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**time** | **float** | Time spent to process this request | [optional] 
**status** | **str** |  | [optional] 
**result** | [**LocksOption**](LocksOption.md) |  | [optional] 

## Example

```python
from qdrant_openapi.models.get_locks200_response import GetLocks200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetLocks200Response from a JSON string
get_locks200_response_instance = GetLocks200Response.from_json(json)
# print the JSON string representation of the object
print GetLocks200Response.to_json()

# convert the object into a dict
get_locks200_response_dict = get_locks200_response_instance.to_dict()
# create an instance of GetLocks200Response from a dict
get_locks200_response_form_dict = get_locks200_response.from_dict(get_locks200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


