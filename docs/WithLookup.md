# WithLookup


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**collection** | **str** | Name of the collection to use for points lookup | 
**with_payload** | [**WithPayloadInterface**](WithPayloadInterface.md) |  | [optional] 
**with_vectors** | [**WithVector**](WithVector.md) |  | [optional] 

## Example

```python
from openapi_client.models.with_lookup import WithLookup

# TODO update the JSON string below
json = "{}"
# create an instance of WithLookup from a JSON string
with_lookup_instance = WithLookup.from_json(json)
# print the JSON string representation of the object
print WithLookup.to_json()

# convert the object into a dict
with_lookup_dict = with_lookup_instance.to_dict()
# create an instance of WithLookup from a dict
with_lookup_form_dict = with_lookup.from_dict(with_lookup_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


