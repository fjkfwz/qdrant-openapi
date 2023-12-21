# ScrollPoints200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**time** | **float** | Time spent to process this request | [optional] 
**status** | **str** |  | [optional] 
**result** | [**ScrollResult**](ScrollResult.md) |  | [optional] 

## Example

```python
from qdrant_openapi.models.scroll_points200_response import ScrollPoints200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ScrollPoints200Response from a JSON string
scroll_points200_response_instance = ScrollPoints200Response.from_json(json)
# print the JSON string representation of the object
print ScrollPoints200Response.to_json()

# convert the object into a dict
scroll_points200_response_dict = scroll_points200_response_instance.to_dict()
# create an instance of ScrollPoints200Response from a dict
scroll_points200_response_form_dict = scroll_points200_response.from_dict(scroll_points200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


