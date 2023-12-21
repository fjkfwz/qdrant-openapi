# WebApiTelemetry


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**responses** | **Dict[str, Dict[str, OperationDurationStatistics]]** |  | 

## Example

```python
from openapi_client.models.web_api_telemetry import WebApiTelemetry

# TODO update the JSON string below
json = "{}"
# create an instance of WebApiTelemetry from a JSON string
web_api_telemetry_instance = WebApiTelemetry.from_json(json)
# print the JSON string representation of the object
print WebApiTelemetry.to_json()

# convert the object into a dict
web_api_telemetry_dict = web_api_telemetry_instance.to_dict()
# create an instance of WebApiTelemetry from a dict
web_api_telemetry_form_dict = web_api_telemetry.from_dict(web_api_telemetry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


