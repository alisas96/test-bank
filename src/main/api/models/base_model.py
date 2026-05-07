from pydantic import BaseModel as BM


class BaseModel(BM):
	model_config = {
        "populate_by_name": True
    }
