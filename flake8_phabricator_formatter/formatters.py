import json
from flake8.formatting import base


class PhabricatorFormatter(base.BaseFormatter):
    """ok"""
    severity = {'E': 'error',
                'W': 'warning',
                }
    def format(self, error):

        errdict = {
            error.filename: [{
                "code": error.code,
                "description": error.text,
                "line": error.line_number,
                "char": error.column_number,
                "severity": self.severity.get(error.code[0], 'unknown'),
                "context": error.physical_line,
            }]
        }
        return json.dumps(errdict)
