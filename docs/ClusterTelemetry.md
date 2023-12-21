# ClusterTelemetry


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** |  | 
**status** | [**ClusterStatusTelemetry**](ClusterStatusTelemetry.md) |  | [optional] 
**config** | [**ClusterConfigTelemetry**](ClusterConfigTelemetry.md) |  | [optional] 

## Example

```python
from openapi_client.models.cluster_telemetry import ClusterTelemetry

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterTelemetry from a JSON string
cluster_telemetry_instance = ClusterTelemetry.from_json(json)
# print the JSON string representation of the object
print ClusterTelemetry.to_json()

# convert the object into a dict
cluster_telemetry_dict = cluster_telemetry_instance.to_dict()
# create an instance of ClusterTelemetry from a dict
cluster_telemetry_form_dict = cluster_telemetry.from_dict(cluster_telemetry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


