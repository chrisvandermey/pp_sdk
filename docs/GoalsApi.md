# pp_sdk.GoalsApi

All URIs are relative to *http://0.0.0.0:8000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**goals_list_list**](GoalsApi.md#goals_list_list) | **GET** /goals/list/ | 


# **goals_list_list**
> List[Goal] goals_list_list(search=search, stakeholders_users=stakeholders_users, status=status, sort=sort, limit=limit, x_user_id=x_user_id)



Search for PRDs

### Example

```python
import time
import os
import pp_sdk
from pp_sdk.models.goal import Goal
from pp_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://0.0.0.0:8000
# See configuration.py for a list of all supported configuration parameters.
configuration = pp_sdk.Configuration(
    host = "http://0.0.0.0:8000"
)


# Enter a context with an instance of the API client
with pp_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pp_sdk.GoalsApi(api_client)
    search = 'search_example' # str | Search term for goal name, language, or description (optional)
    stakeholders_users = 'stakeholders_users_example' # str | Comma-separated list of stakeholder IDs (optional)
    status = 'status_example' # str | Filter by status (optional)
    sort = 'sort_example' # str | Sort field (prefix with '-' for descending order) (optional)
    limit = 56 # int | Limit the number of results (optional)
    x_user_id = 'x_user_id_example' # str | User ID (required when using API key) (optional)

    try:
        api_response = api_instance.goals_list_list(search=search, stakeholders_users=stakeholders_users, status=status, sort=sort, limit=limit, x_user_id=x_user_id)
        print("The response of GoalsApi->goals_list_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GoalsApi->goals_list_list: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search** | **str**| Search term for goal name, language, or description | [optional] 
 **stakeholders_users** | **str**| Comma-separated list of stakeholder IDs | [optional] 
 **status** | **str**| Filter by status | [optional] 
 **sort** | **str**| Sort field (prefix with &#39;-&#39; for descending order) | [optional] 
 **limit** | **int**| Limit the number of results | [optional] 
 **x_user_id** | **str**| User ID (required when using API key) | [optional] 

### Return type

[**List[Goal]**](Goal.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

