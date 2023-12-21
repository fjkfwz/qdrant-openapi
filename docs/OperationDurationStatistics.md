# OperationDurationStatistics


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | 
**fail_count** | **int** |  | [optional] 
**avg_duration_micros** | **float** |  | [optional] 
**min_duration_micros** | **float** |  | [optional] 
**max_duration_micros** | **float** |  | [optional] 
**last_responded** | **datetime** |  | [optional] 

## Example

```python
from openapi_client.models.operation_duration_statistics import OperationDurationStatistics

# TODO update the JSON string below
json = "{}"
# create an instance of OperationDurationStatistics from a JSON string
operation_duration_statistics_instance = OperationDurationStatistics.from_json(json)
# print the JSON string representation of the object
print OperationDurationStatistics.to_json()

# convert the object into a dict
operation_duration_statistics_dict = operation_duration_statistics_instance.to_dict()
# create an instance of OperationDurationStatistics from a dict
operation_duration_statistics_form_dict = operation_duration_statistics.from_dict(operation_duration_statistics_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


