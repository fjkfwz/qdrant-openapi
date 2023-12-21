# CollectionClusterInfo200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**time** | **float** | Time spent to process this request | [optional] 
**status** | **str** |  | [optional] 
**result** | [**CollectionClusterInfo**](CollectionClusterInfo.md) |  | [optional] 

## Example

```python
from openapi_client.models.collection_cluster_info200_response import CollectionClusterInfo200Response

# TODO update the JSON string below
json = "{}"
# create an instance of CollectionClusterInfo200Response from a JSON string
collection_cluster_info200_response_instance = CollectionClusterInfo200Response.from_json(json)
# print the JSON string representation of the object
print CollectionClusterInfo200Response.to_json()

# convert the object into a dict
collection_cluster_info200_response_dict = collection_cluster_info200_response_instance.to_dict()
# create an instance of CollectionClusterInfo200Response from a dict
collection_cluster_info200_response_form_dict = collection_cluster_info200_response.from_dict(collection_cluster_info200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


