"""RAG schemas."""
from enum import Enum
from pathlib import Path
from typing import Optional, Union

from llama_index.core.embeddings import BaseEmbedding
from pydantic import BaseModel, ConfigDict, Field, PrivateAttr, model_validator


class BaseIndexConfig(BaseModel):
    """Common config for index.

    If add new subconfig, it is necessary to add the corresponding instance implementation in rag.factories.index.
    """

    model_config = ConfigDict(arbitrary_types_allowed=True)
    persist_path: Union[str, Path] = Field(description="The directory of saved data.")


class VectorIndexConfig(BaseIndexConfig):
    """Option for vector-based index."""

    embed_model: BaseEmbedding = Field(default=None, description="Embed model.")


class FAISSIndexConfig(VectorIndexConfig):
    """Option for faiss-based index."""




class MilvusIndexConfig(VectorIndexConfig):
    """Option for milvus-based index."""

    collection_name: str = Field(default="metagpt", description="The name of the collection.")
    uri: str = Field(default="./milvus_local.db", description="The uri of the index.")
    token: Optional[str] = Field(default=None, description="The token of the index.")
  


class BM25IndexConfig(BaseIndexConfig):
    """Option for bm25-based index."""

    _no_embedding: bool = PrivateAttr(default=True)



class ColBertIndexConfig(BaseIndexConfig):
    """Option for colbert-based index."""
    index_name: str = Field(default="", description="The name of the index.")
    model_name: str = Field(default="colbert-ir/colbertv2.0", description="The name of the ColBERT model.")
    nbits: int = Field(default=2, description="Number of bits for quantization.")
    gpus: int = Field(default=0, description="Number of GPUs to use.")
    ranks: int = Field(default=1, description="Number of ranks for distributed indexing.")
    doc_maxlen: int = Field(default=120, description="Maximum length of documents.")
    query_maxlen: int = Field(default=60, description="Maximum length of queries.")
    kmeans_niters: int = Field(default=4, description="Number of iterations for K-means clustering.")
class ParseResultType(str, Enum):
    """The result type for the parser."""

    TXT = "text"
    MD = "markdown"
    JSON = "json"




