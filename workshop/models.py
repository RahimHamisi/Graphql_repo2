import uuid
from django.db import models


class Region(models.Model):
    primary_key = models.AutoField(primary_key=True)
    unique_id = models.UUIDField(editable=False, default=uuid.uuid4, unique=True)
    name = models.CharField(default="", max_length=255)
    postcode = models.CharField(default="", max_length=255)
    napa_id = models.CharField(default="", max_length=255)
    created_date = models.DateField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = "regions"
        ordering = ["-primary_key"]
        verbose_name_plural = "REGIONS"

    def __str__(self):
        return "{}-{}".format(self.name, self.postcode)
    
    def get_all_districts(self):
        return self.district_region.all()


class District(models.Model):
    primary_key = models.AutoField(primary_key=True)
    unique_id = models.UUIDField(editable=False, default=uuid.uuid4, unique=True)
    name = models.CharField(default="", max_length=255)
    postcode = models.CharField(default="", max_length=255)
    napa_id = models.CharField(default="", max_length=255,)
    region = models.ForeignKey(Region, on_delete=models.CASCADE, related_name="district_region")
    created_date = models.DateField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = "districts"
        ordering = ["primary_key"]
        verbose_name_plural = "DISTRICTS"

    def __str__(self):
        return "{}".format(self.name)


class Ward(models.Model):
    primary_key = models.AutoField(primary_key=True)
    unique_id = models.UUIDField(editable=False, default=uuid.uuid4, unique=True)
    name = models.CharField(default="", max_length=255)
    postcode = models.CharField(default="", max_length=255)
    napa_id = models.CharField(default="", max_length=255)
    district = models.ForeignKey(District, on_delete=models.CASCADE, related_name="ward_district")
    created_date = models.DateField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return "{}".format(self.name)

    class Meta:
        db_table = "wards"
        ordering = ["-primary_key"]
        verbose_name_plural = "WARDS"


class Street(models.Model):
    primary_key = models.AutoField(primary_key=True)
    unique_id = models.UUIDField(editable=False, default=uuid.uuid4, unique=True)
    name = models.CharField(default="", max_length=255)
    postcode = models.CharField(default="", max_length=255)
    napa_id = models.CharField(default="", max_length=255)
    ward = models.ForeignKey(Ward, on_delete=models.CASCADE, related_name="street_ward")
    created_date = models.DateField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return "{}".format(self.name)

    class Meta:
        db_table = "streets"
        ordering = ["-primary_key"]
        verbose_name_plural = "STREETS"