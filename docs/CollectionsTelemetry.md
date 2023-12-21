# CollectionsTelemetry


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**number_of_collections** | **int** |  | 
**collections** | [**List[CollectionTelemetryEnum]**](CollectionTelemetryEnum.md) |  | [optional] 

## Example

```python
from openapi_client.models.collections_telemetry import CollectionsTelemetry

# TODO update the JSON string below
json = "{}"
# create an instance of CollectionsTelemetry from a JSON string
collections_telemetry_instance = CollectionsTelemetry.from_json(json)
# print the JSON string representation of the object
print CollectionsTelemetry.to_json()

# convert the object into a dict
collections_telemetry_dict = collections_telemetry_instance.to_dict()
# create an instance of CollectionsTelemetry from a dict
collections_telemetry_form_dict = collections_telemetry.from_dict(collections_telemetry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


