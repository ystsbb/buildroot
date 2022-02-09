import pytest
import checkpackagelib.test_util as util
import checkpackagelib.lib_hash as m


HashNumberOfFields = [
    ('empty file',
     'any',
     '',
     []),
    ('empty line',
     'any',
     '\n',
     []),
    ('ignore whitespace',
     'any',
     '\t\n',
     []),
    ('ignore comments',
     'any',
     '# text\n',
     []),
    ('1 field',
     'any',
     'field1\n',
     [['any:1: expected three fields (url#adding-packages-hash)',
       'field1\n']]),
    ('2 fields',
     'any',
     'field1 field2\n',
     [['any:1: expected three fields (url#adding-packages-hash)',
       'field1 field2\n']]),
    ('4 fields',
     'any',
     'field1 field2 field3 field4\n',
     [['any:1: expected three fields (url#adding-packages-hash)',
       'field1 field2 field3 field4\n']]),
    ('with 1 space',
     'any',
     'field1 field2 field3\n',
     []),
    ('many spaces',
     'any',
     '   field1   field2   field3\n',
     []),
    ('tabs',
     'any',
     'field1\tfield2\tfield3\n',
     []),
    ('mix of tabs and spaces',
     'any',
     '\tfield1\t field2\t field3 \n',
     []),
    ]


@pytest.mark.parametrize('testname,filename,string,expected', HashNumberOfFields)
def test_HashNumberOfFields(testname, filename, string, expected):
    warnings = util.check_file(m.HashNumberOfFields, filename, string)
    assert warnings == expected


HashType = [
    ('ignore empty files',
     'any',
     '',
     []),
    ('ignore 1 field',
     'any',
     'text\n',
     []),
    ('wrong type',
     'any',
     'text text\n',
     [['any:1: unexpected type of hash (url#adding-packages-hash)',
       'text text\n']]),
    ('md5 (good)',
     'any',
     'md5 12345678901234567890123456789012\n',
     []),
    ('md5 (short)',
     'any',
     'md5 123456\n',
     [['any:1: hash size does not match type (url#adding-packages-hash)',
       'md5 123456\n',
       'expected 32 hex digits']]),
    ('ignore space before',
     'any',
     ' md5 12345678901234567890123456789012\n',
     []),
    ('2 spaces',
     'any',
     'md5  12345678901234567890123456789012\n',
     []),
    ('ignore tabs',
     'any',
     'md5\t12345678901234567890123456789012\n',
     []),
    ('common typo',
     'any',
     'md5sum 12345678901234567890123456789012\n',
     [['any:1: unexpected type of hash (url#adding-packages-hash)',
       'md5sum 12345678901234567890123456789012\n']]),
    ('md5 (too long)',
     'any',
     'md5 123456789012345678901234567890123\n',
     [['any:1: hash size does not match type (url#adding-packages-hash)',
       'md5 123456789012345678901234567890123\n',
       'expected 32 hex digits']]),
    ('sha1 (good)',
     'any',
     'sha1 1234567890123456789012345678901234567890\n',
     []),
    ('sha256',
     'any',
     'sha256 1234567890123456789012345678901234567890123456789012345678901234\n',
     []),
    ('sha384',
     'any',
     'sha384 123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456\n',
     []),
    ('sha512',
     'any',
     'sha512 1234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678'
     '9012345678\n',
     []),
    ]


@pytest.mark.parametrize('testname,filename,string,expected', HashType)
def test_HashType(testname, filename, string, expected):
    warnings = util.check_file(m.HashType, filename, string)
    assert warnings == expected


HashSpaces = [
    ('ignore empty files',
     'any',
     '',
     []),
    ('ignore 1 field',
     'any',
     'text\n',
     []),
    ('ignore comments',
     'any',
     '# type  1234567890123456789012345678901234567890  file\n',
     []),
    ('ignore trailing space',
     'any',
     'type  1234567890123456789012345678901234567890  file\t \n',
     []),
    ('2 spaces',
     'any',
     'type  1234567890123456789012345678901234567890  file\n',
     []),
    ('1 space',
     'any',
     'type 1234567890123456789012345678901234567890 file\n',
     [['any:1: separation does not match expectation (url#adding-packages-hash)',
       'type 1234567890123456789012345678901234567890 file\n']]),
    ('3 spaces',
     'any',
     'type   1234567890123456789012345678901234567890   file\n',
     [['any:1: separation does not match expectation (url#adding-packages-hash)',
       'type   1234567890123456789012345678901234567890   file\n']]),
    ('tabs',
     'any',
     'type\t1234567890123456789012345678901234567890\tfile\n',
     [['any:1: separation does not match expectation (url#adding-packages-hash)',
       'type\t1234567890123456789012345678901234567890\tfile\n']]),
    ('mixed tabs and spaces',
     'any',
     'type\t 1234567890123456789012345678901234567890 \tfile\n',
     [['any:1: separation does not match expectation (url#adding-packages-hash)',
       'type\t 1234567890123456789012345678901234567890 \tfile\n']]),
    ]


@pytest.mark.parametrize('testname,filename,string,expected', HashSpaces)
def test_HashSpaces(testname, filename, string, expected):
    warnings = util.check_file(m.HashSpaces, filename, string)
    assert warnings == expected