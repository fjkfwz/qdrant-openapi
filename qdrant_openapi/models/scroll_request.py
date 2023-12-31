# coding: utf-8

"""
    Qdrant API

    API description for Qdrant vector search engine.  This document describes CRUD and search operations on collections of points (vectors with payload).  Qdrant supports any combinations of `should`, `must` and `must_not` conditions, which makes it possible to use in applications when object could not be described solely by vector. It could be location features, availability flags, and other custom properties businesses should take into account. ## Examples This examples cover the most basic use-cases - collection creation and basic vector search. ### Create collection First - let's create a collection with dot-production metric. ``` curl -X PUT 'http://localhost:6333/collections/test_collection' \\   -H 'Content-Type: application/json' \\   --data-raw '{     \"vectors\": {       \"size\": 4,       \"distance\": \"Dot\"     }   }'  ``` Expected response: ``` {     \"result\": true,     \"status\": \"ok\",     \"time\": 0.031095451 } ``` We can ensure that collection was created: ``` curl 'http://localhost:6333/collections/test_collection' ``` Expected response: ``` {   \"result\": {     \"status\": \"green\",     \"vectors_count\": 0,     \"segments_count\": 5,     \"disk_data_size\": 0,     \"ram_data_size\": 0,     \"config\": {       \"params\": {         \"vectors\": {           \"size\": 4,           \"distance\": \"Dot\"         }       },       \"hnsw_config\": {         \"m\": 16,         \"ef_construct\": 100,         \"full_scan_threshold\": 10000       },       \"optimizer_config\": {         \"deleted_threshold\": 0.2,         \"vacuum_min_vector_number\": 1000,         \"max_segment_number\": 5,         \"memmap_threshold\": 50000,         \"indexing_threshold\": 20000,         \"flush_interval_sec\": 1       },       \"wal_config\": {         \"wal_capacity_mb\": 32,         \"wal_segments_ahead\": 0       }     }   },   \"status\": \"ok\",   \"time\": 2.1199e-05 } ```  ### Add points Let's now add vectors with some payload: ``` curl -L -X PUT 'http://localhost:6333/collections/test_collection/points?wait=true' \\ -H 'Content-Type: application/json' \\ --data-raw '{   \"points\": [     {\"id\": 1, \"vector\": [0.05, 0.61, 0.76, 0.74], \"payload\": {\"city\": \"Berlin\"}},     {\"id\": 2, \"vector\": [0.19, 0.81, 0.75, 0.11], \"payload\": {\"city\": [\"Berlin\", \"London\"] }},     {\"id\": 3, \"vector\": [0.36, 0.55, 0.47, 0.94], \"payload\": {\"city\": [\"Berlin\", \"Moscow\"] }},     {\"id\": 4, \"vector\": [0.18, 0.01, 0.85, 0.80], \"payload\": {\"city\": [\"London\", \"Moscow\"] }},     {\"id\": 5, \"vector\": [0.24, 0.18, 0.22, 0.44], \"payload\": {\"count\": [0]}},     {\"id\": 6, \"vector\": [0.35, 0.08, 0.11, 0.44]}   ] }' ``` Expected response: ``` {     \"result\": {         \"operation_id\": 0,         \"status\": \"completed\"     },     \"status\": \"ok\",     \"time\": 0.000206061 } ``` ### Search with filtering Let's start with a basic request: ``` curl -L -X POST 'http://localhost:6333/collections/test_collection/points/search' \\ -H 'Content-Type: application/json' \\ --data-raw '{     \"vector\": [0.2,0.1,0.9,0.7],     \"top\": 3 }' ``` Expected response: ``` {     \"result\": [         { \"id\": 4, \"score\": 1.362, \"payload\": null, \"version\": 0 },         { \"id\": 1, \"score\": 1.273, \"payload\": null, \"version\": 0 },         { \"id\": 3, \"score\": 1.208, \"payload\": null, \"version\": 0 }     ],     \"status\": \"ok\",     \"time\": 0.000055785 } ``` But result is different if we add a filter: ``` curl -L -X POST 'http://localhost:6333/collections/test_collection/points/search' \\ -H 'Content-Type: application/json' \\ --data-raw '{     \"filter\": {         \"should\": [             {                 \"key\": \"city\",                 \"match\": {                     \"value\": \"London\"                 }             }         ]     },     \"vector\": [0.2, 0.1, 0.9, 0.7],     \"top\": 3 }' ``` Expected response: ``` {     \"result\": [         { \"id\": 4, \"score\": 1.362, \"payload\": null, \"version\": 0 },         { \"id\": 2, \"score\": 0.871, \"payload\": null, \"version\": 0 }     ],     \"status\": \"ok\",     \"time\": 0.000093972 } ``` 

    The version of the OpenAPI document: v1.7.x
    Contact: andrey@vasnetsov.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Optional
from pydantic import BaseModel, Field, conint
from qdrant_openapi.models.extended_point_id import ExtendedPointId
from qdrant_openapi.models.filter import Filter
from qdrant_openapi.models.shard_key_selector import ShardKeySelector
from qdrant_openapi.models.with_payload_interface import WithPayloadInterface
from qdrant_openapi.models.with_vector import WithVector

class ScrollRequest(BaseModel):
    """
    Scroll request - paginate over all points which matches given condition  # noqa: E501
    """
    shard_key: Optional[ShardKeySelector] = None
    offset: Optional[ExtendedPointId] = None
    limit: Optional[conint(strict=True, ge=1)] = Field(None, description="Page size. Default: 10")
    filter: Optional[Filter] = None
    with_payload: Optional[WithPayloadInterface] = None
    with_vector: Optional[WithVector] = None
    __properties = ["shard_key", "offset", "limit", "filter", "with_payload", "with_vector"]

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
    def from_json(cls, json_str: str) -> ScrollRequest:
        """Create an instance of ScrollRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of shard_key
        if self.shard_key:
            _dict['shard_key'] = self.shard_key.to_dict()
        # override the default output from pydantic by calling `to_dict()` of offset
        if self.offset:
            _dict['offset'] = self.offset.to_dict()
        # override the default output from pydantic by calling `to_dict()` of filter
        if self.filter:
            _dict['filter'] = self.filter.to_dict()
        # override the default output from pydantic by calling `to_dict()` of with_payload
        if self.with_payload:
            _dict['with_payload'] = self.with_payload.to_dict()
        # override the default output from pydantic by calling `to_dict()` of with_vector
        if self.with_vector:
            _dict['with_vector'] = self.with_vector.to_dict()
        # set to None if shard_key (nullable) is None
        # and __fields_set__ contains the field
        if self.shard_key is None and "shard_key" in self.__fields_set__:
            _dict['shard_key'] = None

        # set to None if offset (nullable) is None
        # and __fields_set__ contains the field
        if self.offset is None and "offset" in self.__fields_set__:
            _dict['offset'] = None

        # set to None if limit (nullable) is None
        # and __fields_set__ contains the field
        if self.limit is None and "limit" in self.__fields_set__:
            _dict['limit'] = None

        # set to None if filter (nullable) is None
        # and __fields_set__ contains the field
        if self.filter is None and "filter" in self.__fields_set__:
            _dict['filter'] = None

        # set to None if with_payload (nullable) is None
        # and __fields_set__ contains the field
        if self.with_payload is None and "with_payload" in self.__fields_set__:
            _dict['with_payload'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ScrollRequest:
        """Create an instance of ScrollRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ScrollRequest.parse_obj(obj)

        _obj = ScrollRequest.parse_obj({
            "shard_key": ShardKeySelector.from_dict(obj.get("shard_key")) if obj.get("shard_key") is not None else None,
            "offset": ExtendedPointId.from_dict(obj.get("offset")) if obj.get("offset") is not None else None,
            "limit": obj.get("limit"),
            "filter": Filter.from_dict(obj.get("filter")) if obj.get("filter") is not None else None,
            "with_payload": WithPayloadInterface.from_dict(obj.get("with_payload")) if obj.get("with_payload") is not None else None,
            "with_vector": WithVector.from_dict(obj.get("with_vector")) if obj.get("with_vector") is not None else None
        })
        return _obj


