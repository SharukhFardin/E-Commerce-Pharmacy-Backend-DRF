from rest_framework.permissions import BasePermission
from we.models import OrganizationUser

# IsOwner, IsAdmins, IsManager, IsStaff, IsCustomer type of permissions

class RoleBasedPermission(BasePermission):
    def has_permission(self, request, view):
        user = request.user

        # Check if user has appropriate role for the view
        required_role = view.required_role  # You can define this attribute in your views
        user_role = user.organizationuser.role

        if user_role == required_role:
            return True

        return False
    

class IsOwner(BasePermission):
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False

        # Retrieve the authenticated owner's role
        try:
            owner_role = request.user.organizationuser.role
        except OrganizationUser.DoesNotExist:
            return False

        # Customize permissions based on role
        if owner_role == 'owner':
            return True
        # Add more role-specific logic here if needed

        return False


class IsManager(BasePermission):
    def has_permission(self, request, view):
        return request.user.user_type == 'manager'
    
