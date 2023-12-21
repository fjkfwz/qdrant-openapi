# WithLookupInterface


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**collection** | **str** | Name of the collection to use for points lookup | 
**with_payload** | [**WithPayloadInterface**](WithPayloadInterface.md) |  | [optional] 
**with_vectors** | [**WithVector**](WithVector.md) |  | [optional] 

## Example

```python
from openapi_client.models.with_lookup_interface import WithLookupInterface

# TODO update the JSON string below
json = "{}"
# create an instance of WithLookupInterface from a JSON string
with_lookup_interface_instance = WithLookupInterface.from_json(json)
# print the JSON string representation of the object
print WithLookupInterface.to_json()

# convert the object into a dict
with_lookup_interface_dict = with_lookup_interface_instance.to_dict()
# create an instance of WithLookupInterface from a dict
with_lookup_interface_form_dict = with_lookup_interface.from_dict(with_lookup_interface_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


