import graphene
import logging
from graphene_django import DjangoObjectType

from vehicles.models import Vehicle


logger = logging.getLogger(__name__)


class VehicleType(DjangoObjectType):
    class Meta:
        model = Vehicle
        fields = (
            'id',
            'uuid',
            'brand',
            'model',
            'plate_number',
            'owners_name',
            'created_at',
            'updated_at',
        )


class Query(graphene.ObjectType):
    all_vehicles = graphene.List(VehicleType)
    vehicle_by_id = graphene.Field(
        VehicleType,
        id=graphene.Int(required=True),
    )

    def resolve_all_vehicles(root, info):
        return Vehicle.objects.all()

    def resolve_vehicle_by_id(root, info, id):
        try:
            return Vehicle.objects.get(id=id)
        except Exception as e:
            logger.error(e)
            return None


class VehicleInput(graphene.InputObjectType):
    brand = graphene.String()
    model = graphene.String()
    owners_name = graphene.String()
    plate_number = graphene.String()


class CreateVehicle(graphene.Mutation):
    class Arguments:
        input = VehicleInput(required=True)

    ok = graphene.Boolean()
    vehicle = graphene.Field(VehicleType)

    def mutate(root, info, input=None):
        ok = True
        vehicle_instance = Vehicle(**input)
        vehicle_instance.save()
        return CreateVehicle(ok=ok, vehicle=vehicle_instance)


class UpdateVehicle(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        input = VehicleInput(required=True)

    ok = graphene.Boolean()
    vehicle = graphene.Field(VehicleType)

    def mutate(root, info, id, input=None):
        ok = False
        vehicle_instance = Vehicle.objects.get(pk=id)
        if vehicle_instance:
            ok = True
            vehicle_instance.brand = input.brand
            vehicle_instance.model = input.model
            vehicle_instance.owners_name = input.owners_name
            vehicle_instance.plate_number = input.plate_number
            vehicle_instance.save()
            return UpdateVehicle(ok=ok, vehicle=vehicle_instance)
        return UpdateVehicle(ok=ok, vehicle=None)


class DeleteVehicle(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)

    ok = graphene.Boolean()

    def mutate(root, info, id):
        ok = False
        vehicle_instance = Vehicle.objects.get(pk=id)
        if vehicle_instance:
            ok = True
            vehicle_instance.delete()
        return DeleteVehicle(ok=ok)


class Mutation(graphene.ObjectType):
    create_vehicle = CreateVehicle.Field()
    update_vehicle = UpdateVehicle.Field()
    delete_vehicle = DeleteVehicle.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
