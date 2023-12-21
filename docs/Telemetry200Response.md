# Telemetry200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**time** | **float** | Time spent to process this request | [optional] 
**status** | **str** |  | [optional] 
**result** | [**TelemetryData**](TelemetryData.md) |  | [optional] 

## Example

```python
from openapi_client.models.telemetry200_response import Telemetry200Response

# TODO update the JSON string below
json = "{}"
# create an instance of Telemetry200Response from a JSON string
telemetry200_response_instance = Telemetry200Response.from_json(json)
# print the JSON string representation of the object
print Telemetry200Response.to_json()

# convert the object into a dict
telemetry200_response_dict = telemetry200_response_instance.to_dict()
# create an instance of Telemetry200Response from a dict
telemetry200_response_form_dict = telemetry200_response.from_dict(telemetry200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


