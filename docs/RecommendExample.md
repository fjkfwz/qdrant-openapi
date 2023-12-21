# RecommendExample


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**indices** | **List[int]** | indices must be unique | 
**values** | **List[float]** | values and indices must be the same length | 

## Example

```python
from qdrant_openapi.models.recommend_example import RecommendExample

# TODO update the JSON string below
json = "{}"
# create an instance of RecommendExample from a JSON string
recommend_example_instance = RecommendExample.from_json(json)
# print the JSON string representation of the object
print RecommendExample.to_json()

# convert the object into a dict
recommend_example_dict = recommend_example_instance.to_dict()
# create an instance of RecommendExample from a dict
recommend_example_form_dict = recommend_example.from_dict(recommend_example_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


