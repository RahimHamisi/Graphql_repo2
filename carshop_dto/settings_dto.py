import graphene
from carshop_dto.response_dto import PageObject, ResponseObjects


class RegionInputObject(graphene.InputObjectType):
    unique_id = graphene.String()
    name = graphene.String()
    postcode = graphene.String()
    napa_id = graphene.String()


class RegionObject(graphene.ObjectType):
    id = graphene.String()
    unique_id = graphene.String()
    name = graphene.String()
    postcode = graphene.String()
    napa_id = graphene.String()
    created_date = graphene.Date()
    is_active = graphene.Boolean()
    has_district = graphene.Boolean()


class RegionFilterInput(graphene.InputObjectType):
    page_number = graphene.Int()
    items_per_page = graphene.Int()


class RegionResponseObject(graphene.ObjectType):
    response = graphene.Field(ResponseObjects)
    page = graphene.Field(PageObject)
    data = graphene.List(RegionObject)
    