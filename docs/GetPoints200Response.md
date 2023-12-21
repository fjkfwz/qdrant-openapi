# GetPoints200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**time** | **float** | Time spent to process this request | [optional] 
**status** | **str** |  | [optional] 
**result** | [**List[Record]**](Record.md) |  | [optional] 

## Example

```python
from qdrant_openapi.models.get_points200_response import GetPoints200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetPoints200Response from a JSON string
get_points200_response_instance = GetPoints200Response.from_json(json)
# print the JSON string representation of the object
print GetPoints200Response.to_json()

# convert the object into a dict
get_points200_response_dict = get_points200_response_instance.to_dict()
# create an instance of GetPoints200Response from a dict
get_points200_response_form_dict = get_points200_response.from_dict(get_points200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


