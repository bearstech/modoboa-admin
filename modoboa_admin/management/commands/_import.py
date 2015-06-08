import os.path
import sys
import csv

from modoboa.core.models import User
from modoboa.lib import events
from modoboa.lib.exceptions import Conflict

from modoboa_admin.views.import_ import (  # NOQA
    import_account, import_alias, import_forward, import_dlist,
    import_domain, import_domainalias
)


def import_csv(filename, options):
    superadmin = User.objects.filter(is_superuser=True).first()
    if not os.path.exists(filename):
        print('File not found')
        sys.exit(1)

    with open(filename, 'r') as f:
        reader = csv.reader(f, delimiter=';')
        for row in reader:
            if not row:
                continue

            try:
                fct = globals()["import_%s" % row[0].strip()]
            except KeyError:
                fct = events.raiseQueryEvent(
                    'ImportObject', row[0].strip())
                if not fct:
                    continue
                fct = fct[0]

            try:
                fct(superadmin, row, options)
            except Conflict:
                if options['continue_if_exists']:
                    continue

                raise Conflict(
                    "Object already exists: %s"
                    % options['sepchar'].join(row[:2])
                )
