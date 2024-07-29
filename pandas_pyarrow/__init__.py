from importlib.metadata import version

from .pda_converter import PandasArrowConverter
from .reverse_converter import convert_to_numpy

__version__ = version("pandas-pyarrow")

convert_to_pyarrow = PandasArrowConverter()
__all__ = ["PandasArrowConverter", "convert_to_pyarrow", "convert_to_numpy"]
