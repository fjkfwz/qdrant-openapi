# CollectionsAggregatedTelemetry


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vectors** | **int** |  | 
**optimizers_status** | [**OptimizersStatus**](OptimizersStatus.md) |  | 
**params** | [**CollectionParams**](CollectionParams.md) |  | 

## Example

```python
from openapi_client.models.collections_aggregated_telemetry import CollectionsAggregatedTelemetry

# TODO update the JSON string below
json = "{}"
# create an instance of CollectionsAggregatedTelemetry from a JSON string
collections_aggregated_telemetry_instance = CollectionsAggregatedTelemetry.from_json(json)
# print the JSON string representation of the object
print CollectionsAggregatedTelemetry.to_json()

# convert the object into a dict
collections_aggregated_telemetry_dict = collections_aggregated_telemetry_instance.to_dict()
# create an instance of CollectionsAggregatedTelemetry from a dict
collections_aggregated_telemetry_form_dict = collections_aggregated_telemetry.from_dict(collections_aggregated_telemetry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


