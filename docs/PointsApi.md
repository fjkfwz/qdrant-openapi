# qdrant_openapi.PointsApi

All URIs are relative to *http://localhost:6333*

Method | HTTP request | Description
------------- | ------------- | -------------
[**batch_update**](PointsApi.md#batch_update) | **POST** /collections/{collection_name}/points/batch | Batch update points
[**clear_payload**](PointsApi.md#clear_payload) | **POST** /collections/{collection_name}/points/payload/clear | Clear payload
[**count_points**](PointsApi.md#count_points) | **POST** /collections/{collection_name}/points/count | Count points
[**delete_payload**](PointsApi.md#delete_payload) | **POST** /collections/{collection_name}/points/payload/delete | Delete payload
[**delete_points**](PointsApi.md#delete_points) | **POST** /collections/{collection_name}/points/delete | Delete points
[**delete_vectors**](PointsApi.md#delete_vectors) | **POST** /collections/{collection_name}/points/vectors/delete | Delete vectors
[**discover_batch_points**](PointsApi.md#discover_batch_points) | **POST** /collections/{collection_name}/points/discover/batch | Discover batch points
[**discover_points**](PointsApi.md#discover_points) | **POST** /collections/{collection_name}/points/discover | Discover points
[**get_point**](PointsApi.md#get_point) | **GET** /collections/{collection_name}/points/{id} | Get point
[**get_points**](PointsApi.md#get_points) | **POST** /collections/{collection_name}/points | Get points
[**overwrite_payload**](PointsApi.md#overwrite_payload) | **PUT** /collections/{collection_name}/points/payload | Overwrite payload
[**recommend_batch_points**](PointsApi.md#recommend_batch_points) | **POST** /collections/{collection_name}/points/recommend/batch | Recommend batch points
[**recommend_point_groups**](PointsApi.md#recommend_point_groups) | **POST** /collections/{collection_name}/points/recommend/groups | Recommend point groups
[**recommend_points**](PointsApi.md#recommend_points) | **POST** /collections/{collection_name}/points/recommend | Recommend points
[**scroll_points**](PointsApi.md#scroll_points) | **POST** /collections/{collection_name}/points/scroll | Scroll points
[**search_batch_points**](PointsApi.md#search_batch_points) | **POST** /collections/{collection_name}/points/search/batch | Search batch points
[**search_point_groups**](PointsApi.md#search_point_groups) | **POST** /collections/{collection_name}/points/search/groups | Search point groups
[**search_points**](PointsApi.md#search_points) | **POST** /collections/{collection_name}/points/search | Search points
[**set_payload**](PointsApi.md#set_payload) | **POST** /collections/{collection_name}/points/payload | Set payload
[**update_vectors**](PointsApi.md#update_vectors) | **PUT** /collections/{collection_name}/points/vectors | Update vectors
[**upsert_points**](PointsApi.md#upsert_points) | **PUT** /collections/{collection_name}/points | Upsert points


# **batch_update**
> BatchUpdate200Response batch_update(collection_name, wait=wait, ordering=ordering, update_operations=update_operations)

Batch update points

Apply a series of update operations for points, vectors and payloads

### Example

* Api Key Authentication (api-key):
* Bearer Authentication (bearerAuth):
```python
import time
import os
import qdrant_openapi
from qdrant_openapi.models.batch_update200_response import BatchUpdate200Response
from qdrant_openapi.models.update_operations import UpdateOperations
from qdrant_openapi.models.write_ordering import WriteOrdering
from qdrant_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:6333
# See configuration.py for a list of all supported configuration parameters.
configuration = qdrant_openapi.Configuration(
    host = "http://localhost:6333"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api-key
configuration.api_key['api-key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'

# Configure Bearer authorization: bearerAuth
configuration = qdrant_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with qdrant_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = qdrant_openapi.PointsApi(api_client)
    collection_name = 'collection_name_example' # str | Name of the collection to apply operations on
    wait = True # bool | If true, wait for changes to actually happen (optional)
    ordering = qdrant_openapi.WriteOrdering() # WriteOrdering | define ordering guarantees for the operation (optional)
    update_operations = qdrant_openapi.UpdateOperations() # UpdateOperations | update operations (optional)

    try:
        # Batch update points
        api_response = api_instance.batch_update(collection_name, wait=wait, ordering=ordering, update_operations=update_operations)
        print("The response of PointsApi->batch_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PointsApi->batch_update: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection_name** | **str**| Name of the collection to apply operations on | 
 **wait** | **bool**| If true, wait for changes to actually happen | [optional] 
 **ordering** | [**WriteOrdering**](.md)| define ordering guarantees for the operation | [optional] 
 **update_operations** | [**UpdateOperations**](UpdateOperations.md)| update operations | [optional] 

### Return type

[**BatchUpdate200Response**](BatchUpdate200Response.md)

### Authorization

[api-key](../README.md#api-key), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**4XX** | error |  -  |
**0** | error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **clear_payload**
> CreateFieldIndex200Response clear_payload(collection_name, wait=wait, ordering=ordering, points_selector=points_selector)

Clear payload

Remove all payload for specified points

### Example

* Api Key Authentication (api-key):
* Bearer Authentication (bearerAuth):
```python
import time
import os
import qdrant_openapi
from qdrant_openapi.models.create_field_index200_response import CreateFieldIndex200Response
from qdrant_openapi.models.points_selector import PointsSelector
from qdrant_openapi.models.write_ordering import WriteOrdering
from qdrant_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:6333
# See configuration.py for a list of all supported configuration parameters.
configuration = qdrant_openapi.Configuration(
    host = "http://localhost:6333"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api-key
configuration.api_key['api-key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'

# Configure Bearer authorization: bearerAuth
configuration = qdrant_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with qdrant_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = qdrant_openapi.PointsApi(api_client)
    collection_name = 'collection_name_example' # str | Name of the collection to clear payload from
    wait = True # bool | If true, wait for changes to actually happen (optional)
    ordering = qdrant_openapi.WriteOrdering() # WriteOrdering | define ordering guarantees for the operation (optional)
    points_selector = qdrant_openapi.PointsSelector() # PointsSelector | clear payload on points (optional)

    try:
        # Clear payload
        api_response = api_instance.clear_payload(collection_name, wait=wait, ordering=ordering, points_selector=points_selector)
        print("The response of PointsApi->clear_payload:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PointsApi->clear_payload: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection_name** | **str**| Name of the collection to clear payload from | 
 **wait** | **bool**| If true, wait for changes to actually happen | [optional] 
 **ordering** | [**WriteOrdering**](.md)| define ordering guarantees for the operation | [optional] 
 **points_selector** | [**PointsSelector**](PointsSelector.md)| clear payload on points | [optional] 

### Return type

[**CreateFieldIndex200Response**](CreateFieldIndex200Response.md)

### Authorization

[api-key](../README.md#api-key), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**4XX** | error |  -  |
**0** | error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **count_points**
> CountPoints200Response count_points(collection_name, count_request=count_request)

Count points

Count points which matches given filtering condition

### Example

* Api Key Authentication (api-key):
* Bearer Authentication (bearerAuth):
```python
import time
import os
import qdrant_openapi
from qdrant_openapi.models.count_points200_response import CountPoints200Response
from qdrant_openapi.models.count_request import CountRequest
from qdrant_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:6333
# See configuration.py for a list of all supported configuration parameters.
configuration = qdrant_openapi.Configuration(
    host = "http://localhost:6333"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api-key
configuration.api_key['api-key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'

# Configure Bearer authorization: bearerAuth
configuration = qdrant_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with qdrant_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = qdrant_openapi.PointsApi(api_client)
    collection_name = 'collection_name_example' # str | Name of the collection to count in
    count_request = qdrant_openapi.CountRequest() # CountRequest | Request counts of points which matches given filtering condition (optional)

    try:
        # Count points
        api_response = api_instance.count_points(collection_name, count_request=count_request)
        print("The response of PointsApi->count_points:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PointsApi->count_points: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection_name** | **str**| Name of the collection to count in | 
 **count_request** | [**CountRequest**](CountRequest.md)| Request counts of points which matches given filtering condition | [optional] 

### Return type

[**CountPoints200Response**](CountPoints200Response.md)

### Authorization

[api-key](../README.md#api-key), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**4XX** | error |  -  |
**0** | error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_payload**
> CreateFieldIndex200Response delete_payload(collection_name, wait=wait, ordering=ordering, delete_payload=delete_payload)

Delete payload

Delete specified key payload for points

### Example

* Api Key Authentication (api-key):
* Bearer Authentication (bearerAuth):
```python
import time
import os
import qdrant_openapi
from qdrant_openapi.models.create_field_index200_response import CreateFieldIndex200Response
from qdrant_openapi.models.delete_payload import DeletePayload
from qdrant_openapi.models.write_ordering import WriteOrdering
from qdrant_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:6333
# See configuration.py for a list of all supported configuration parameters.
configuration = qdrant_openapi.Configuration(
    host = "http://localhost:6333"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api-key
configuration.api_key['api-key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'

# Configure Bearer authorization: bearerAuth
configuration = qdrant_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with qdrant_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = qdrant_openapi.PointsApi(api_client)
    collection_name = 'collection_name_example' # str | Name of the collection to delete from
    wait = True # bool | If true, wait for changes to actually happen (optional)
    ordering = qdrant_openapi.WriteOrdering() # WriteOrdering | define ordering guarantees for the operation (optional)
    delete_payload = qdrant_openapi.DeletePayload() # DeletePayload | delete payload on points (optional)

    try:
        # Delete payload
        api_response = api_instance.delete_payload(collection_name, wait=wait, ordering=ordering, delete_payload=delete_payload)
        print("The response of PointsApi->delete_payload:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PointsApi->delete_payload: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection_name** | **str**| Name of the collection to delete from | 
 **wait** | **bool**| If true, wait for changes to actually happen | [optional] 
 **ordering** | [**WriteOrdering**](.md)| define ordering guarantees for the operation | [optional] 
 **delete_payload** | [**DeletePayload**](DeletePayload.md)| delete payload on points | [optional] 

### Return type

[**CreateFieldIndex200Response**](CreateFieldIndex200Response.md)

### Authorization

[api-key](../README.md#api-key), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**4XX** | error |  -  |
**0** | error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_points**
> CreateFieldIndex200Response delete_points(collection_name, wait=wait, ordering=ordering, points_selector=points_selector)

Delete points

Delete points

### Example

* Api Key Authentication (api-key):
* Bearer Authentication (bearerAuth):
```python
import time
import os
import qdrant_openapi
from qdrant_openapi.models.create_field_index200_response import CreateFieldIndex200Response
from qdrant_openapi.models.points_selector import PointsSelector
from qdrant_openapi.models.write_ordering import WriteOrdering
from qdrant_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:6333
# See configuration.py for a list of all supported configuration parameters.
configuration = qdrant_openapi.Configuration(
    host = "http://localhost:6333"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api-key
configuration.api_key['api-key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'

# Configure Bearer authorization: bearerAuth
configuration = qdrant_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with qdrant_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = qdrant_openapi.PointsApi(api_client)
    collection_name = 'collection_name_example' # str | Name of the collection to delete from
    wait = True # bool | If true, wait for changes to actually happen (optional)
    ordering = qdrant_openapi.WriteOrdering() # WriteOrdering | define ordering guarantees for the operation (optional)
    points_selector = qdrant_openapi.PointsSelector() # PointsSelector | Operation to perform on points (optional)

    try:
        # Delete points
        api_response = api_instance.delete_points(collection_name, wait=wait, ordering=ordering, points_selector=points_selector)
        print("The response of PointsApi->delete_points:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PointsApi->delete_points: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection_name** | **str**| Name of the collection to delete from | 
 **wait** | **bool**| If true, wait for changes to actually happen | [optional] 
 **ordering** | [**WriteOrdering**](.md)| define ordering guarantees for the operation | [optional] 
 **points_selector** | [**PointsSelector**](PointsSelector.md)| Operation to perform on points | [optional] 

### Return type

[**CreateFieldIndex200Response**](CreateFieldIndex200Response.md)

### Authorization

[api-key](../README.md#api-key), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**4XX** | error |  -  |
**0** | error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_vectors**
> CreateFieldIndex200Response delete_vectors(collection_name, wait=wait, ordering=ordering, delete_vectors=delete_vectors)

Delete vectors

Delete named vectors from the given points.

### Example

* Api Key Authentication (api-key):
* Bearer Authentication (bearerAuth):
```python
import time
import os
import qdrant_openapi
from qdrant_openapi.models.create_field_index200_response import CreateFieldIndex200Response
from qdrant_openapi.models.delete_vectors import DeleteVectors
from qdrant_openapi.models.write_ordering import WriteOrdering
from qdrant_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:6333
# See configuration.py for a list of all supported configuration parameters.
configuration = qdrant_openapi.Configuration(
    host = "http://localhost:6333"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api-key
configuration.api_key['api-key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'

# Configure Bearer authorization: bearerAuth
configuration = qdrant_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with qdrant_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = qdrant_openapi.PointsApi(api_client)
    collection_name = 'collection_name_example' # str | Name of the collection to delete from
    wait = True # bool | If true, wait for changes to actually happen (optional)
    ordering = qdrant_openapi.WriteOrdering() # WriteOrdering | define ordering guarantees for the operation (optional)
    delete_vectors = qdrant_openapi.DeleteVectors() # DeleteVectors | Delete named vectors from points (optional)

    try:
        # Delete vectors
        api_response = api_instance.delete_vectors(collection_name, wait=wait, ordering=ordering, delete_vectors=delete_vectors)
        print("The response of PointsApi->delete_vectors:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PointsApi->delete_vectors: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection_name** | **str**| Name of the collection to delete from | 
 **wait** | **bool**| If true, wait for changes to actually happen | [optional] 
 **ordering** | [**WriteOrdering**](.md)| define ordering guarantees for the operation | [optional] 
 **delete_vectors** | [**DeleteVectors**](DeleteVectors.md)| Delete named vectors from points | [optional] 

### Return type

[**CreateFieldIndex200Response**](CreateFieldIndex200Response.md)

### Authorization

[api-key](../README.md#api-key), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**4XX** | error |  -  |
**0** | error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **discover_batch_points**
> SearchBatchPoints200Response discover_batch_points(collection_name, consistency=consistency, timeout=timeout, discover_request_batch=discover_request_batch)

Discover batch points

Look for points based on target and/or positive and negative example pairs, in batch.

### Example

* Api Key Authentication (api-key):
* Bearer Authentication (bearerAuth):
```python
import time
import os
import qdrant_openapi
from qdrant_openapi.models.discover_request_batch import DiscoverRequestBatch
from qdrant_openapi.models.search_batch_points200_response import SearchBatchPoints200Response
from qdrant_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:6333
# See configuration.py for a list of all supported configuration parameters.
configuration = qdrant_openapi.Configuration(
    host = "http://localhost:6333"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api-key
configuration.api_key['api-key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'

# Configure Bearer authorization: bearerAuth
configuration = qdrant_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with qdrant_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = qdrant_openapi.PointsApi(api_client)
    collection_name = 'collection_name_example' # str | Name of the collection to search in
    consistency = qdrant_openapi.ReadConsistency() # ReadConsistency | Define read consistency guarantees for the operation (optional)
    timeout = 56 # int | If set, overrides global timeout for this request. Unit is seconds. (optional)
    discover_request_batch = qdrant_openapi.DiscoverRequestBatch() # DiscoverRequestBatch | Batch request points based on { positive, negative } pairs of examples, and/or a target. (optional)

    try:
        # Discover batch points
        api_response = api_instance.discover_batch_points(collection_name, consistency=consistency, timeout=timeout, discover_request_batch=discover_request_batch)
        print("The response of PointsApi->discover_batch_points:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PointsApi->discover_batch_points: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection_name** | **str**| Name of the collection to search in | 
 **consistency** | [**ReadConsistency**](.md)| Define read consistency guarantees for the operation | [optional] 
 **timeout** | **int**| If set, overrides global timeout for this request. Unit is seconds. | [optional] 
 **discover_request_batch** | [**DiscoverRequestBatch**](DiscoverRequestBatch.md)| Batch request points based on { positive, negative } pairs of examples, and/or a target. | [optional] 

### Return type

[**SearchBatchPoints200Response**](SearchBatchPoints200Response.md)

### Authorization

[api-key](../README.md#api-key), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**4XX** | error |  -  |
**0** | error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **discover_points**
> SearchPoints200Response discover_points(collection_name, consistency=consistency, timeout=timeout, discover_request=discover_request)

Discover points

Use context and a target to find the most similar points to the target, constrained by the context. When using only the context (without a target), a special search - called context search - is performed where pairs of points are used to generate a loss that guides the search towards the zone where most positive examples overlap. This means that the score minimizes the scenario of finding a point closer to a negative than to a positive part of a pair. Since the score of a context relates to loss, the maximum score a point can get is 0.0, and it becomes normal that many points can have a score of 0.0. When using target (with or without context), the score behaves a little different: The  integer part of the score represents the rank with respect to the context, while the decimal part of the score relates to the distance to the target. The context part of the score for  each pair is calculated +1 if the point is closer to a positive than to a negative part of a pair,  and -1 otherwise. 

### Example

* Api Key Authentication (api-key):
* Bearer Authentication (bearerAuth):
```python
import time
import os
import qdrant_openapi
from qdrant_openapi.models.discover_request import DiscoverRequest
from qdrant_openapi.models.search_points200_response import SearchPoints200Response
from qdrant_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:6333
# See configuration.py for a list of all supported configuration parameters.
configuration = qdrant_openapi.Configuration(
    host = "http://localhost:6333"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api-key
configuration.api_key['api-key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'

# Configure Bearer authorization: bearerAuth
configuration = qdrant_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with qdrant_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = qdrant_openapi.PointsApi(api_client)
    collection_name = 'collection_name_example' # str | Name of the collection to search in
    consistency = qdrant_openapi.ReadConsistency() # ReadConsistency | Define read consistency guarantees for the operation (optional)
    timeout = 56 # int | If set, overrides global timeout for this request. Unit is seconds. (optional)
    discover_request = qdrant_openapi.DiscoverRequest() # DiscoverRequest | Request points based on {positive, negative} pairs of examples, and/or a target (optional)

    try:
        # Discover points
        api_response = api_instance.discover_points(collection_name, consistency=consistency, timeout=timeout, discover_request=discover_request)
        print("The response of PointsApi->discover_points:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PointsApi->discover_points: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection_name** | **str**| Name of the collection to search in | 
 **consistency** | [**ReadConsistency**](.md)| Define read consistency guarantees for the operation | [optional] 
 **timeout** | **int**| If set, overrides global timeout for this request. Unit is seconds. | [optional] 
 **discover_request** | [**DiscoverRequest**](DiscoverRequest.md)| Request points based on {positive, negative} pairs of examples, and/or a target | [optional] 

### Return type

[**SearchPoints200Response**](SearchPoints200Response.md)

### Authorization

[api-key](../README.md#api-key), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**4XX** | error |  -  |
**0** | error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_point**
> GetPoint200Response get_point(collection_name, id, consistency=consistency)

Get point

Retrieve full information of single point by id

### Example

* Api Key Authentication (api-key):
* Bearer Authentication (bearerAuth):
```python
import time
import os
import qdrant_openapi
from qdrant_openapi.models.get_point200_response import GetPoint200Response
from qdrant_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:6333
# See configuration.py for a list of all supported configuration parameters.
configuration = qdrant_openapi.Configuration(
    host = "http://localhost:6333"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api-key
configuration.api_key['api-key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'

# Configure Bearer authorization: bearerAuth
configuration = qdrant_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with qdrant_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = qdrant_openapi.PointsApi(api_client)
    collection_name = 'collection_name_example' # str | Name of the collection to retrieve from
    id = qdrant_openapi.ExtendedPointId() # ExtendedPointId | Id of the point
    consistency = qdrant_openapi.ReadConsistency() # ReadConsistency | Define read consistency guarantees for the operation (optional)

    try:
        # Get point
        api_response = api_instance.get_point(collection_name, id, consistency=consistency)
        print("The response of PointsApi->get_point:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PointsApi->get_point: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection_name** | **str**| Name of the collection to retrieve from | 
 **id** | [**ExtendedPointId**](.md)| Id of the point | 
 **consistency** | [**ReadConsistency**](.md)| Define read consistency guarantees for the operation | [optional] 

### Return type

[**GetPoint200Response**](GetPoint200Response.md)

### Authorization

[api-key](../README.md#api-key), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**4XX** | error |  -  |
**0** | error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_points**
> GetPoints200Response get_points(collection_name, consistency=consistency, point_request=point_request)

Get points

Retrieve multiple points by specified IDs

### Example

* Api Key Authentication (api-key):
* Bearer Authentication (bearerAuth):
```python
import time
import os
import qdrant_openapi
from qdrant_openapi.models.get_points200_response import GetPoints200Response
from qdrant_openapi.models.point_request import PointRequest
from qdrant_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:6333
# See configuration.py for a list of all supported configuration parameters.
configuration = qdrant_openapi.Configuration(
    host = "http://localhost:6333"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api-key
configuration.api_key['api-key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'

# Configure Bearer authorization: bearerAuth
configuration = qdrant_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with qdrant_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = qdrant_openapi.PointsApi(api_client)
    collection_name = 'collection_name_example' # str | Name of the collection to retrieve from
    consistency = qdrant_openapi.ReadConsistency() # ReadConsistency | Define read consistency guarantees for the operation (optional)
    point_request = qdrant_openapi.PointRequest() # PointRequest | List of points to retrieve (optional)

    try:
        # Get points
        api_response = api_instance.get_points(collection_name, consistency=consistency, point_request=point_request)
        print("The response of PointsApi->get_points:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PointsApi->get_points: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection_name** | **str**| Name of the collection to retrieve from | 
 **consistency** | [**ReadConsistency**](.md)| Define read consistency guarantees for the operation | [optional] 
 **point_request** | [**PointRequest**](PointRequest.md)| List of points to retrieve | [optional] 

### Return type

[**GetPoints200Response**](GetPoints200Response.md)

### Authorization

[api-key](../README.md#api-key), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**4XX** | error |  -  |
**0** | error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **overwrite_payload**
> CreateFieldIndex200Response overwrite_payload(collection_name, wait=wait, ordering=ordering, set_payload=set_payload)

Overwrite payload

Replace full payload of points with new one

### Example

* Api Key Authentication (api-key):
* Bearer Authentication (bearerAuth):
```python
import time
import os
import qdrant_openapi
from qdrant_openapi.models.create_field_index200_response import CreateFieldIndex200Response
from qdrant_openapi.models.set_payload import SetPayload
from qdrant_openapi.models.write_ordering import WriteOrdering
from qdrant_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:6333
# See configuration.py for a list of all supported configuration parameters.
configuration = qdrant_openapi.Configuration(
    host = "http://localhost:6333"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api-key
configuration.api_key['api-key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'

# Configure Bearer authorization: bearerAuth
configuration = qdrant_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with qdrant_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = qdrant_openapi.PointsApi(api_client)
    collection_name = 'collection_name_example' # str | Name of the collection to set from
    wait = True # bool | If true, wait for changes to actually happen (optional)
    ordering = qdrant_openapi.WriteOrdering() # WriteOrdering | define ordering guarantees for the operation (optional)
    set_payload = qdrant_openapi.SetPayload() # SetPayload | Payload and points selector (optional)

    try:
        # Overwrite payload
        api_response = api_instance.overwrite_payload(collection_name, wait=wait, ordering=ordering, set_payload=set_payload)
        print("The response of PointsApi->overwrite_payload:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PointsApi->overwrite_payload: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection_name** | **str**| Name of the collection to set from | 
 **wait** | **bool**| If true, wait for changes to actually happen | [optional] 
 **ordering** | [**WriteOrdering**](.md)| define ordering guarantees for the operation | [optional] 
 **set_payload** | [**SetPayload**](SetPayload.md)| Payload and points selector | [optional] 

### Return type

[**CreateFieldIndex200Response**](CreateFieldIndex200Response.md)

### Authorization

[api-key](../README.md#api-key), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**4XX** | error |  -  |
**0** | error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **recommend_batch_points**
> SearchBatchPoints200Response recommend_batch_points(collection_name, consistency=consistency, timeout=timeout, recommend_request_batch=recommend_request_batch)

Recommend batch points

Look for the points which are closer to stored positive examples and at the same time further to negative examples.

### Example

* Api Key Authentication (api-key):
* Bearer Authentication (bearerAuth):
```python
import time
import os
import qdrant_openapi
from qdrant_openapi.models.recommend_request_batch import RecommendRequestBatch
from qdrant_openapi.models.search_batch_points200_response import SearchBatchPoints200Response
from qdrant_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:6333
# See configuration.py for a list of all supported configuration parameters.
configuration = qdrant_openapi.Configuration(
    host = "http://localhost:6333"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api-key
configuration.api_key['api-key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'

# Configure Bearer authorization: bearerAuth
configuration = qdrant_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with qdrant_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = qdrant_openapi.PointsApi(api_client)
    collection_name = 'collection_name_example' # str | Name of the collection to search in
    consistency = qdrant_openapi.ReadConsistency() # ReadConsistency | Define read consistency guarantees for the operation (optional)
    timeout = 56 # int | If set, overrides global timeout for this request. Unit is seconds. (optional)
    recommend_request_batch = qdrant_openapi.RecommendRequestBatch() # RecommendRequestBatch | Request points based on positive and negative examples. (optional)

    try:
        # Recommend batch points
        api_response = api_instance.recommend_batch_points(collection_name, consistency=consistency, timeout=timeout, recommend_request_batch=recommend_request_batch)
        print("The response of PointsApi->recommend_batch_points:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PointsApi->recommend_batch_points: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection_name** | **str**| Name of the collection to search in | 
 **consistency** | [**ReadConsistency**](.md)| Define read consistency guarantees for the operation | [optional] 
 **timeout** | **int**| If set, overrides global timeout for this request. Unit is seconds. | [optional] 
 **recommend_request_batch** | [**RecommendRequestBatch**](RecommendRequestBatch.md)| Request points based on positive and negative examples. | [optional] 

### Return type

[**SearchBatchPoints200Response**](SearchBatchPoints200Response.md)

### Authorization

[api-key](../README.md#api-key), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**4XX** | error |  -  |
**0** | error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **recommend_point_groups**
> SearchPointGroups200Response recommend_point_groups(collection_name, consistency=consistency, timeout=timeout, recommend_groups_request=recommend_groups_request)

Recommend point groups

Look for the points which are closer to stored positive examples and at the same time further to negative examples, grouped by a given payload field.

### Example

* Api Key Authentication (api-key):
* Bearer Authentication (bearerAuth):
```python
import time
import os
import qdrant_openapi
from qdrant_openapi.models.recommend_groups_request import RecommendGroupsRequest
from qdrant_openapi.models.search_point_groups200_response import SearchPointGroups200Response
from qdrant_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:6333
# See configuration.py for a list of all supported configuration parameters.
configuration = qdrant_openapi.Configuration(
    host = "http://localhost:6333"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api-key
configuration.api_key['api-key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'

# Configure Bearer authorization: bearerAuth
configuration = qdrant_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with qdrant_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = qdrant_openapi.PointsApi(api_client)
    collection_name = 'collection_name_example' # str | Name of the collection to search in
    consistency = qdrant_openapi.ReadConsistency() # ReadConsistency | Define read consistency guarantees for the operation (optional)
    timeout = 56 # int | If set, overrides global timeout for this request. Unit is seconds. (optional)
    recommend_groups_request = qdrant_openapi.RecommendGroupsRequest() # RecommendGroupsRequest | Request points based on positive and negative examples, grouped by a payload field. (optional)

    try:
        # Recommend point groups
        api_response = api_instance.recommend_point_groups(collection_name, consistency=consistency, timeout=timeout, recommend_groups_request=recommend_groups_request)
        print("The response of PointsApi->recommend_point_groups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PointsApi->recommend_point_groups: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection_name** | **str**| Name of the collection to search in | 
 **consistency** | [**ReadConsistency**](.md)| Define read consistency guarantees for the operation | [optional] 
 **timeout** | **int**| If set, overrides global timeout for this request. Unit is seconds. | [optional] 
 **recommend_groups_request** | [**RecommendGroupsRequest**](RecommendGroupsRequest.md)| Request points based on positive and negative examples, grouped by a payload field. | [optional] 

### Return type

[**SearchPointGroups200Response**](SearchPointGroups200Response.md)

### Authorization

[api-key](../README.md#api-key), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**4XX** | error |  -  |
**0** | error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **recommend_points**
> SearchPoints200Response recommend_points(collection_name, consistency=consistency, timeout=timeout, recommend_request=recommend_request)

Recommend points

Look for the points which are closer to stored positive examples and at the same time further to negative examples.

### Example

* Api Key Authentication (api-key):
* Bearer Authentication (bearerAuth):
```python
import time
import os
import qdrant_openapi
from qdrant_openapi.models.recommend_request import RecommendRequest
from qdrant_openapi.models.search_points200_response import SearchPoints200Response
from qdrant_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:6333
# See configuration.py for a list of all supported configuration parameters.
configuration = qdrant_openapi.Configuration(
    host = "http://localhost:6333"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api-key
configuration.api_key['api-key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'

# Configure Bearer authorization: bearerAuth
configuration = qdrant_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with qdrant_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = qdrant_openapi.PointsApi(api_client)
    collection_name = 'collection_name_example' # str | Name of the collection to search in
    consistency = qdrant_openapi.ReadConsistency() # ReadConsistency | Define read consistency guarantees for the operation (optional)
    timeout = 56 # int | If set, overrides global timeout for this request. Unit is seconds. (optional)
    recommend_request = qdrant_openapi.RecommendRequest() # RecommendRequest | Request points based on positive and negative examples. (optional)

    try:
        # Recommend points
        api_response = api_instance.recommend_points(collection_name, consistency=consistency, timeout=timeout, recommend_request=recommend_request)
        print("The response of PointsApi->recommend_points:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PointsApi->recommend_points: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection_name** | **str**| Name of the collection to search in | 
 **consistency** | [**ReadConsistency**](.md)| Define read consistency guarantees for the operation | [optional] 
 **timeout** | **int**| If set, overrides global timeout for this request. Unit is seconds. | [optional] 
 **recommend_request** | [**RecommendRequest**](RecommendRequest.md)| Request points based on positive and negative examples. | [optional] 

### Return type

[**SearchPoints200Response**](SearchPoints200Response.md)

### Authorization

[api-key](../README.md#api-key), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**4XX** | error |  -  |
**0** | error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **scroll_points**
> ScrollPoints200Response scroll_points(collection_name, consistency=consistency, scroll_request=scroll_request)

Scroll points

Scroll request - paginate over all points which matches given filtering condition

### Example

* Api Key Authentication (api-key):
* Bearer Authentication (bearerAuth):
```python
import time
import os
import qdrant_openapi
from qdrant_openapi.models.scroll_points200_response import ScrollPoints200Response
from qdrant_openapi.models.scroll_request import ScrollRequest
from qdrant_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:6333
# See configuration.py for a list of all supported configuration parameters.
configuration = qdrant_openapi.Configuration(
    host = "http://localhost:6333"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api-key
configuration.api_key['api-key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'

# Configure Bearer authorization: bearerAuth
configuration = qdrant_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with qdrant_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = qdrant_openapi.PointsApi(api_client)
    collection_name = 'collection_name_example' # str | Name of the collection to retrieve from
    consistency = qdrant_openapi.ReadConsistency() # ReadConsistency | Define read consistency guarantees for the operation (optional)
    scroll_request = qdrant_openapi.ScrollRequest() # ScrollRequest | Pagination and filter parameters (optional)

    try:
        # Scroll points
        api_response = api_instance.scroll_points(collection_name, consistency=consistency, scroll_request=scroll_request)
        print("The response of PointsApi->scroll_points:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PointsApi->scroll_points: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection_name** | **str**| Name of the collection to retrieve from | 
 **consistency** | [**ReadConsistency**](.md)| Define read consistency guarantees for the operation | [optional] 
 **scroll_request** | [**ScrollRequest**](ScrollRequest.md)| Pagination and filter parameters | [optional] 

### Return type

[**ScrollPoints200Response**](ScrollPoints200Response.md)

### Authorization

[api-key](../README.md#api-key), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**4XX** | error |  -  |
**0** | error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_batch_points**
> SearchBatchPoints200Response search_batch_points(collection_name, consistency=consistency, timeout=timeout, search_request_batch=search_request_batch)

Search batch points

Retrieve by batch the closest points based on vector similarity and given filtering conditions

### Example

* Api Key Authentication (api-key):
* Bearer Authentication (bearerAuth):
```python
import time
import os
import qdrant_openapi
from qdrant_openapi.models.search_batch_points200_response import SearchBatchPoints200Response
from qdrant_openapi.models.search_request_batch import SearchRequestBatch
from qdrant_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:6333
# See configuration.py for a list of all supported configuration parameters.
configuration = qdrant_openapi.Configuration(
    host = "http://localhost:6333"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api-key
configuration.api_key['api-key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'

# Configure Bearer authorization: bearerAuth
configuration = qdrant_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with qdrant_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = qdrant_openapi.PointsApi(api_client)
    collection_name = 'collection_name_example' # str | Name of the collection to search in
    consistency = qdrant_openapi.ReadConsistency() # ReadConsistency | Define read consistency guarantees for the operation (optional)
    timeout = 56 # int | If set, overrides global timeout for this request. Unit is seconds. (optional)
    search_request_batch = qdrant_openapi.SearchRequestBatch() # SearchRequestBatch | Search batch request (optional)

    try:
        # Search batch points
        api_response = api_instance.search_batch_points(collection_name, consistency=consistency, timeout=timeout, search_request_batch=search_request_batch)
        print("The response of PointsApi->search_batch_points:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PointsApi->search_batch_points: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection_name** | **str**| Name of the collection to search in | 
 **consistency** | [**ReadConsistency**](.md)| Define read consistency guarantees for the operation | [optional] 
 **timeout** | **int**| If set, overrides global timeout for this request. Unit is seconds. | [optional] 
 **search_request_batch** | [**SearchRequestBatch**](SearchRequestBatch.md)| Search batch request | [optional] 

### Return type

[**SearchBatchPoints200Response**](SearchBatchPoints200Response.md)

### Authorization

[api-key](../README.md#api-key), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**4XX** | error |  -  |
**0** | error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_point_groups**
> SearchPointGroups200Response search_point_groups(collection_name, consistency=consistency, timeout=timeout, search_groups_request=search_groups_request)

Search point groups

Retrieve closest points based on vector similarity and given filtering conditions, grouped by a given payload field

### Example

* Api Key Authentication (api-key):
* Bearer Authentication (bearerAuth):
```python
import time
import os
import qdrant_openapi
from qdrant_openapi.models.search_groups_request import SearchGroupsRequest
from qdrant_openapi.models.search_point_groups200_response import SearchPointGroups200Response
from qdrant_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:6333
# See configuration.py for a list of all supported configuration parameters.
configuration = qdrant_openapi.Configuration(
    host = "http://localhost:6333"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api-key
configuration.api_key['api-key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'

# Configure Bearer authorization: bearerAuth
configuration = qdrant_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with qdrant_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = qdrant_openapi.PointsApi(api_client)
    collection_name = 'collection_name_example' # str | Name of the collection to search in
    consistency = qdrant_openapi.ReadConsistency() # ReadConsistency | Define read consistency guarantees for the operation (optional)
    timeout = 56 # int | If set, overrides global timeout for this request. Unit is seconds. (optional)
    search_groups_request = qdrant_openapi.SearchGroupsRequest() # SearchGroupsRequest | Search request with optional filtering, grouped by a given payload field (optional)

    try:
        # Search point groups
        api_response = api_instance.search_point_groups(collection_name, consistency=consistency, timeout=timeout, search_groups_request=search_groups_request)
        print("The response of PointsApi->search_point_groups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PointsApi->search_point_groups: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection_name** | **str**| Name of the collection to search in | 
 **consistency** | [**ReadConsistency**](.md)| Define read consistency guarantees for the operation | [optional] 
 **timeout** | **int**| If set, overrides global timeout for this request. Unit is seconds. | [optional] 
 **search_groups_request** | [**SearchGroupsRequest**](SearchGroupsRequest.md)| Search request with optional filtering, grouped by a given payload field | [optional] 

### Return type

[**SearchPointGroups200Response**](SearchPointGroups200Response.md)

### Authorization

[api-key](../README.md#api-key), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**4XX** | error |  -  |
**0** | error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_points**
> SearchPoints200Response search_points(collection_name, consistency=consistency, timeout=timeout, search_request=search_request)

Search points

Retrieve closest points based on vector similarity and given filtering conditions

### Example

* Api Key Authentication (api-key):
* Bearer Authentication (bearerAuth):
```python
import time
import os
import qdrant_openapi
from qdrant_openapi.models.search_points200_response import SearchPoints200Response
from qdrant_openapi.models.search_request import SearchRequest
from qdrant_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:6333
# See configuration.py for a list of all supported configuration parameters.
configuration = qdrant_openapi.Configuration(
    host = "http://localhost:6333"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api-key
configuration.api_key['api-key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'

# Configure Bearer authorization: bearerAuth
configuration = qdrant_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with qdrant_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = qdrant_openapi.PointsApi(api_client)
    collection_name = 'collection_name_example' # str | Name of the collection to search in
    consistency = qdrant_openapi.ReadConsistency() # ReadConsistency | Define read consistency guarantees for the operation (optional)
    timeout = 56 # int | If set, overrides global timeout for this request. Unit is seconds. (optional)
    search_request = qdrant_openapi.SearchRequest() # SearchRequest | Search request with optional filtering (optional)

    try:
        # Search points
        api_response = api_instance.search_points(collection_name, consistency=consistency, timeout=timeout, search_request=search_request)
        print("The response of PointsApi->search_points:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PointsApi->search_points: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection_name** | **str**| Name of the collection to search in | 
 **consistency** | [**ReadConsistency**](.md)| Define read consistency guarantees for the operation | [optional] 
 **timeout** | **int**| If set, overrides global timeout for this request. Unit is seconds. | [optional] 
 **search_request** | [**SearchRequest**](SearchRequest.md)| Search request with optional filtering | [optional] 

### Return type

[**SearchPoints200Response**](SearchPoints200Response.md)

### Authorization

[api-key](../README.md#api-key), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**4XX** | error |  -  |
**0** | error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_payload**
> CreateFieldIndex200Response set_payload(collection_name, wait=wait, ordering=ordering, set_payload=set_payload)

Set payload

Set payload values for points

### Example

* Api Key Authentication (api-key):
* Bearer Authentication (bearerAuth):
```python
import time
import os
import qdrant_openapi
from qdrant_openapi.models.create_field_index200_response import CreateFieldIndex200Response
from qdrant_openapi.models.set_payload import SetPayload
from qdrant_openapi.models.write_ordering import WriteOrdering
from qdrant_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:6333
# See configuration.py for a list of all supported configuration parameters.
configuration = qdrant_openapi.Configuration(
    host = "http://localhost:6333"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api-key
configuration.api_key['api-key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'

# Configure Bearer authorization: bearerAuth
configuration = qdrant_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with qdrant_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = qdrant_openapi.PointsApi(api_client)
    collection_name = 'collection_name_example' # str | Name of the collection to set from
    wait = True # bool | If true, wait for changes to actually happen (optional)
    ordering = qdrant_openapi.WriteOrdering() # WriteOrdering | define ordering guarantees for the operation (optional)
    set_payload = qdrant_openapi.SetPayload() # SetPayload | Set payload on points (optional)

    try:
        # Set payload
        api_response = api_instance.set_payload(collection_name, wait=wait, ordering=ordering, set_payload=set_payload)
        print("The response of PointsApi->set_payload:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PointsApi->set_payload: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection_name** | **str**| Name of the collection to set from | 
 **wait** | **bool**| If true, wait for changes to actually happen | [optional] 
 **ordering** | [**WriteOrdering**](.md)| define ordering guarantees for the operation | [optional] 
 **set_payload** | [**SetPayload**](SetPayload.md)| Set payload on points | [optional] 

### Return type

[**CreateFieldIndex200Response**](CreateFieldIndex200Response.md)

### Authorization

[api-key](../README.md#api-key), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**4XX** | error |  -  |
**0** | error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_vectors**
> CreateFieldIndex200Response update_vectors(collection_name, wait=wait, ordering=ordering, update_vectors=update_vectors)

Update vectors

Update specified named vectors on points, keep unspecified vectors intact.

### Example

* Api Key Authentication (api-key):
* Bearer Authentication (bearerAuth):
```python
import time
import os
import qdrant_openapi
from qdrant_openapi.models.create_field_index200_response import CreateFieldIndex200Response
from qdrant_openapi.models.update_vectors import UpdateVectors
from qdrant_openapi.models.write_ordering import WriteOrdering
from qdrant_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:6333
# See configuration.py for a list of all supported configuration parameters.
configuration = qdrant_openapi.Configuration(
    host = "http://localhost:6333"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api-key
configuration.api_key['api-key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'

# Configure Bearer authorization: bearerAuth
configuration = qdrant_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with qdrant_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = qdrant_openapi.PointsApi(api_client)
    collection_name = 'collection_name_example' # str | Name of the collection to update from
    wait = True # bool | If true, wait for changes to actually happen (optional)
    ordering = qdrant_openapi.WriteOrdering() # WriteOrdering | define ordering guarantees for the operation (optional)
    update_vectors = qdrant_openapi.UpdateVectors() # UpdateVectors | Update named vectors on points (optional)

    try:
        # Update vectors
        api_response = api_instance.update_vectors(collection_name, wait=wait, ordering=ordering, update_vectors=update_vectors)
        print("The response of PointsApi->update_vectors:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PointsApi->update_vectors: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection_name** | **str**| Name of the collection to update from | 
 **wait** | **bool**| If true, wait for changes to actually happen | [optional] 
 **ordering** | [**WriteOrdering**](.md)| define ordering guarantees for the operation | [optional] 
 **update_vectors** | [**UpdateVectors**](UpdateVectors.md)| Update named vectors on points | [optional] 

### Return type

[**CreateFieldIndex200Response**](CreateFieldIndex200Response.md)

### Authorization

[api-key](../README.md#api-key), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**4XX** | error |  -  |
**0** | error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upsert_points**
> CreateFieldIndex200Response upsert_points(collection_name, wait=wait, ordering=ordering, point_insert_operations=point_insert_operations)

Upsert points

Perform insert + updates on points. If point with given ID already exists - it will be overwritten.

### Example

* Api Key Authentication (api-key):
* Bearer Authentication (bearerAuth):
```python
import time
import os
import qdrant_openapi
from qdrant_openapi.models.create_field_index200_response import CreateFieldIndex200Response
from qdrant_openapi.models.point_insert_operations import PointInsertOperations
from qdrant_openapi.models.write_ordering import WriteOrdering
from qdrant_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:6333
# See configuration.py for a list of all supported configuration parameters.
configuration = qdrant_openapi.Configuration(
    host = "http://localhost:6333"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api-key
configuration.api_key['api-key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'

# Configure Bearer authorization: bearerAuth
configuration = qdrant_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with qdrant_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = qdrant_openapi.PointsApi(api_client)
    collection_name = 'collection_name_example' # str | Name of the collection to update from
    wait = True # bool | If true, wait for changes to actually happen (optional)
    ordering = qdrant_openapi.WriteOrdering() # WriteOrdering | define ordering guarantees for the operation (optional)
    point_insert_operations = qdrant_openapi.PointInsertOperations() # PointInsertOperations | Operation to perform on points (optional)

    try:
        # Upsert points
        api_response = api_instance.upsert_points(collection_name, wait=wait, ordering=ordering, point_insert_operations=point_insert_operations)
        print("The response of PointsApi->upsert_points:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PointsApi->upsert_points: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection_name** | **str**| Name of the collection to update from | 
 **wait** | **bool**| If true, wait for changes to actually happen | [optional] 
 **ordering** | [**WriteOrdering**](.md)| define ordering guarantees for the operation | [optional] 
 **point_insert_operations** | [**PointInsertOperations**](PointInsertOperations.md)| Operation to perform on points | [optional] 

### Return type

[**CreateFieldIndex200Response**](CreateFieldIndex200Response.md)

### Authorization

[api-key](../README.md#api-key), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**4XX** | error |  -  |
**0** | error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

