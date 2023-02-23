"""Test module for the Sphinx JSON Domain."""
import sphinx_jsondomain


def test_normalize_object_name():
    """Test object name normalization."""
    previous_object_name = ':json:object:: test'
    result = sphinx_jsondomain.normalize_object_name(previous_object_name)
    assert result == ':json:object::-test'
