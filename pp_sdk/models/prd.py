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

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from pp_sdk.models.created_by import CreatedBy
from pp_sdk.models.programs_inner import ProgramsInner
from pp_sdk.models.stakeholder_users_inner import StakeholderUsersInner
from pp_sdk.models.tags_inner import TagsInner
from typing import Optional, Set
from typing_extensions import Self

class PRD(BaseModel):
    """
    PRD
    """ # noqa: E501
    id: Optional[StrictStr] = None
    title: Annotated[str, Field(min_length=1, strict=True, max_length=255)]
    description: Optional[StrictStr] = None
    body: Optional[StrictStr] = None
    status: Optional[StrictStr] = None
    due_date: Optional[datetime] = None
    modified_date: Optional[datetime] = None
    tags: Optional[List[TagsInner]] = None
    stakeholder_users: Optional[List[StakeholderUsersInner]] = None
    programs: Optional[List[ProgramsInner]] = None
    created_by: Optional[CreatedBy] = None
    created_date: Optional[datetime] = None
    __properties: ClassVar[List[str]] = ["id", "title", "description", "body", "status", "due_date", "modified_date", "tags", "stakeholder_users", "programs", "created_by", "created_date"]

    @field_validator('status')
    def status_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['DRAFT', 'PENDING_REVIEW', 'IN_REVIEW', 'APPROVED', 'ARCHIVED', 'COMPLETED']):
            raise ValueError("must be one of enum values ('DRAFT', 'PENDING_REVIEW', 'IN_REVIEW', 'APPROVED', 'ARCHIVED', 'COMPLETED')")
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
        """Create an instance of PRD from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        """
        excluded_fields: Set[str] = set([
            "id",
            "modified_date",
            "tags",
            "stakeholder_users",
            "programs",
            "created_date",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in tags (list)
        _items = []
        if self.tags:
            for _item_tags in self.tags:
                if _item_tags:
                    _items.append(_item_tags.to_dict())
            _dict['tags'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in stakeholder_users (list)
        _items = []
        if self.stakeholder_users:
            for _item_stakeholder_users in self.stakeholder_users:
                if _item_stakeholder_users:
                    _items.append(_item_stakeholder_users.to_dict())
            _dict['stakeholder_users'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in programs (list)
        _items = []
        if self.programs:
            for _item_programs in self.programs:
                if _item_programs:
                    _items.append(_item_programs.to_dict())
            _dict['programs'] = _items
        # override the default output from pydantic by calling `to_dict()` of created_by
        if self.created_by:
            _dict['created_by'] = self.created_by.to_dict()
        # set to None if description (nullable) is None
        # and model_fields_set contains the field
        if self.description is None and "description" in self.model_fields_set:
            _dict['description'] = None

        # set to None if body (nullable) is None
        # and model_fields_set contains the field
        if self.body is None and "body" in self.model_fields_set:
            _dict['body'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PRD from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "title": obj.get("title"),
            "description": obj.get("description"),
            "body": obj.get("body"),
            "status": obj.get("status"),
            "due_date": obj.get("due_date"),
            "modified_date": obj.get("modified_date"),
            "tags": [TagsInner.from_dict(_item) for _item in obj["tags"]] if obj.get("tags") is not None else None,
            "stakeholder_users": [StakeholderUsersInner.from_dict(_item) for _item in obj["stakeholder_users"]] if obj.get("stakeholder_users") is not None else None,
            "programs": [ProgramsInner.from_dict(_item) for _item in obj["programs"]] if obj.get("programs") is not None else None,
            "created_by": CreatedBy.from_dict(obj["created_by"]) if obj.get("created_by") is not None else None,
            "created_date": obj.get("created_date")
        })
        return _obj


