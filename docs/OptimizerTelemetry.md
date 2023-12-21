# OptimizerTelemetry


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**OptimizersStatus**](OptimizersStatus.md) |  | 
**optimizations** | [**OperationDurationStatistics**](OperationDurationStatistics.md) |  | 
**log** | [**List[TrackerTelemetry]**](TrackerTelemetry.md) |  | 

## Example

```python
from qdrant_openapi.models.optimizer_telemetry import OptimizerTelemetry

# TODO update the JSON string below
json = "{}"
# create an instance of OptimizerTelemetry from a JSON string
optimizer_telemetry_instance = OptimizerTelemetry.from_json(json)
# print the JSON string representation of the object
print OptimizerTelemetry.to_json()

# convert the object into a dict
optimizer_telemetry_dict = optimizer_telemetry_instance.to_dict()
# create an instance of OptimizerTelemetry from a dict
optimizer_telemetry_form_dict = optimizer_telemetry.from_dict(optimizer_telemetry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


