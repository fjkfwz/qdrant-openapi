# FilterSelector


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filter** | [**Filter**](Filter.md) |  | 
**shard_key** | [**ShardKeySelector**](ShardKeySelector.md) |  | [optional] 

## Example

```python
from qdrant_openapi.models.filter_selector import FilterSelector

# TODO update the JSON string below
json = "{}"
# create an instance of FilterSelector from a JSON string
filter_selector_instance = FilterSelector.from_json(json)
# print the JSON string representation of the object
print FilterSelector.to_json()

# convert the object into a dict
filter_selector_dict = filter_selector_instance.to_dict()
# create an instance of FilterSelector from a dict
filter_selector_form_dict = filter_selector.from_dict(filter_selector_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


