from rest_framework import permissions

class IsAuthorOrReadOnly(permissions.BasePermission):
    """
    Permite leitura para qualquer um, mas apenas edição/deleção para o autor.
    """
    def has_object_permission(self, request, view, obj):
        # GET, HEAD ou OPTIONS são seguros
        if request.method in permissions.SAFE_METHODS:
            return True
        
        # Permissões de escrita são dadas apenas ao autor
        return obj.author == request.user