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
from pp_sdk.models.organization import Organization
from pp_sdk.models.tag import Tag
from pp_sdk.models.user_base import UserBase
from typing import Optional, Set
from typing_extensions import Self

class UserStory(BaseModel):
    """
    UserStory
    """ # noqa: E501
    id: Optional[StrictStr] = None
    prd: Optional[StrictStr]
    as_a: Optional[Annotated[str, Field(strict=True, max_length=255)]] = None
    i_want_to: Optional[Annotated[str, Field(strict=True, max_length=255)]] = None
    so_that: Optional[Annotated[str, Field(strict=True, max_length=255)]] = None
    freetext_override: Optional[StrictStr] = None
    created_date: Optional[datetime] = None
    modified_date: Optional[datetime] = None
    due_date: Optional[datetime] = None
    status: Optional[StrictStr] = None
    priority: Optional[Annotated[str, Field(strict=True, max_length=50)]] = None
    tags: Optional[List[Tag]] = None
    created_by: Optional[UserBase] = None
    organization: Optional[Organization] = None
    __properties: ClassVar[List[str]] = ["id", "prd", "as_a", "i_want_to", "so_that", "freetext_override", "created_date", "modified_date", "due_date", "status", "priority", "tags", "created_by", "organization"]

    @field_validator('status')
    def status_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['RED', 'YELLOW', 'GREEN', 'NOT_STARTED', 'COMPLETED', 'COMPLETED_LATE', 'CANCELLED', 'DEFERRED']):
            raise ValueError("must be one of enum values ('RED', 'YELLOW', 'GREEN', 'NOT_STARTED', 'COMPLETED', 'COMPLETED_LATE', 'CANCELLED', 'DEFERRED')")
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
        """Create an instance of UserStory from a JSON string"""
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
        """
        excluded_fields: Set[str] = set([
            "id",
            "created_date",
            "modified_date",
            "tags",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in tags (list)
        _items = []
        if self.tags:
            for _item in self.tags:
                if _item:
                    _items.append(_item.to_dict())
            _dict['tags'] = _items
        # override the default output from pydantic by calling `to_dict()` of created_by
        if self.created_by:
            _dict['created_by'] = self.created_by.to_dict()
        # override the default output from pydantic by calling `to_dict()` of organization
        if self.organization:
            _dict['organization'] = self.organization.to_dict()
        # set to None if prd (nullable) is None
        # and model_fields_set contains the field
        if self.prd is None and "prd" in self.model_fields_set:
            _dict['prd'] = None

        # set to None if as_a (nullable) is None
        # and model_fields_set contains the field
        if self.as_a is None and "as_a" in self.model_fields_set:
            _dict['as_a'] = None

        # set to None if i_want_to (nullable) is None
        # and model_fields_set contains the field
        if self.i_want_to is None and "i_want_to" in self.model_fields_set:
            _dict['i_want_to'] = None

        # set to None if so_that (nullable) is None
        # and model_fields_set contains the field
        if self.so_that is None and "so_that" in self.model_fields_set:
            _dict['so_that'] = None

        # set to None if freetext_override (nullable) is None
        # and model_fields_set contains the field
        if self.freetext_override is None and "freetext_override" in self.model_fields_set:
            _dict['freetext_override'] = None

        # set to None if due_date (nullable) is None
        # and model_fields_set contains the field
        if self.due_date is None and "due_date" in self.model_fields_set:
            _dict['due_date'] = None

        # set to None if priority (nullable) is None
        # and model_fields_set contains the field
        if self.priority is None and "priority" in self.model_fields_set:
            _dict['priority'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of UserStory from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "prd": obj.get("prd"),
            "as_a": obj.get("as_a"),
            "i_want_to": obj.get("i_want_to"),
            "so_that": obj.get("so_that"),
            "freetext_override": obj.get("freetext_override"),
            "created_date": obj.get("created_date"),
            "modified_date": obj.get("modified_date"),
            "due_date": obj.get("due_date"),
            "status": obj.get("status"),
            "priority": obj.get("priority"),
            "tags": [Tag.from_dict(_item) for _item in obj["tags"]] if obj.get("tags") is not None else None,
            "created_by": UserBase.from_dict(obj["created_by"]) if obj.get("created_by") is not None else None,
            "organization": Organization.from_dict(obj["organization"]) if obj.get("organization") is not None else None
        })
        return _obj


