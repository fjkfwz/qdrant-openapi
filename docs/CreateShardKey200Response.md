# CreateShardKey200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**time** | **float** | Time spent to process this request | [optional] 
**status** | **str** |  | [optional] 
**result** | **bool** |  | [optional] 

## Example

```python
from qdrant_openapi.models.create_shard_key200_response import CreateShardKey200Response

# TODO update the JSON string below
json = "{}"
# create an instance of CreateShardKey200Response from a JSON string
create_shard_key200_response_instance = CreateShardKey200Response.from_json(json)
# print the JSON string representation of the object
print CreateShardKey200Response.to_json()

# convert the object into a dict
create_shard_key200_response_dict = create_shard_key200_response_instance.to_dict()
# create an instance of CreateShardKey200Response from a dict
create_shard_key200_response_form_dict = create_shard_key200_response.from_dict(create_shard_key200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


