from .pda_converter import PandasArrowConverter

convert_to_pyarrow = PandasArrowConverter()
__all__ = ["PandasArrowConverter", "convert_to_pyarrow"]
