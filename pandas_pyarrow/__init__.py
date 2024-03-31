from importlib.metadata import version

from .pda_converter import PandasArrowConverter

__version__ = version("pandas-pyarrow")
convert_to_pyarrow = PandasArrowConverter()
__all__ = ["PandasArrowConverter", "convert_to_pyarrow"]
