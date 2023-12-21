# Vector


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**indices** | **List[int]** | indices must be unique | 
**values** | **List[float]** | values and indices must be the same length | 

## Example

```python
from openapi_client.models.vector import Vector

# TODO update the JSON string below
json = "{}"
# create an instance of Vector from a JSON string
vector_instance = Vector.from_json(json)
# print the JSON string representation of the object
print Vector.to_json()

# convert the object into a dict
vector_dict = vector_instance.to_dict()
# create an instance of Vector from a dict
vector_form_dict = vector.from_dict(vector_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


