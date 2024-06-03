from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict
from cognee.root_dir import get_absolute_path
from cognee.shared.data_models import MonitoringTool

class BaseConfig(BaseSettings):
    data_root_directory: str = get_absolute_path(".data")
    monitoring_tool: object = MonitoringTool.LANGFUSE
    graphistry_username: str = None
    graphistry_password: str = None

    model_config = SettingsConfigDict(env_file = ".env", extra = "allow")

    def to_dict(self) -> dict:
        return {
            "data_root_directory": self.data_root_directory,
            "monitoring_tool": self.monitoring_tool,
        }

@lru_cache
def get_base_config():
    return BaseConfig()
