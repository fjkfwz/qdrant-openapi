# qdrant_openapi.ClusterApi

All URIs are relative to *http://localhost:6333*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cluster_status**](ClusterApi.md#cluster_status) | **GET** /cluster | Get cluster status info
[**collection_cluster_info**](ClusterApi.md#collection_cluster_info) | **GET** /collections/{collection_name}/cluster | Collection cluster info
[**create_shard_key**](ClusterApi.md#create_shard_key) | **PUT** /collections/{collection_name}/shards | Create shard key
[**delete_shard_key**](ClusterApi.md#delete_shard_key) | **POST** /collections/{collection_name}/shards/delete | Delete shard key
[**recover_current_peer**](ClusterApi.md#recover_current_peer) | **POST** /cluster/recover | Tries to recover current peer Raft state.
[**remove_peer**](ClusterApi.md#remove_peer) | **DELETE** /cluster/peer/{peer_id} | Remove peer from the cluster
[**update_collection_cluster**](ClusterApi.md#update_collection_cluster) | **POST** /collections/{collection_name}/cluster | Update collection cluster setup


# **cluster_status**
> ClusterStatus200Response cluster_status()

Get cluster status info

Get information about the current state and composition of the cluster

### Example

* Api Key Authentication (api-key):
* Bearer Authentication (bearerAuth):
```python
import time
import os
import qdrant_openapi
from qdrant_openapi.models.cluster_status200_response import ClusterStatus200Response
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
    api_instance = qdrant_openapi.ClusterApi(api_client)

    try:
        # Get cluster status info
        api_response = api_instance.cluster_status()
        print("The response of ClusterApi->cluster_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClusterApi->cluster_status: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**ClusterStatus200Response**](ClusterStatus200Response.md)

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

# **collection_cluster_info**
> CollectionClusterInfo200Response collection_cluster_info(collection_name)

Collection cluster info

Get cluster information for a collection

### Example

* Api Key Authentication (api-key):
* Bearer Authentication (bearerAuth):
```python
import time
import os
import qdrant_openapi
from qdrant_openapi.models.collection_cluster_info200_response import CollectionClusterInfo200Response
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
    api_instance = qdrant_openapi.ClusterApi(api_client)
    collection_name = 'collection_name_example' # str | Name of the collection to retrieve the cluster info for

    try:
        # Collection cluster info
        api_response = api_instance.collection_cluster_info(collection_name)
        print("The response of ClusterApi->collection_cluster_info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClusterApi->collection_cluster_info: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection_name** | **str**| Name of the collection to retrieve the cluster info for | 

### Return type

[**CollectionClusterInfo200Response**](CollectionClusterInfo200Response.md)

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

# **create_shard_key**
> CreateShardKey200Response create_shard_key(collection_name, timeout=timeout, create_sharding_key=create_sharding_key)

Create shard key

### Example

* Api Key Authentication (api-key):
* Bearer Authentication (bearerAuth):
```python
import time
import os
import qdrant_openapi
from qdrant_openapi.models.create_shard_key200_response import CreateShardKey200Response
from qdrant_openapi.models.create_sharding_key import CreateShardingKey
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
    api_instance = qdrant_openapi.ClusterApi(api_client)
    collection_name = 'collection_name_example' # str | Name of the collection to create shards for
    timeout = 56 # int | Wait for operation commit timeout in seconds.  If timeout is reached - request will return with service error.  (optional)
    create_sharding_key = qdrant_openapi.CreateShardingKey() # CreateShardingKey | Shard key configuration (optional)

    try:
        # Create shard key
        api_response = api_instance.create_shard_key(collection_name, timeout=timeout, create_sharding_key=create_sharding_key)
        print("The response of ClusterApi->create_shard_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClusterApi->create_shard_key: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection_name** | **str**| Name of the collection to create shards for | 
 **timeout** | **int**| Wait for operation commit timeout in seconds.  If timeout is reached - request will return with service error.  | [optional] 
 **create_sharding_key** | [**CreateShardingKey**](CreateShardingKey.md)| Shard key configuration | [optional] 

### Return type

[**CreateShardKey200Response**](CreateShardKey200Response.md)

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

# **delete_shard_key**
> CreateShardKey200Response delete_shard_key(collection_name, timeout=timeout, drop_sharding_key=drop_sharding_key)

Delete shard key

### Example

* Api Key Authentication (api-key):
* Bearer Authentication (bearerAuth):
```python
import time
import os
import qdrant_openapi
from qdrant_openapi.models.create_shard_key200_response import CreateShardKey200Response
from qdrant_openapi.models.drop_sharding_key import DropShardingKey
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
    api_instance = qdrant_openapi.ClusterApi(api_client)
    collection_name = 'collection_name_example' # str | Name of the collection to create shards for
    timeout = 56 # int | Wait for operation commit timeout in seconds.  If timeout is reached - request will return with service error.  (optional)
    drop_sharding_key = qdrant_openapi.DropShardingKey() # DropShardingKey | Select shard key to delete (optional)

    try:
        # Delete shard key
        api_response = api_instance.delete_shard_key(collection_name, timeout=timeout, drop_sharding_key=drop_sharding_key)
        print("The response of ClusterApi->delete_shard_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClusterApi->delete_shard_key: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection_name** | **str**| Name of the collection to create shards for | 
 **timeout** | **int**| Wait for operation commit timeout in seconds.  If timeout is reached - request will return with service error.  | [optional] 
 **drop_sharding_key** | [**DropShardingKey**](DropShardingKey.md)| Select shard key to delete | [optional] 

### Return type

[**CreateShardKey200Response**](CreateShardKey200Response.md)

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

# **recover_current_peer**
> CreateShardKey200Response recover_current_peer()

Tries to recover current peer Raft state.

### Example

* Api Key Authentication (api-key):
* Bearer Authentication (bearerAuth):
```python
import time
import os
import qdrant_openapi
from qdrant_openapi.models.create_shard_key200_response import CreateShardKey200Response
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
    api_instance = qdrant_openapi.ClusterApi(api_client)

    try:
        # Tries to recover current peer Raft state.
        api_response = api_instance.recover_current_peer()
        print("The response of ClusterApi->recover_current_peer:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClusterApi->recover_current_peer: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**CreateShardKey200Response**](CreateShardKey200Response.md)

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

# **remove_peer**
> CreateShardKey200Response remove_peer(peer_id, force=force)

Remove peer from the cluster

Tries to remove peer from the cluster. Will return an error if peer has shards on it.

### Example

* Api Key Authentication (api-key):
* Bearer Authentication (bearerAuth):
```python
import time
import os
import qdrant_openapi
from qdrant_openapi.models.create_shard_key200_response import CreateShardKey200Response
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
    api_instance = qdrant_openapi.ClusterApi(api_client)
    peer_id = 56 # int | Id of the peer
    force = False # bool | If true - removes peer even if it has shards/replicas on it. (optional) (default to False)

    try:
        # Remove peer from the cluster
        api_response = api_instance.remove_peer(peer_id, force=force)
        print("The response of ClusterApi->remove_peer:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClusterApi->remove_peer: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **peer_id** | **int**| Id of the peer | 
 **force** | **bool**| If true - removes peer even if it has shards/replicas on it. | [optional] [default to False]

### Return type

[**CreateShardKey200Response**](CreateShardKey200Response.md)

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

# **update_collection_cluster**
> CreateShardKey200Response update_collection_cluster(collection_name, timeout=timeout, cluster_operations=cluster_operations)

Update collection cluster setup

### Example

* Api Key Authentication (api-key):
* Bearer Authentication (bearerAuth):
```python
import time
import os
import qdrant_openapi
from qdrant_openapi.models.cluster_operations import ClusterOperations
from qdrant_openapi.models.create_shard_key200_response import CreateShardKey200Response
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
    api_instance = qdrant_openapi.ClusterApi(api_client)
    collection_name = 'collection_name_example' # str | Name of the collection on which to to apply the cluster update operation
    timeout = 56 # int | Wait for operation commit timeout in seconds.  If timeout is reached - request will return with service error.  (optional)
    cluster_operations = qdrant_openapi.ClusterOperations() # ClusterOperations | Collection cluster update operations (optional)

    try:
        # Update collection cluster setup
        api_response = api_instance.update_collection_cluster(collection_name, timeout=timeout, cluster_operations=cluster_operations)
        print("The response of ClusterApi->update_collection_cluster:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClusterApi->update_collection_cluster: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection_name** | **str**| Name of the collection on which to to apply the cluster update operation | 
 **timeout** | **int**| Wait for operation commit timeout in seconds.  If timeout is reached - request will return with service error.  | [optional] 
 **cluster_operations** | [**ClusterOperations**](ClusterOperations.md)| Collection cluster update operations | [optional] 

### Return type

[**CreateShardKey200Response**](CreateShardKey200Response.md)

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

