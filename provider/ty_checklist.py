from typing import Any

from dify_plugin import ToolProvider
from dify_plugin.errors.tool import ToolProviderCredentialValidationError


class TyChecklistProvider(ToolProvider):
    
    def _validate_credentials(self, credentials: dict[str, Any]) -> None:
        try:
            """
            Validation for TY Checklist Provider
            No credentials required for this provider
            """
            pass
        except Exception as e:
            raise ToolProviderCredentialValidationError(str(e))
