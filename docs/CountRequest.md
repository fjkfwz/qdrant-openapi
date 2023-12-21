# CountRequest

Count Request Counts the number of points which satisfy the given filter. If filter is not provided, the count of all points in the collection will be returned.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**shard_key** | [**ShardKeySelector**](ShardKeySelector.md) |  | [optional] 
**filter** | [**Filter**](Filter.md) |  | [optional] 
**exact** | **bool** | If true, count exact number of points. If false, count approximate number of points faster. Approximate count might be unreliable during the indexing process. Default: true | [optional] [default to True]

## Example

```python
from openapi_client.models.count_request import CountRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CountRequest from a JSON string
count_request_instance = CountRequest.from_json(json)
# print the JSON string representation of the object
print CountRequest.to_json()

# convert the object into a dict
count_request_dict = count_request_instance.to_dict()
# create an instance of CountRequest from a dict
count_request_form_dict = count_request.from_dict(count_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


