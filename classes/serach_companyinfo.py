from typing import Optional, Type

from langchain_core.callbacks import CallbackManagerForToolRun
from langchain_core.pydantic_v1 import BaseModel, Field
from langchain_core.tools import BaseTool

from langchain_community.tools.file_management.utils import (
    INVALID_PATH_TEMPLATE,
    BaseFileToolMixin,
)
from common.utils import COMPANYINFO_DB

class SearchInfoInput(BaseModel):
    """Input for WriteFileTool."""

    keywords: str = Field(..., description="Key phrases for company information, such as: 'DXC, generative AI, finance.'")


# キーワードに基づいてデータベースから情報検索
class SearchCompanyInfoTool(BaseFileToolMixin, BaseTool):
    """Tool that writes a file to disk."""

    name: str = "search_companyInfo"
    args_schema: Type[BaseModel] = SearchInfoInput
    description: str = "Use the keywords of a company to match similar information of company."

    def _run(
        self,
        keywords: str,
        run_manager: Optional[CallbackManagerForToolRun] = None,
    ) -> str:
        try:
            docs = COMPANYINFO_DB.similarity_search(keywords,k=6)
            companyInfo = ""
            for doc in docs:
                companyInfo += doc.page_content + "\n"
            return companyInfo
        except Exception as e:
            return "Failed to find the company information."