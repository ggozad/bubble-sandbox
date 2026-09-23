import pydantic
import pytest

from bubble_sandbox import models as bs_models


def test_executeresult_rejects_unknown_field():
    with pytest.raises(pydantic.ValidationError, match="output"):
        bs_models.ExecuteResult(output="hello", exit_code=0)


def test_executeresult_model_validate_rejects_unknown_field():
    with pytest.raises(pydantic.ValidationError, match="output"):
        bs_models.ExecuteResult.model_validate_json(
            '{"output": "x", "exit_code": -1}'
        )
