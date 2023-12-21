# openapi_client.ServiceApi

All URIs are relative to *http://localhost:6333*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_locks**](ServiceApi.md#get_locks) | **GET** /locks | Get lock options
[**healthz**](ServiceApi.md#healthz) | **GET** /healthz | Kubernetes healthz endpoint
[**livez**](ServiceApi.md#livez) | **GET** /livez | Kubernetes livez endpoint
[**metrics**](ServiceApi.md#metrics) | **GET** /metrics | Collect Prometheus metrics data
[**post_locks**](ServiceApi.md#post_locks) | **POST** /locks | Set lock options
[**readyz**](ServiceApi.md#readyz) | **GET** /readyz | Kubernetes readyz endpoint
[**telemetry**](ServiceApi.md#telemetry) | **GET** /telemetry | Collect telemetry data


# **get_locks**
> GetLocks200Response get_locks()

Get lock options

Get lock options. If write is locked, all write operations and collection creation are forbidden

### Example

* Api Key Authentication (api-key):
* Bearer Authentication (bearerAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.get_locks200_response import GetLocks200Response
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:6333
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
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
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.ServiceApi(api_client)

    try:
        # Get lock options
        api_response = api_instance.get_locks()
        print("The response of ServiceApi->get_locks:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceApi->get_locks: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**GetLocks200Response**](GetLocks200Response.md)

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

# **healthz**
> str healthz()

Kubernetes healthz endpoint

An endpoint for health checking used in Kubernetes.

### Example

* Api Key Authentication (api-key):
* Bearer Authentication (bearerAuth):
```python
import time
import os
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:6333
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
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
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.ServiceApi(api_client)

    try:
        # Kubernetes healthz endpoint
        api_response = api_instance.healthz()
        print("The response of ServiceApi->healthz:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceApi->healthz: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

**str**

### Authorization

[api-key](../README.md#api-key), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Healthz response |  -  |
**4XX** | error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **livez**
> str livez()

Kubernetes livez endpoint

An endpoint for health checking used in Kubernetes.

### Example

* Api Key Authentication (api-key):
* Bearer Authentication (bearerAuth):
```python
import time
import os
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:6333
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
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
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.ServiceApi(api_client)

    try:
        # Kubernetes livez endpoint
        api_response = api_instance.livez()
        print("The response of ServiceApi->livez:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceApi->livez: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

**str**

### Authorization

[api-key](../README.md#api-key), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Healthz response |  -  |
**4XX** | error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **metrics**
> str metrics(anonymize=anonymize)

Collect Prometheus metrics data

Collect metrics data including app info, collections info, cluster info and statistics

### Example

* Api Key Authentication (api-key):
* Bearer Authentication (bearerAuth):
```python
import time
import os
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:6333
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
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
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.ServiceApi(api_client)
    anonymize = True # bool | If true, anonymize result (optional)

    try:
        # Collect Prometheus metrics data
        api_response = api_instance.metrics(anonymize=anonymize)
        print("The response of ServiceApi->metrics:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceApi->metrics: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **anonymize** | **bool**| If true, anonymize result | [optional] 

### Return type

**str**

### Authorization

[api-key](../README.md#api-key), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Metrics data in Prometheus format |  -  |
**4XX** | error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_locks**
> GetLocks200Response post_locks(locks_option=locks_option)

Set lock options

Set lock options. If write is locked, all write operations and collection creation are forbidden. Returns previous lock options

### Example

* Api Key Authentication (api-key):
* Bearer Authentication (bearerAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.get_locks200_response import GetLocks200Response
from openapi_client.models.locks_option import LocksOption
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:6333
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
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
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.ServiceApi(api_client)
    locks_option = openapi_client.LocksOption() # LocksOption | Lock options and optional error message (optional)

    try:
        # Set lock options
        api_response = api_instance.post_locks(locks_option=locks_option)
        print("The response of ServiceApi->post_locks:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceApi->post_locks: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **locks_option** | [**LocksOption**](LocksOption.md)| Lock options and optional error message | [optional] 

### Return type

[**GetLocks200Response**](GetLocks200Response.md)

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

# **readyz**
> str readyz()

Kubernetes readyz endpoint

An endpoint for health checking used in Kubernetes.

### Example

* Api Key Authentication (api-key):
* Bearer Authentication (bearerAuth):
```python
import time
import os
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:6333
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
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
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.ServiceApi(api_client)

    try:
        # Kubernetes readyz endpoint
        api_response = api_instance.readyz()
        print("The response of ServiceApi->readyz:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceApi->readyz: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

**str**

### Authorization

[api-key](../README.md#api-key), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Healthz response |  -  |
**4XX** | error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **telemetry**
> Telemetry200Response telemetry(anonymize=anonymize)

Collect telemetry data

Collect telemetry data including app info, system info, collections info, cluster info, configs and statistics

### Example

* Api Key Authentication (api-key):
* Bearer Authentication (bearerAuth):
```python
import time
import os
import openapi_client
from openapi_client.models.telemetry200_response import Telemetry200Response
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:6333
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
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
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.ServiceApi(api_client)
    anonymize = True # bool | If true, anonymize result (optional)

    try:
        # Collect telemetry data
        api_response = api_instance.telemetry(anonymize=anonymize)
        print("The response of ServiceApi->telemetry:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceApi->telemetry: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **anonymize** | **bool**| If true, anonymize result | [optional] 

### Return type

[**Telemetry200Response**](Telemetry200Response.md)

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

