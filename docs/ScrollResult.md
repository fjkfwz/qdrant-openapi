# ScrollResult

Result of the points read request

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**points** | [**List[Record]**](Record.md) | List of retrieved points | 
**next_page_offset** | [**ExtendedPointId**](ExtendedPointId.md) |  | [optional] 

## Example

```python
from openapi_client.models.scroll_result import ScrollResult

# TODO update the JSON string below
json = "{}"
# create an instance of ScrollResult from a JSON string
scroll_result_instance = ScrollResult.from_json(json)
# print the JSON string representation of the object
print ScrollResult.to_json()

# convert the object into a dict
scroll_result_dict = scroll_result_instance.to_dict()
# create an instance of ScrollResult from a dict
scroll_result_form_dict = scroll_result.from_dict(scroll_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


