import pytest

def get_file_name(file_names):
    return [file_name.split('.')[0] for file_name in file_names]

def test_get_file_name():
    file_names = ['file1.txt', 'file2.pdf', 'file3.docx']
    expected_result = ['file1', 'file2', 'file3']
    assert get_file_name(file_names) == expected_result

def test_get_file_name_empty_list():
    file_names = []
    expected_result = []
    assert get_file_name(file_names) == expected_result

def test_get_file_name_no_extension():
    file_names = ['file1', 'file2', 'file3']
    expected_result = ['file1', 'file2', 'file3']
    assert get_file_name(file_names) == expected_result

def test_get_file_name_multiple_dots():
    file_names = ['file1.txt.pdf', 'file2.pdf.docx']
    expected_result = ['file1', 'file2']
    assert get_file_name(file_names) == expected_result
