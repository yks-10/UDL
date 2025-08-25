PAGINATION_COUNT=10

ACTIVE = 'active'
INACTIVE = 'inactive'
ARCHIVE = 'archive'
UNARCHIVE = 'unarchive'
STATUS_CHOICES = [
    (ACTIVE, 'Active'),
    (INACTIVE, 'Inactive'),
    (ARCHIVE, 'Archive'),
    (UNARCHIVE, 'UnArchive')
]

NEW = 'new'
PENDING='pending'
IN_PROGRESS = 'in progress'
COMPLETED = 'completed'
RESOLVED = 'resolved'
CANCELLED = 'cancelled'
ON_HOLD = 'on hold'
REJECTED = 'rejected'
IN_REVIEW = 'in review'
FAILED = 'failed'
CLOSED = 'closed'
ASSIGNED = 'assigned'
WAIT = 'wait'
ACCEPTED = 'accepted'
IMPORTANT = 'important'
ACTIVE = 'active'
INACTIVE = 'inactive'
ARCHIVE = 'archive'
UNARCHIVE = 'unarchive'
DECLINED = 'declined'
NOT_ACCEPTED = 'not accepted'
DUPLICATE = 'duplicate'
DECEASED = 'deceased'
NO_LONGER = 'no longer'
DISMISSED = 'dismissed'
PENDING_ACTIVATE = 'pending activate'
STATUS_CHOICES = [
    (NEW, 'New'),
    (ARCHIVE, 'Archive'),
    (UNARCHIVE, 'UnArchive'),
    (PENDING, 'Pending'),
    (IN_REVIEW, 'In Review'),
    (ACCEPTED, 'Accepted'),
    (NOT_ACCEPTED, 'Not Accepted'),
    (DECLINED, 'Declined'),
    (ACTIVE, 'Active'),
    (INACTIVE, 'Inactive'),
    (REJECTED, 'Rejected'),
    (DUPLICATE, 'Duplicate'),
    (DECEASED, 'Deceased'),
    (NO_LONGER, 'No Longer'),
    (DISMISSED, 'Dismissed'),
    (PENDING_ACTIVATE, 'Pending Activate'),
]


REGISTERED = 'registered'
UNREGISTERED = 'unregistered'
DECLINED = 'declined'
REGISTER_STATUS_CHOICES = [
    (REGISTERED, 'registered'),
    (UNREGISTERED, 'unregistered'),
    (DECLINED, 'declined')
]



CONSUMER = 'consumer'
AGENT = 'agent'
PARTNER = 'partner'
ADMIN = 'admin'
STAFF = 'staff'
USER_CHOICES = [
    (CONSUMER, 'Consumer'),
    (AGENT, 'Agent'),
    (PARTNER, 'Partner'),
    (ADMIN, 'Admin'),
    (STAFF, 'Staff')
]