from rest_framework.permissions import BasePermission

from agency.models import Agency
from agent.models import Agent
from myuser.models import UserProfile
from staff.models import Staff


class UserAuthRequired(BasePermission):
    def has_permission(self, request, view):
        return (
            request.user and request.user.is_authenticated
            and isinstance(request.user, UserProfile)
            and not request.user.is_banned
        )


class StaffAuthRequired(BasePermission):
    def has_permission(self, request, view):
        return (
            request.user and request.user.is_authenticated
            and isinstance(request.user, Staff)
        )


class AgentAuthRequired(BasePermission):
    def has_permission(self, request, view):
        return (
            request.user and request.user.is_authenticated
            and isinstance(request.user, Agent)
        )


class AgencyAuthRequired(BasePermission):
    def has_permission(self, request, view):
        return (
            request.user and request.user.is_authenticated
            and isinstance(request.user, Agency)
        )


class FirstClassAgencyAuthRequired(BasePermission):
    def has_permission(self, request, view):
        return (
            request.user and request.user.is_authenticated
            and isinstance(request.user, Agency)
            and request.user.can_create_agency
        )
