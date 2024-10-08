# coding: utf-8

"""
    Product Partner API

    Product Partner APIs can create, list, and modify goals, prds, status updates, and other product management artifacts.

    The version of the OpenAPI document: v1
    Contact: chris@productpartner.ai
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import date
from pydantic import BaseModel, ConfigDict, Field, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class ApiPrdsCreateRequest(BaseModel):
    """
    ApiPrdsCreateRequest
    """ # noqa: E501
    title: StrictStr
    description: StrictStr
    body: StrictStr
    status: Optional[StrictStr] = None
    due_date: Optional[date] = None
    tags: Optional[List[StrictStr]] = Field(default=None, description="List of tags")
    stakeholder_users: Optional[List[StrictStr]] = Field(default=None, description="List of stakeholder user emails or UUIDs")
    programs: Optional[List[StrictStr]] = Field(default=None, description="List of program UUIDs")
    __properties: ClassVar[List[str]] = ["title", "description", "body", "status", "due_date", "tags", "stakeholder_users", "programs"]

    @field_validator('status')
    def status_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['DRAFT', 'PENDING_REVIEW', 'IN_REVIEW', 'APPROVED', 'PUBLISHED']):
            raise ValueError("must be one of enum values ('DRAFT', 'PENDING_REVIEW', 'IN_REVIEW', 'APPROVED', 'PUBLISHED')")
        return value

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of ApiPrdsCreateRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ApiPrdsCreateRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "title": obj.get("title"),
            "description": obj.get("description"),
            "body": obj.get("body"),
            "status": obj.get("status"),
            "due_date": obj.get("due_date"),
            "tags": obj.get("tags"),
            "stakeholder_users": obj.get("stakeholder_users"),
            "programs": obj.get("programs")
        })
        return _obj


