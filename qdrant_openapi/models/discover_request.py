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


from typing import List, Optional
from pydantic import BaseModel, Field, StrictStr, conint, conlist
from qdrant_openapi.models.context_example_pair import ContextExamplePair
from qdrant_openapi.models.filter import Filter
from qdrant_openapi.models.lookup_location import LookupLocation
from qdrant_openapi.models.recommend_example import RecommendExample
from qdrant_openapi.models.search_params import SearchParams
from qdrant_openapi.models.shard_key_selector import ShardKeySelector
from qdrant_openapi.models.with_payload_interface import WithPayloadInterface
from qdrant_openapi.models.with_vector import WithVector

class DiscoverRequest(BaseModel):
    """
    Use context and a target to find the most similar points, constrained by the context.  # noqa: E501
    """
    shard_key: Optional[ShardKeySelector] = None
    target: Optional[RecommendExample] = None
    context: Optional[conlist(ContextExamplePair)] = Field(None, description="Pairs of { positive, negative } examples to constrain the search.  When using only the context (without a target), a special search - called context search - is performed where pairs of points are used to generate a loss that guides the search towards the zone where most positive examples overlap. This means that the score minimizes the scenario of finding a point closer to a negative than to a positive part of a pair.  Since the score of a context relates to loss, the maximum score a point can get is 0.0, and it becomes normal that many points can have a score of 0.0.  For discovery search (when including a target), the context part of the score for each pair is calculated +1 if the point is closer to a positive than to a negative part of a pair, and -1 otherwise.")
    filter: Optional[Filter] = None
    params: Optional[SearchParams] = None
    limit: conint(strict=True, ge=1) = Field(..., description="Max number of result to return")
    offset: Optional[conint(strict=True, ge=0)] = Field(None, description="Offset of the first result to return. May be used to paginate results. Note: large offset values may cause performance issues.")
    with_payload: Optional[WithPayloadInterface] = None
    with_vector: Optional[WithVector] = None
    using: Optional[StrictStr] = None
    lookup_from: Optional[LookupLocation] = None
    __properties = ["shard_key", "target", "context", "filter", "params", "limit", "offset", "with_payload", "with_vector", "using", "lookup_from"]

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
    def from_json(cls, json_str: str) -> DiscoverRequest:
        """Create an instance of DiscoverRequest from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of target
        if self.target:
            _dict['target'] = self.target.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in context (list)
        _items = []
        if self.context:
            for _item in self.context:
                if _item:
                    _items.append(_item.to_dict())
            _dict['context'] = _items
        # override the default output from pydantic by calling `to_dict()` of filter
        if self.filter:
            _dict['filter'] = self.filter.to_dict()
        # override the default output from pydantic by calling `to_dict()` of params
        if self.params:
            _dict['params'] = self.params.to_dict()
        # override the default output from pydantic by calling `to_dict()` of with_payload
        if self.with_payload:
            _dict['with_payload'] = self.with_payload.to_dict()
        # override the default output from pydantic by calling `to_dict()` of with_vector
        if self.with_vector:
            _dict['with_vector'] = self.with_vector.to_dict()
        # override the default output from pydantic by calling `to_dict()` of lookup_from
        if self.lookup_from:
            _dict['lookup_from'] = self.lookup_from.to_dict()
        # set to None if shard_key (nullable) is None
        # and __fields_set__ contains the field
        if self.shard_key is None and "shard_key" in self.__fields_set__:
            _dict['shard_key'] = None

        # set to None if target (nullable) is None
        # and __fields_set__ contains the field
        if self.target is None and "target" in self.__fields_set__:
            _dict['target'] = None

        # set to None if context (nullable) is None
        # and __fields_set__ contains the field
        if self.context is None and "context" in self.__fields_set__:
            _dict['context'] = None

        # set to None if filter (nullable) is None
        # and __fields_set__ contains the field
        if self.filter is None and "filter" in self.__fields_set__:
            _dict['filter'] = None

        # set to None if params (nullable) is None
        # and __fields_set__ contains the field
        if self.params is None and "params" in self.__fields_set__:
            _dict['params'] = None

        # set to None if offset (nullable) is None
        # and __fields_set__ contains the field
        if self.offset is None and "offset" in self.__fields_set__:
            _dict['offset'] = None

        # set to None if with_payload (nullable) is None
        # and __fields_set__ contains the field
        if self.with_payload is None and "with_payload" in self.__fields_set__:
            _dict['with_payload'] = None

        # set to None if with_vector (nullable) is None
        # and __fields_set__ contains the field
        if self.with_vector is None and "with_vector" in self.__fields_set__:
            _dict['with_vector'] = None

        # set to None if lookup_from (nullable) is None
        # and __fields_set__ contains the field
        if self.lookup_from is None and "lookup_from" in self.__fields_set__:
            _dict['lookup_from'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> DiscoverRequest:
        """Create an instance of DiscoverRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return DiscoverRequest.parse_obj(obj)

        _obj = DiscoverRequest.parse_obj({
            "shard_key": ShardKeySelector.from_dict(obj.get("shard_key")) if obj.get("shard_key") is not None else None,
            "target": RecommendExample.from_dict(obj.get("target")) if obj.get("target") is not None else None,
            "context": [ContextExamplePair.from_dict(_item) for _item in obj.get("context")] if obj.get("context") is not None else None,
            "filter": Filter.from_dict(obj.get("filter")) if obj.get("filter") is not None else None,
            "params": SearchParams.from_dict(obj.get("params")) if obj.get("params") is not None else None,
            "limit": obj.get("limit"),
            "offset": obj.get("offset"),
            "with_payload": WithPayloadInterface.from_dict(obj.get("with_payload")) if obj.get("with_payload") is not None else None,
            "with_vector": WithVector.from_dict(obj.get("with_vector")) if obj.get("with_vector") is not None else None,
            "using": obj.get("using"),
            "lookup_from": LookupLocation.from_dict(obj.get("lookup_from")) if obj.get("lookup_from") is not None else None
        })
        return _obj


