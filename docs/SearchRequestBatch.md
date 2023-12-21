# SearchRequestBatch


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**searches** | [**List[SearchRequest]**](SearchRequest.md) |  | 

## Example

```python
from openapi_client.models.search_request_batch import SearchRequestBatch

# TODO update the JSON string below
json = "{}"
# create an instance of SearchRequestBatch from a JSON string
search_request_batch_instance = SearchRequestBatch.from_json(json)
# print the JSON string representation of the object
print SearchRequestBatch.to_json()

# convert the object into a dict
search_request_batch_dict = search_request_batch_instance.to_dict()
# create an instance of SearchRequestBatch from a dict
search_request_batch_form_dict = search_request_batch.from_dict(search_request_batch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


