# RunningEnvironmentTelemetry


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**distribution** | **str** |  | [optional] 
**distribution_version** | **str** |  | [optional] 
**is_docker** | **bool** |  | 
**cores** | **int** |  | [optional] 
**ram_size** | **int** |  | [optional] 
**disk_size** | **int** |  | [optional] 
**cpu_flags** | **str** |  | 

## Example

```python
from qdrant_openapi.models.running_environment_telemetry import RunningEnvironmentTelemetry

# TODO update the JSON string below
json = "{}"
# create an instance of RunningEnvironmentTelemetry from a JSON string
running_environment_telemetry_instance = RunningEnvironmentTelemetry.from_json(json)
# print the JSON string representation of the object
print RunningEnvironmentTelemetry.to_json()

# convert the object into a dict
running_environment_telemetry_dict = running_environment_telemetry_instance.to_dict()
# create an instance of RunningEnvironmentTelemetry from a dict
running_environment_telemetry_form_dict = running_environment_telemetry.from_dict(running_environment_telemetry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


