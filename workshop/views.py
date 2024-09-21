import graphene

from carshop_dto.settings_dto import RegionInputObject, RegionObject
from carshop_dto_builders.settings_dto_builders import SettingsBuilders

from .models import *


# Endpoint to create Region
class CreateRegionMutation(graphene.Mutation):
    class Arguments:
        input = RegionInputObject() # Input za frontend

    data = graphene.Field(RegionObject) # Output za frontend

    @classmethod
    def mutate(self, root, info, input):
        region = Region.objects.create(name=input.name, postcode=input.postcode, napa_id=input.napa_id)
        data = SettingsBuilders.get_all_region_data(unique_id=region.unique_id)
        return self(data=data)



# Endpoint to update Region
class UpdateRegionMutation(graphene.Mutation):
    class Arguments:
        input = RegionInputObject() # Input za frontend

    data = graphene.Field(RegionObject)

    @classmethod
    def mutate(self, root, info, input):
        
        if input.unique_id is not None:
            region = Region.objects.filter(unique_id=input.unique_id).first() # SINGLE OBJECT

            region.name = input.name
            region.postcode = input.postcode
            region.napa_id = input.napa_id
            region.save()

            data = SettingsBuilders.get_all_region_data(unique_id=region.unique_id)
            
        return self(data=data)
    


class DeleteRegionMutation(graphene.Mutation):
    class Arguments:
        unique_id = graphene.String()

    success = graphene.Boolean()

    @classmethod
    def mutate(self, root, info, unique_id):

        # Peform SOFT DELETE
        Region.objects.filter(unique_id=unique_id).update(is_active=False)

        return True
    
    
class Carshop(graphene.ObjectType):
    create_region=CreateRegionMutation.Field()
    update_region=UpdateRegionMutation.Field()
    dlete_region=DeleteRegionMutation.Field()
    