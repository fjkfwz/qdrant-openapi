# LookupLocation

Defines a location to use for looking up the vector. Specifies collection and vector field name.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**collection** | **str** | Name of the collection used for lookup | 
**vector** | **str** | Optional name of the vector field within the collection. If not provided, the default vector field will be used. | [optional] 
**shard_key** | [**ShardKeySelector**](ShardKeySelector.md) |  | [optional] 

## Example

```python
from qdrant_openapi.models.lookup_location import LookupLocation

# TODO update the JSON string below
json = "{}"
# create an instance of LookupLocation from a JSON string
lookup_location_instance = LookupLocation.from_json(json)
# print the JSON string representation of the object
print LookupLocation.to_json()

# convert the object into a dict
lookup_location_dict = lookup_location_instance.to_dict()
# create an instance of LookupLocation from a dict
lookup_location_form_dict = lookup_location.from_dict(lookup_location_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


