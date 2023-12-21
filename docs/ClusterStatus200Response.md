# ClusterStatus200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**time** | **float** | Time spent to process this request | [optional] 
**status** | **str** |  | [optional] 
**result** | [**ClusterStatus**](ClusterStatus.md) |  | [optional] 

## Example

```python
from qdrant_openapi.models.cluster_status200_response import ClusterStatus200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterStatus200Response from a JSON string
cluster_status200_response_instance = ClusterStatus200Response.from_json(json)
# print the JSON string representation of the object
print ClusterStatus200Response.to_json()

# convert the object into a dict
cluster_status200_response_dict = cluster_status200_response_instance.to_dict()
# create an instance of ClusterStatus200Response from a dict
cluster_status200_response_form_dict = cluster_status200_response.from_dict(cluster_status200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


