import pytest

from search_text import search_text

test_cases = [
    ('Peter', '1, 20, 75'),
    ('peter', '1, 20, 75'),
    ('pick', '30, 58'),
    ('pi', '30, 37, 43, 51, 58'),
    ('z', None),
    ('Peterz', None),
    ('!', '92'),
]


@pytest.mark.parametrize('sub_text, expected', test_cases)
def test_search_text(sub_text, expected):
    text_to_search = 'Peter told me that peter the pickle piper ' \
                     'piped a pitted pickle before he petered out. Phew!'
    assert search_text(text_to_search, sub_text) == expected
