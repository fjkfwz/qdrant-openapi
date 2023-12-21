# ReadConsistency

Read consistency parameter  Defines how many replicas should be queried to get the result  * `N` - send N random request and return points, which present on all of them  * `majority` - send N/2+1 random request and return points, which present on all of them  * `quorum` - send requests to all nodes and return points which present on majority of them  * `all` - send requests to all nodes and return points which present on all of them  Default value is `Factor(1)`

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from openapi_client.models.read_consistency import ReadConsistency

# TODO update the JSON string below
json = "{}"
# create an instance of ReadConsistency from a JSON string
read_consistency_instance = ReadConsistency.from_json(json)
# print the JSON string representation of the object
print ReadConsistency.to_json()

# convert the object into a dict
read_consistency_dict = read_consistency_instance.to_dict()
# create an instance of ReadConsistency from a dict
read_consistency_form_dict = read_consistency.from_dict(read_consistency_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


