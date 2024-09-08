# pp_sdk
Product Partner APIs can create, list, and modify goals, prds, status updates, and other product management artifacts.

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: v1
- Package version: 0.1
- Generator version: 7.7.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

## Requirements.

Python 3.7+

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import pp_sdk
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import pp_sdk
```

### Tests

Execute `pytest` to run the tests.

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import pp_sdk
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
    api_instance = pp_sdk.ApiApi(api_client)
    data = pp_sdk.Goal() # Goal | 

    try:
        api_response = api_instance.api_goals_create(data)
        print("The response of ApiApi->api_goals_create:\n")
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ApiApi->api_goals_create: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *http://0.0.0.0:8000*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*ApiApi* | [**api_goals_create**](docs/ApiApi.md#api_goals_create) | **POST** /api/goals/ | 
*ApiApi* | [**api_goals_delete**](docs/ApiApi.md#api_goals_delete) | **DELETE** /api/goals/{goal_id}/ | 
*ApiApi* | [**api_goals_list**](docs/ApiApi.md#api_goals_list) | **GET** /api/goals/ | 
*ApiApi* | [**api_goals_partial_update**](docs/ApiApi.md#api_goals_partial_update) | **PATCH** /api/goals/{goal_id}/ | 
*ApiApi* | [**api_goals_read**](docs/ApiApi.md#api_goals_read) | **GET** /api/goals/{goal_id}/ | 
*ApiApi* | [**api_goals_search_list**](docs/ApiApi.md#api_goals_search_list) | **GET** /api/goals/search/ | 
*ApiApi* | [**api_goals_update**](docs/ApiApi.md#api_goals_update) | **PUT** /api/goals/{goal_id}/ | 
*ApiApi* | [**api_prd_search_list**](docs/ApiApi.md#api_prd_search_list) | **GET** /api/prd/search/ | 
*ApiApi* | [**api_prds_create**](docs/ApiApi.md#api_prds_create) | **POST** /api/prds/ | 
*ApiApi* | [**api_prds_delete**](docs/ApiApi.md#api_prds_delete) | **DELETE** /api/prds/{id}/ | 
*ApiApi* | [**api_prds_list**](docs/ApiApi.md#api_prds_list) | **GET** /api/prds/ | 
*ApiApi* | [**api_prds_partial_update**](docs/ApiApi.md#api_prds_partial_update) | **PATCH** /api/prds/{id}/ | 
*ApiApi* | [**api_prds_read**](docs/ApiApi.md#api_prds_read) | **GET** /api/prds/{id}/ | 
*ApiApi* | [**api_prds_update**](docs/ApiApi.md#api_prds_update) | **PUT** /api/prds/{id}/ | 
*ApiApi* | [**api_programs_create**](docs/ApiApi.md#api_programs_create) | **POST** /api/programs/ | 
*ApiApi* | [**api_programs_delete**](docs/ApiApi.md#api_programs_delete) | **DELETE** /api/programs/{program_id}/ | 
*ApiApi* | [**api_programs_list**](docs/ApiApi.md#api_programs_list) | **GET** /api/programs/ | 
*ApiApi* | [**api_programs_partial_update**](docs/ApiApi.md#api_programs_partial_update) | **PATCH** /api/programs/{program_id}/ | 
*ApiApi* | [**api_programs_read**](docs/ApiApi.md#api_programs_read) | **GET** /api/programs/{program_id}/ | 
*ApiApi* | [**api_programs_search_list**](docs/ApiApi.md#api_programs_search_list) | **GET** /api/programs/search | 
*ApiApi* | [**api_programs_update**](docs/ApiApi.md#api_programs_update) | **PUT** /api/programs/{program_id}/ | 
*ApiApi* | [**api_status_create**](docs/ApiApi.md#api_status_create) | **POST** /api/status/ | 
*ApiApi* | [**api_status_delete**](docs/ApiApi.md#api_status_delete) | **DELETE** /api/status/{status_id}/ | 
*ApiApi* | [**api_status_list**](docs/ApiApi.md#api_status_list) | **GET** /api/status/ | 
*ApiApi* | [**api_status_partial_update**](docs/ApiApi.md#api_status_partial_update) | **PATCH** /api/status/{status_id}/ | 
*ApiApi* | [**api_status_read**](docs/ApiApi.md#api_status_read) | **GET** /api/status/{status_id}/ | 
*ApiApi* | [**api_status_update**](docs/ApiApi.md#api_status_update) | **PUT** /api/status/{status_id}/ | 
*ApiApi* | [**api_user_create_create**](docs/ApiApi.md#api_user_create_create) | **POST** /api/user/create/ | 
*ApiApi* | [**api_user_read**](docs/ApiApi.md#api_user_read) | **GET** /api/user/ | 
*ApiApi* | [**api_user_search_list**](docs/ApiApi.md#api_user_search_list) | **GET** /api/user/search/ | 
*ApiApi* | [**api_user_update_partial_update**](docs/ApiApi.md#api_user_update_partial_update) | **PATCH** /api/user/update/ | 
*ApiApi* | [**api_user_update_update**](docs/ApiApi.md#api_user_update_update) | **PUT** /api/user/update/ | 
*ApiApi* | [**api_userstories_create**](docs/ApiApi.md#api_userstories_create) | **POST** /api/userstories/ | 
*ApiApi* | [**api_userstories_delete**](docs/ApiApi.md#api_userstories_delete) | **DELETE** /api/userstories/{id}/ | 
*ApiApi* | [**api_userstories_list**](docs/ApiApi.md#api_userstories_list) | **GET** /api/userstories/ | 
*ApiApi* | [**api_userstories_partial_update**](docs/ApiApi.md#api_userstories_partial_update) | **PATCH** /api/userstories/{id}/ | 
*ApiApi* | [**api_userstories_read**](docs/ApiApi.md#api_userstories_read) | **GET** /api/userstories/{id}/ | 
*ApiApi* | [**api_userstories_search_list**](docs/ApiApi.md#api_userstories_search_list) | **GET** /api/userstories/search | 
*ApiApi* | [**api_userstories_update**](docs/ApiApi.md#api_userstories_update) | **PUT** /api/userstories/{id}/ | 
*ChatApi* | [**chat_list**](docs/ChatApi.md#chat_list) | **GET** /chat | 
*ChatApi* | [**chat_upload_create**](docs/ChatApi.md#chat_upload_create) | **POST** /chat/upload/ | 
*GoalsApi* | [**goals_list_list**](docs/GoalsApi.md#goals_list_list) | **GET** /goals/list/ | 
*LeadersApi* | [**leaders_list**](docs/LeadersApi.md#leaders_list) | **GET** /leaders | 
*PrdApi* | [**prd_list_list**](docs/PrdApi.md#prd_list_list) | **GET** /prd/list/ | 
*ProgramsApi* | [**programs_list**](docs/ProgramsApi.md#programs_list) | **GET** /programs/ | 
*ProgramsApi* | [**programs_list_list**](docs/ProgramsApi.md#programs_list_list) | **GET** /programs/list/ | 
*ProgramsApi* | [**programs_search_list**](docs/ProgramsApi.md#programs_search_list) | **GET** /programs/search/ | 
*UserstoryApi* | [**userstory_search_list**](docs/UserstoryApi.md#userstory_search_list) | **GET** /userstory/search/ | 


## Documentation For Models

 - [Address](docs/Address.md)
 - [ApiPrdsList200Response](docs/ApiPrdsList200Response.md)
 - [ApiUserSearchList200Response](docs/ApiUserSearchList200Response.md)
 - [Goal](docs/Goal.md)
 - [GoalBase](docs/GoalBase.md)
 - [Organization](docs/Organization.md)
 - [PRD](docs/PRD.md)
 - [PRDDetail](docs/PRDDetail.md)
 - [Program](docs/Program.md)
 - [ProgramBase](docs/ProgramBase.md)
 - [Status](docs/Status.md)
 - [Tag](docs/Tag.md)
 - [User](docs/User.md)
 - [UserBase](docs/UserBase.md)
 - [UserCreate](docs/UserCreate.md)
 - [UserStory](docs/UserStory.md)
 - [UserUpdate](docs/UserUpdate.md)


<a id="documentation-for-authorization"></a>
## Documentation For Authorization

Endpoints do not require authorization.


## Author

chris@productpartner.ai


