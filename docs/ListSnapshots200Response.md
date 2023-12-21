# ListSnapshots200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**time** | **float** | Time spent to process this request | [optional] 
**status** | **str** |  | [optional] 
**result** | [**List[SnapshotDescription]**](SnapshotDescription.md) |  | [optional] 

## Example

```python
from qdrant_openapi.models.list_snapshots200_response import ListSnapshots200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ListSnapshots200Response from a JSON string
list_snapshots200_response_instance = ListSnapshots200Response.from_json(json)
# print the JSON string representation of the object
print ListSnapshots200Response.to_json()

# convert the object into a dict
list_snapshots200_response_dict = list_snapshots200_response_instance.to_dict()
# create an instance of ListSnapshots200Response from a dict
list_snapshots200_response_form_dict = list_snapshots200_response.from_dict(list_snapshots200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


