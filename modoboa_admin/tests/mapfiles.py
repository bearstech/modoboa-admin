"""Test map files generation."""

from modoboa.lib.test_utils import MapFilesTestCase as BaseTestCase


class MapFilesTestCase(BaseTestCase):

    """Test case for modoboa_admin."""

    extension = "modoboa_admin"

    MAP_FILES = [
        "sql-domains.cf", "sql-domain-aliases.cf", "sql-aliases.cf",
        "sql-domain-aliases-mailboxes.cf", "sql-catchall-aliases.cf",
        "sql-maintain.cf"
    ]
