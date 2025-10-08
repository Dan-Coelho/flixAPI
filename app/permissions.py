from rest_framework import permissions


class GlobalDefaultPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        view = str(view).split('.')[0].removeprefix('<')
        method = request.method
        print(view, method)
        if method in permissions.SAFE_METHODS:
            return request.user.has_perm(f'{view.lower()}.view_{view.lower().removesuffix("s")}')
        if method == 'POST':
            return request.user.has_perm(f'{view.lower()}.add_{view.lower().removesuffix("s")}')
        if method in ['PUT', 'PATCH']:
            return request.user.has_perm(f'{view.lower()}.change_{view.lower().removesuffix("s")}')
        if method == 'DELETE':
            return request.user.has_perm(f'{view.lower()}.delete_{view.lower().removesuffix("s")}')
        return False
    