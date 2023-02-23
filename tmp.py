from loguru import logger
from sphinx.application import Sphinx
import sphinx_jsondomain

s = Sphinx('.', '.', 'build/docs', 'build/docs/.doctrees', 'html')
jo = sphinx_jsondomain.JSONObject()

logger.debug(jo)
