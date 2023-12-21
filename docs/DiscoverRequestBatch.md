# DiscoverRequestBatch


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**searches** | [**List[DiscoverRequest]**](DiscoverRequest.md) |  | 

## Example

```python
from openapi_client.models.discover_request_batch import DiscoverRequestBatch

# TODO update the JSON string below
json = "{}"
# create an instance of DiscoverRequestBatch from a JSON string
discover_request_batch_instance = DiscoverRequestBatch.from_json(json)
# print the JSON string representation of the object
print DiscoverRequestBatch.to_json()

# convert the object into a dict
discover_request_batch_dict = discover_request_batch_instance.to_dict()
# create an instance of DiscoverRequestBatch from a dict
discover_request_batch_form_dict = discover_request_batch.from_dict(discover_request_batch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


