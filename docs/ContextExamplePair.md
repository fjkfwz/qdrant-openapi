# ContextExamplePair


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**positive** | [**RecommendExample**](RecommendExample.md) |  | 
**negative** | [**RecommendExample**](RecommendExample.md) |  | 

## Example

```python
from qdrant_openapi.models.context_example_pair import ContextExamplePair

# TODO update the JSON string below
json = "{}"
# create an instance of ContextExamplePair from a JSON string
context_example_pair_instance = ContextExamplePair.from_json(json)
# print the JSON string representation of the object
print ContextExamplePair.to_json()

# convert the object into a dict
context_example_pair_dict = context_example_pair_instance.to_dict()
# create an instance of ContextExamplePair from a dict
context_example_pair_form_dict = context_example_pair.from_dict(context_example_pair_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


