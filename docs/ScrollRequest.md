# ScrollRequest

Scroll request - paginate over all points which matches given condition

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**shard_key** | [**ShardKeySelector**](ShardKeySelector.md) |  | [optional] 
**offset** | [**ExtendedPointId**](ExtendedPointId.md) |  | [optional] 
**limit** | **int** | Page size. Default: 10 | [optional] 
**filter** | [**Filter**](Filter.md) |  | [optional] 
**with_payload** | [**WithPayloadInterface**](WithPayloadInterface.md) |  | [optional] 
**with_vector** | [**WithVector**](WithVector.md) |  | [optional] 

## Example

```python
from openapi_client.models.scroll_request import ScrollRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ScrollRequest from a JSON string
scroll_request_instance = ScrollRequest.from_json(json)
# print the JSON string representation of the object
print ScrollRequest.to_json()

# convert the object into a dict
scroll_request_dict = scroll_request_instance.to_dict()
# create an instance of ScrollRequest from a dict
scroll_request_form_dict = scroll_request.from_dict(scroll_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


