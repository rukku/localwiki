# Trick to force makemessages to detect these strings
gettext = lambda s: s

TYPE_ADDED = 0
TYPE_UPDATED = 1
TYPE_DELETED = 2
TYPE_DELETED_CASCADE = 3
TYPE_REVERTED = 4
TYPE_REVERTED_ADDED = 5
TYPE_REVERTED_DELETED = 6
TYPE_REVERTED_DELETED_CASCADE = 7
TYPE_REVERTED_CASCADE = 8
TYPE_CHOICES = (
    (TYPE_ADDED, gettext('Added')),
    (TYPE_UPDATED, gettext('Updated')),
    (TYPE_DELETED, gettext('Deleted')),
    (TYPE_DELETED_CASCADE, gettext('Deleted via cascade')),
    (TYPE_REVERTED, gettext('Reverted')),
    (TYPE_REVERTED_ADDED, gettext('Reverted/Added')),
    (TYPE_REVERTED_DELETED, gettext('Reverted/Deleted')),
    (TYPE_REVERTED_DELETED_CASCADE, gettext('Reverted/Deleted via cascade')),
    (TYPE_REVERTED_CASCADE, gettext('Reverted via cascade')),
)

ADDED_TYPES = [TYPE_ADDED, TYPE_REVERTED_ADDED]
DELETED_TYPES = [TYPE_DELETED, TYPE_DELETED_CASCADE, TYPE_REVERTED_DELETED]
REVERTED_TYPES = [
    TYPE_REVERTED, TYPE_REVERTED_ADDED, TYPE_REVERTED_DELETED,
    TYPE_REVERTED_DELETED_CASCADE, TYPE_REVERTED_CASCADE
]
