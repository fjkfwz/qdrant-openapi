# CountResult


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | Number of points which satisfy the conditions | 

## Example

```python
from qdrant_openapi.models.count_result import CountResult

# TODO update the JSON string below
json = "{}"
# create an instance of CountResult from a JSON string
count_result_instance = CountResult.from_json(json)
# print the JSON string representation of the object
print CountResult.to_json()

# convert the object into a dict
count_result_dict = count_result_instance.to_dict()
# create an instance of CountResult from a dict
count_result_form_dict = count_result.from_dict(count_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


