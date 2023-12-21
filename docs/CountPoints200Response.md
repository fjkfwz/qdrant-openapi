# CountPoints200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**time** | **float** | Time spent to process this request | [optional] 
**status** | **str** |  | [optional] 
**result** | [**CountResult**](CountResult.md) |  | [optional] 

## Example

```python
from qdrant_openapi.models.count_points200_response import CountPoints200Response

# TODO update the JSON string below
json = "{}"
# create an instance of CountPoints200Response from a JSON string
count_points200_response_instance = CountPoints200Response.from_json(json)
# print the JSON string representation of the object
print CountPoints200Response.to_json()

# convert the object into a dict
count_points200_response_dict = count_points200_response_instance.to_dict()
# create an instance of CountPoints200Response from a dict
count_points200_response_form_dict = count_points200_response.from_dict(count_points200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


