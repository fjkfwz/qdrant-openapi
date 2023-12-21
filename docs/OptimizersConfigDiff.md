# OptimizersConfigDiff


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deleted_threshold** | **float** | The minimal fraction of deleted vectors in a segment, required to perform segment optimization | [optional] 
**vacuum_min_vector_number** | **int** | The minimal number of vectors in a segment, required to perform segment optimization | [optional] 
**default_segment_number** | **int** | Target amount of segments optimizer will try to keep. Real amount of segments may vary depending on multiple parameters: - Amount of stored points - Current write RPS  It is recommended to select default number of segments as a factor of the number of search threads, so that each segment would be handled evenly by one of the threads If &#x60;default_segment_number &#x3D; 0&#x60;, will be automatically selected by the number of available CPUs | [optional] 
**max_segment_size** | **int** | Do not create segments larger this size (in kilobytes). Large segments might require disproportionately long indexation times, therefore it makes sense to limit the size of segments.  If indexation speed have more priority for your - make this parameter lower. If search speed is more important - make this parameter higher. Note: 1Kb &#x3D; 1 vector of size 256 | [optional] 
**memmap_threshold** | **int** | Maximum size (in kilobytes) of vectors to store in-memory per segment. Segments larger than this threshold will be stored as read-only memmaped file.  Memmap storage is disabled by default, to enable it, set this threshold to a reasonable value.  To disable memmap storage, set this to &#x60;0&#x60;.  Note: 1Kb &#x3D; 1 vector of size 256 | [optional] 
**indexing_threshold** | **int** | Maximum size (in kilobytes) of vectors allowed for plain index, exceeding this threshold will enable vector indexing  Default value is 20,000, based on &lt;https://github.com/google-research/google-research/blob/master/scann/docs/algorithms.md&gt;.  To disable vector indexing, set to &#x60;0&#x60;.  Note: 1kB &#x3D; 1 vector of size 256. | [optional] 
**flush_interval_sec** | **int** | Minimum interval between forced flushes. | [optional] 
**max_optimization_threads** | **int** | Maximum available threads for optimization workers | [optional] 

## Example

```python
from openapi_client.models.optimizers_config_diff import OptimizersConfigDiff

# TODO update the JSON string below
json = "{}"
# create an instance of OptimizersConfigDiff from a JSON string
optimizers_config_diff_instance = OptimizersConfigDiff.from_json(json)
# print the JSON string representation of the object
print OptimizersConfigDiff.to_json()

# convert the object into a dict
optimizers_config_diff_dict = optimizers_config_diff_instance.to_dict()
# create an instance of OptimizersConfigDiff from a dict
optimizers_config_diff_form_dict = optimizers_config_diff.from_dict(optimizers_config_diff_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

