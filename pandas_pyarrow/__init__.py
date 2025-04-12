from importlib.metadata import version

from .pda_converter import PandasArrowConverter
from .reverse_converter import ReversePandasArrowConverter

__version__ = version("pandas-pyarrow")

convert_to_pyarrow = PandasArrowConverter()
convert_to_numpy = ReversePandasArrowConverter()

__all__ = ["PandasArrowConverter", "ReversePandasArrowConverter", "convert_to_pyarrow", "convert_to_numpy"]
