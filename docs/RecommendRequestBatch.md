# RecommendRequestBatch


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**searches** | [**List[RecommendRequest]**](RecommendRequest.md) |  | 

## Example

```python
from qdrant_openapi.models.recommend_request_batch import RecommendRequestBatch

# TODO update the JSON string below
json = "{}"
# create an instance of RecommendRequestBatch from a JSON string
recommend_request_batch_instance = RecommendRequestBatch.from_json(json)
# print the JSON string representation of the object
print RecommendRequestBatch.to_json()

# convert the object into a dict
recommend_request_batch_dict = recommend_request_batch_instance.to_dict()
# create an instance of RecommendRequestBatch from a dict
recommend_request_batch_form_dict = recommend_request_batch.from_dict(recommend_request_batch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


