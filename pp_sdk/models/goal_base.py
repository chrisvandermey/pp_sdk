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


from typing import Any, Dict, Optional
from pydantic import BaseModel, Field, StrictStr, constr

class GoalBase(BaseModel):
    """
    GoalBase
    """
    id: Optional[StrictStr] = None
    name: constr(strict=True, max_length=255, min_length=1) = Field(...)
    goal_language: constr(strict=True, min_length=1) = Field(...)
    description: Optional[StrictStr] = None
    additional_properties: Dict[str, Any] = {}
    __properties = ["id", "name", "goal_language", "description"]

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> GoalBase:
        """Create an instance of GoalBase from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                            "id",
                            "additional_properties"
                          },
                          exclude_none=True)
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        # set to None if description (nullable) is None
        # and __fields_set__ contains the field
        if self.description is None and "description" in self.__fields_set__:
            _dict['description'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> GoalBase:
        """Create an instance of GoalBase from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return GoalBase.parse_obj(obj)

        _obj = GoalBase.parse_obj({
            "id": obj.get("id"),
            "name": obj.get("name"),
            "goal_language": obj.get("goal_language"),
            "description": obj.get("description")
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj


