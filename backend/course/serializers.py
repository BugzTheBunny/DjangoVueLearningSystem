from dataclasses import fields
import imp
from pyexpat import model
from rest_framework import serializers

from .models import Course, Lesson, Comment, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            'id',
            'title',
            'slug'
        )


class CourseListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course

        fields = (
            'id',
            'title',
            'slug',
            'short_description',
            'get_image'
        )


class CourseDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course

        fields = (
            'id',
            'title',
            'slug',
            'short_description',
            'long_description'
        )


class LessonListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = (
            'id',
            'title',
            'slug',
            'short_description',
            'long_description'
        )


class CommentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = (
            'id',
            'name',
            'content',
            'created_at'
        )
