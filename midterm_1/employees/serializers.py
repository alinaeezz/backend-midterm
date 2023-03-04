from rest_framework import serializers
from employees.models import Position, Salary

    def create(self, validated_data):
        full_name = Employees(**validated_data)
        full_name.save()
        return category

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.save()
        return instance


    def create(self, validated_data):
        product = Product(**validated_data)
        product.save()
        return product

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.price = validated_data.get('price', instance.price)
        instance.code = validated_data.get('code', instance.code)
        instance.category_id = validated_data.get('category_id', instance.category_id)

        instance.save()
        return instance
