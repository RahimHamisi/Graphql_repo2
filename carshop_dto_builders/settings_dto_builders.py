import graphene

from carshop_dto.settings_dto import RegionObject
from workshop.models import *


class SettingsBuilders:

    def get_all_region_data(unique_id):
        if unique_id is not None:
            region = Region.objects.filter(unique_id=unique_id).first()

            data = RegionObject(
                id = region.primary_key,
                unique_id = region.unique_id,
                name = region.name,
                postcode = region.postcode,
                napa_id = region.napa_id,
                created_date = region.created_date,
                is_active = region.is_active,
                has_district = True if region.get_all_districts() else False
            )

        return data


