import graphene


from workshop.models import Region
from carshop_dto.settings_dto import RegionResponseObject, RegionFilterInput
from carshop_dto_builders.settings_dto_builders import SettingsBuilders
from carshop_dto.response_dto import ResponseObjects, PageObject
from django.core.paginator import Paginator


class Query(graphene.ObjectType):
    get_all_regions = graphene.Field(RegionResponseObject, filtering=RegionFilterInput())


    @staticmethod
    def resolve_get_all_regions(self, info, filtering=None, **kwargs):
        try:
            page_number = 1 if filtering.page_number is None else filtering.page_number
            items_per_page = 10 if filtering.items_per_page is None else filtering.items_per_page

            query_set = Region.objects.filter(is_active=True).only('unique_id')
            paginated_sectors = Paginator(query_set, items_per_page)
            page_object, paged_data = PageObject.get_page(page_datas=paginated_sectors, page_number=page_number, total_items=query_set.count())
            resp_data = list(map(lambda query: SettingsBuilders.get_all_region_data(unique_id=query.unique_id), paged_data))

            print(ResponseObjects.get_response(id=1))
            return info.return_type.graphene_type(response=ResponseObjects.get_response(id=1), data=resp_data, page=page_object)
        except Exception as e:
            return info.return_type.graphene_type(response=ResponseObjects.get_response(id=5))
    