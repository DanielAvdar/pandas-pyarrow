from importlib.metadata import version

from .pda_converter import PandasArrowConverter
from .reverse_converter import ReversePandasArrowConverter

__version__ = version("pandas-pyarrow")

convert_to_pyarrow = PandasArrowConverter().__call__
convert_to_numpy = ReversePandasArrowConverter().__call__

__all__ = ["PandasArrowConverter", "ReversePandasArrowConverter", "convert_to_pyarrow", "convert_to_numpy"]
