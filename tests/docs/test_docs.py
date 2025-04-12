from pathlib import Path

import pytest
from sybil import Sybil
from sybil.parsers.codeblock import PythonCodeBlockParser
from sybil.parsers.doctest import DocTestParser


def collect_examples():
    docs_folder_path = Path(__file__).parent.parent.parent / "docs" / "source"
    assert docs_folder_path.exists(), f"Docs path doesn't exist: {docs_folder_path.resolve()}"

    all_rst_files = list(docs_folder_path.glob("*.rst"))
    print(f"Found {len(all_rst_files)} .rst files in docs folder.")
    # Configure Sybil
    sybil = Sybil(
        parsers=[
            DocTestParser(),
            PythonCodeBlockParser(),
        ],
        pattern="*.rst",
        path=docs_folder_path.as_posix(),
    )
    examples_list = []
    for f_path in all_rst_files:
        document_ = sybil.parse(f_path)

        examples_ = list(document_)
        examples_files = [e.path for e in examples_]
        examples_start_lines = [e.start for e in examples_]

        examples_list.extend(zip(examples_files, examples_start_lines, examples_))
        # examples_list=[example for example in examples_]

    return examples_list


@pytest.mark.parametrize("file_path, line, example", collect_examples())
def test_doc_examples(file_path, line, example):
    example.evaluate()
